#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

double mini_scalar(double* v1, double* v2, int n);
void sort1(double *v, int n);
void sort2(double *v, int n);

void print_arr(double *v, int n);

int main(){
	ifstream fin;
	fin.open("A-large.in");
	if(!fin){
		cout<<"open input failed"<<endl;
		return -1;
	}
	
	ofstream fout;
	fout.open("output.txt");
	if(!fout){
		cout<<"open output failed"<<endl;
		return -1;
	}

	int tn = 0;
	fin>>tn;
	cout<<"tn: "<<tn<<endl;
	int vn;
	double *v1, *v2;
	for(int i = 0; i < tn; i++){
		fin>>vn;
	//	cout<<"vn: "<<vn<<endl;
		v1 = new double[vn];
		v2 = new double[vn];
		
		for(int j = 0; j< vn; j++){
			fin>>v1[j];
		//	cout<<"j = "<<j<<endl;
		}
		for(int j = 0; j < vn; j++){
			fin>>v2[j];
		}
		fout<<"Case #"<<i+1<<": "<<setprecision(20)<<mini_scalar(v1,v2,vn)<<endl;
		
		//cout<<"end"<<endl;
		//delete[] v1;
		//delete[] v2;
	}
	cout<<"out"<<endl;
	
	fin.close();
	fout.close();
	return 0;
}

double mini_scalar(double *v1,double* v2, int n){
	//cout<<"enter in"<<endl;
	//print_arr(v1,n);
	//print_arr(v2,n);
	if(n > 1){
		sort1(v1,n);
		sort1(v2,n);
	}
	//cout<<"after sort"<<endl;
	//print_arr(v1,n);
	//print_arr(v2,n);
	double r = 0;
	for(int i = 0; i < n; i++){
		r += v1[i]*v2[n-1-i];
	}
	//cout<<"r =:"<<r<<endl;
	return r;
}

void sort1(double *v, int n){
	double tmp;
	for(int j = 0; j <= n-2; j++){
		for(int i = 0; i <= n-2-j; i++){
			if(v[i] < v[i+1]){
				tmp = v[i];
				v[i] = v[i+1];
				v[i+1] = tmp;
			}
		}
	}
}

void sort2(double *v, int n){
	double tmp;
	for(int j = 0; j <= n-2; j++){
		for(int i = 0; i < n-1-j; i++){
			if(v[i] > v[i+1]){
				tmp = v[i];
				v[i] = v[i+1];
				v[i+1] = tmp;
			}
		}
	}
}

void print_arr(double* v, int n){
	for(int i = 0; i < n; i++){
		cout<<v[i]<<" ";
	}
	cout<<endl;
}