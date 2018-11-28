#include <iostream>
#include <string>
#include <vector>
#include <OpenCL/OpenCL.h>
using namespace std;
typedef unsigned int uint;

const char *src = "\n" \
"__kernel void flow(__global unsigned int *alt, __global unsigned int *par, const unsigned int w, const unsigned int count) {\n" \
"  unsigned int i = get_global_id(0);\n"\
"  if (i<count) {\n" \
"    unsigned int b = alt[i], y=i/w, x=i%w, j=i;\n" \
"    if (y>0)       if (alt[i-w] < b) b=alt[(j = i-w)];\n" \
"    if (x>0)       if (alt[i-1] < b) b=alt[(j = i-1)];\n" \
"    if (x+1<w)     if (alt[i+1] < b) b=alt[(j = i+1)];\n" \
"    if (i+w<count) if (alt[i+w] < b)        j = i+w;\n" \
"    par[i] = j;\n" \
"  }\n"\
"}\n\n"\
"__kernel void opt(__global unsigned int *par, const unsigned int count) {\n" \
"  unsigned int i = get_global_id(0);\n"\
"  if (i<count) {\n" \
"    unsigned int j=i;\n" \
"    while(j!=par[j]) j=par[j];\n" \
"    par[i]=j;\n" \
"  }\n"\
"}\n";
#define SIZE 10000

int main() {
	int err;
	size_t global; //, local;
	cl_device_id device_id;
	cl_context context;
	cl_command_queue queue;
	cl_program program;
	cl_kernel flow, opt;
	cl_mem alt, par;
	
	clGetDeviceIDs(NULL, CL_DEVICE_TYPE_GPU, 1, &device_id, NULL);
	context = clCreateContext(0, 1, &device_id, NULL, NULL, &err);
	if (err != CL_SUCCESS) cout << "clCreateContext " << err << endl;
	queue = clCreateCommandQueue(context, device_id, 0, &err);
	if (err != CL_SUCCESS) cout << "clCreateCommandQueue " << err << endl;
	program = clCreateProgramWithSource(context, 1, (const char **)&src, NULL, &err);
	if (err != CL_SUCCESS) cout << "clCreateProgramWithSource " << err << endl;
	err = clBuildProgram(program, 0, NULL, NULL, NULL, NULL);
    if (err != CL_SUCCESS)
    {
        size_t len;
        char buffer[2048];
        cout << "Error: Failed to build program executable!" << endl;
        clGetProgramBuildInfo(program, device_id, CL_PROGRAM_BUILD_LOG, sizeof(buffer), buffer, &len);
        cout << buffer << endl;
        exit(1);
    }
	flow = clCreateKernel(program, "flow", &err);
	if (!flow || err != CL_SUCCESS) cout << "clCreateKernel " << err << endl;
	opt = clCreateKernel(program, "opt", &err);
	if (!flow || err != CL_SUCCESS) cout << "clCreateKernel " << err << endl;
	
	alt = clCreateBuffer(context, CL_MEM_READ_ONLY, sizeof(uint) * SIZE, NULL, NULL);
	par = clCreateBuffer(context, CL_MEM_READ_WRITE, sizeof(uint)* SIZE, NULL, NULL);
	if (!alt || !par) cout << "clCreateBuffer " << err << endl;
	
	err = clSetKernelArg(flow, 0, sizeof(cl_mem), &alt);
	err|= clSetKernelArg(flow, 1, sizeof(cl_mem), &par);
	err|= clSetKernelArg(opt, 0, sizeof(cl_mem), &par);
	if (err != CL_SUCCESS) cout << "clSetKernelArg " << err << endl;

	uint T;
	cin >> T;
	
	
	for (uint i=0; i<T; ++i)
	{
		uint h,w,sz;
		cin >> h >> w;
		uint in[sz = h*w], out[sz];
		for (int j=0; j<sz; ++j)
			cin >> in[j];
		
		err = clSetKernelArg(flow, 2, sizeof(uint), &w);
		err|= clSetKernelArg(flow, 3, sizeof(uint), &sz);
		err|= clSetKernelArg(opt, 1, sizeof(uint), &sz);
		if (err != CL_SUCCESS) cout << "clSetKernelArg " << err << endl;
		
		err = clEnqueueWriteBuffer(queue, alt, CL_TRUE, 0, sizeof(uint) * sz, in, 0, NULL, NULL);
		if (err != CL_SUCCESS) cout << "clEnqueueWriteBuffer " << err << endl;
		
		global = sz;
		err = clEnqueueNDRangeKernel(queue, flow, 1, NULL, &global, NULL, 0, NULL, NULL);
		if (err != CL_SUCCESS) cout << "clEnqueueNDRangeKernel " << err << endl;
		
		err = clEnqueueNDRangeKernel(queue, opt, 1, NULL, &global, NULL, 0, NULL, NULL);
		if (err != CL_SUCCESS) cout << "clEnqueueNDRangeKernel " << err << endl;
		
		clFinish(queue);
		
		err = clEnqueueReadBuffer(queue, par, CL_TRUE, 0, sizeof(uint) * sz, out, 0, NULL, NULL);
		if (err != CL_SUCCESS) cout << "clEnqueueReadBuffer " << err << endl;
		
		string myout;
		myout.resize(sz,' ');
		
		cout << "Case #" << (i+1) << ": " << endl;
		
		char z = 'a';
		for (uint j=0; j<sz; ++j)
		{
			uint k=out[j];
			//while (k!=out[k]) k=out[k];
			if (myout[k] == ' ') myout[k] = z++;
			myout[j] = myout[k];
			cout << myout[j]; 
			if (j%w+1 == w) cout << endl; else cout << " ";
		}
		

	}
	
	clReleaseMemObject(alt);
    clReleaseMemObject(par);
    clReleaseProgram(program);
    clReleaseKernel(flow);
	clReleaseKernel(opt);
    clReleaseCommandQueue(queue);
    clReleaseContext(context);

	
	return 0;
}