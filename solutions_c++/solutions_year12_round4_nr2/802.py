#include<iostream>
#include<fstream>
#include<string>
#include<cmath>

using namespace std;

const double PI=3.14159265358979323846264338327950288;
ifstream fin;
ofstream fout;

__int64 long_rand(){
	__int64 re=0;
	re += rand();
	re <<= 15;
	re += rand();
	return re;
}

void _main(){
	__int64 N,W,L;
	__int64 x[1002],y[1002],r[1002];
	__int64 i,j,k;
	fin>>N>>W>>L;
	for(i=0;i<N;i++){
		fin>>r[i];
	}
	
	__int64 x_try,y_try;
	for(i=0;i<N;i++){
		while(1){
			x_try = long_rand()%W;
			y_try = long_rand()%L;
			bool pass = true;
			for(j=0;j<i;j++){
				//int test=(x[j]-x_try)*(x[j]-x_try)+(y[j]-y_try)*(y[j]-y_try)-(r[i]+r[j])*(r[i]+r[j]);
				//fout<<test<<endl;
				if((x[j]-x_try)*(x[j]-x_try)+(y[j]-y_try)*(y[j]-y_try)<(r[i]+r[j])*(r[i]+r[j])){
					pass = false;
					break;
				}
			}
			if(pass){
				x[i]=x_try;
				y[i]=y_try;
				break;
			}
		}
	}
	
	for(i=0;i<N;i++) fout<<" "<<x[i]<<" "<<y[i];
}

int main(){
    fin.open("sample.in");
    fout.open("result.out");
    int T;
    fin>>T;
    for(int i=0;i<T;i++){
            fout<<"Case #"<<i+1<<":";
            cout<<"Case #"<<i+1<<" is runing"<<endl;
            _main();
            fout<<endl;
    }
}
