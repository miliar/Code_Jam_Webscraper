
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <cmath>

using namespace std;

FILE *fin,*fout;
long long x[100000];
long long y[100000];

int n;

int main()
{
	int num,run,i,j,k,count;
	int P,K,L; int A[100000],B[10000];

	long long area,a,b,c;
	fin = fopen("input","r");
	fout = fopen("output","w");
	fscanf(fin,"%d",&num);

	for(run=1;run<=num;run++)
	{
		fscanf(fin,"%d",&P);
		fscanf(fin,"%d",&K);
		fscanf(fin,"%d",&L);
		cout<<P<<" "<<K<<"  "<<L<<"\n";
for(i=0;i<L;++i)
		fscanf(fin,"%d",&A[i]);
sort(A,A+L);
for(i=0;i<L;++i)
cout<<A[i]<<"\t";
k=L-1;
for(i=0;i<P;++i)
for(j=0;j<K;++j){
B[k]=i+1;
k--;
}
cout<<".........."<<"\n";
for(i=0;i<L;++i)
cout<<B[i]<<"\n";
c=0;
for(i=0;i<L;++i)
c=c+B[i]*A[i];
		printf("Case #%d:  %d \n",run,c);
		fprintf(fout,"Case #%d: %d\n",run,c);
	}
	return 0;
}
