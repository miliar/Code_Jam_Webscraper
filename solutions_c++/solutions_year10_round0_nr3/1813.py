#include<iostream>
#include<cmath>
#include<cstdlib>
#include<cstdio>
#include<cstring>
using namespace std;
unsigned long long int s[1000],a[1000];
int pos[1000];
FILE * fin=fopen("C-large.in","r");
FILE * fout=fopen("res.txt","w");
int main(){
	int t;
	unsigned long long r,ki,tot;
	int n; fscanf(fin,"%d",&t);
	for(int i=1;i<=t;i++){  
		fscanf(fin,"%llu%llu",&r,&ki);
		fscanf(fin,"%d",&n); 
		for(int j=0;j<n;j++) { fscanf(fin,"%llu",&a[j]); }
		unsigned long long int x=0;
		for(int j=0;j<n;j++) { int k=(j+1)%n; x=a[j]; while(k!=j && x+a[k]<=ki) { x+=a[k]; k=(k+1)%n; }  if(k<0) k+=n; 
		                                                                                         if(x>ki) s[j]=pos[j]=-1;
		                                                                                         else { s[j]=x; pos[j]=k; }
		                     }
		
		                     int p=0; tot=0;
		for(unsigned long long j=0;j<r;j++){ tot+=s[p]; p=pos[p]; }
		fprintf(fout,"Case #%d: %llu\n",i,tot);
	}
	return 0;
}
