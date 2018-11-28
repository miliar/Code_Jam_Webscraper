#include <stdio.h>
#include <vector>
using namespace std;

void main()
{
	FILE *f=fopen("A-small-attempt0.in","rb");
	if(!f)
	{
		printf("Fail to open file\n");
		return;
	}
	
	int T,A,B;
	float *out;
	fscanf(f,"%d\n",&T);
	out=new float[T];

	vector<float> vp;
	float min;
	for(int i=0;i<T;i++)
	{
		vp.clear();
		fscanf(f,"%d %d\n",&A,&B);
		float ex=0;
		float p=1.0f;
		for(int n=0;n<A;n++)
		{
			float temp;
			fscanf(f,"%f",&temp);
			p*=temp;
			vp.push_back(p);
		}
//option 1:
		ex=(B-A+1)*vp[A-1];
		ex+=(B-A+1+B+1)*(1-vp[A-1]);
		min=ex;
//op 2:
		for(int n=1;n<=A;n++)
		{
			if(n==A)
			{
				ex=A+B+1;
				if(ex<min) min=ex;
				break;
			}
			ex=(n+n+B-A+1)*(vp[A-n-1]);
			ex+=(n+n+B-A+1+B+1)*(1-vp[A-n-1]);
			if(ex<min)
				min=ex;
		}
//op 3:
		ex=1+B+1;
		if(ex<min)
			min=ex;

		out[i]=min;
	}
	fclose(f);

	f=fopen("out.txt","wb");
	for(int i=0;i<T;i++)
		fprintf(f,"Case #%d: %f\n",i+1,out[i]);
	fclose(f);


	delete[] out;

	return;
}