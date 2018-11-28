#include <iostream>
#include <fstream>
#include <iomanip>
#include <stdio.h>
using namespace std;

int main(){
	ifstream infile;
	char inname[50];
	cout<<"input input filename: ";
	cin>>inname;	
	infile.open(inname);
	FILE *outfile;
	outfile=fopen("p1Ans.txt","w");
	int T;
	infile>>T;
	string line;
	getline(infile,line);//?
	cout<<"test lineget is "<<line<<endl;//test
	int I=1;
	while(I<=T){
		//input
		int A=-1,N=-1;
		infile>>A;
		infile>>N;
		double *p=new double[A];
		for(int i=0;i<A;++i){
			infile>>p[i];
		}
		//calculate
		double *c=new double[A+2];
		for(int i=0;i<(A+2);++i){
			c[i]=0;
		}
		double *totp=new double[A+1];
		for(int i=0;i<(A+1);++i){
			totp[i]=1;
			for(int j=0;j<i;++j){
				totp[i]*=p[j];
			}
			if (i!=A) totp[i]*=1-p[i];
		} 	
		c[0]=(2*N+2-A)*(1-totp[A])+(N-A+1)*totp[A];
		for(int m=1;m<=A;++m){
			for(int i=0;i<(A-m);++i){
				c[m]+=(2*m+2*N+2-A)*totp[i];
			}
			for(int i=(A-m);i<(A+1);++i){
				c[m]+=(2*m+N-A+1)*totp[i];
			}		
		}	
		c[A+1]=2+N;		
		//select min
		double min=c[0];
		for(int i=1;i<(A+2);++i){
			if(c[i]<min) min=c[i];	
		}
		delete []p;
		delete []c;
		delete []totp;
		//output	
		fprintf(outfile,"Case #%d: %.6f\n",I,min);
		++I;
	}
	fclose(outfile);
return 0;
}
