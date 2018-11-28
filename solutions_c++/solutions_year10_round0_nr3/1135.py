#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <string>
#include <iomanip>
#include <cstdlib>
#include <bitset>
#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("C-small.in");
FILE * fout=fopen("C-small.out","w");
//ofstream fout("C-small.out");
//ifstream fin("C-large.in");
//ofstream fout("C-large.out");
int g[2000];
int main()
{
	int i,j,N,T,t,k,r;
	__int64 ans,p,total;
	fin>>T;
	for(t=1;t<=T;t++){
		ans=0;
		fin>>r>>k>>N;
		total=0;
		for(i=0;i<N;i++){
			fin>>g[i];
			total+=g[i];
		}
		for(i=j=0;i<r;i++){
			p=0;
			while(p+g[j]<=k&&p+g[j]<=total){
				p+=g[j];
				j++;
				if(j>=N)j%=N;
			}
			ans+=p;
		}
		fprintf(fout,"Case #%d: %I64d\n",t,ans);
	}
    return 0;
}
