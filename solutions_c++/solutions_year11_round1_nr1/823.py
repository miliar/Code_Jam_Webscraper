/*Written by Vladimir Ignatiev aka Neacher (neacher@gmail.com)*/
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>

using namespace std;

typedef long long int64;
#define abs64(A) _abs64((int64)A)
#define INT64_MAX   0x7fffffffffffffffLL
#define INT64_MIN   (-INT64_MAX - 1LL)

int Pd, Pg;
int64 N;

bool is_N(int n)
{
	if((Pd==0)||(n==0))
	return Pd==n;

	return ((Pd*n)%100)==0;
}

bool f()
{	
	if((Pd!=0)&&(Pg==0)) return false;
	if((Pd!=100)&&(Pg==100)) return false;

	if(N>100) return true;//N=100;

	for(int i=0;i<=N;i++)
	{
		if(is_N(i))	return true;		
	}
	return false;//B
}

int main()
{
	FILE* In=fopen("A.in","r");if(!In) return 1;
	FILE* Out=fopen("A.res","w");if(!Out) return 2;

	int nCount,i;
	fscanf(In,"%d",&nCount);
	for(i=0;i<nCount;i++)
	{
		fprintf(Out,"Case #%d: ",i+1);
		printf("%d\n",i);
		fscanf(In,"%I64d%d%d",&N,&Pd,&Pg);

		fprintf(Out,"%s\n",f()?"Possible":"Broken");
	};
	fclose(In);
	fclose(Out);
	return 0;
}