#include<iostream>
#include<fstream>
#include<cmath>
#include<cstdlib>
#include<cstring>
using namespace std;
FILE * fin = fopen("A-large.in","r");
FILE * fout = fopen("res","w");
//char a[N];
int main(){
	int t,n;  fscanf(fin,"%d",&t);
	unsigned long long k,p;
	for(int b=1;b<=t;b++){ 
		fscanf(fin,"%d%llu",&n,&k);
		p=pow(2.0,n);     cout<<p<<endl;
		fprintf(fout,"Case #%d: ",b);
		
		if(k%p==p-1) fprintf(fout,"ON\n");
		else fprintf(fout,"OFF\n");
	}
	return 0;
}
