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

int N, L, H;
int a[10001];

int f()
{	
	for(int i=L;i<=H;i++)
	{
		int j;
		for(j=0;j<N;j++)
			if(i>a[j]) 
			{
				if(i%a[j]) break;
			}
			else
				if(a[j]%i) break;

		if(j==N) return i;
	}
		
	return 0;
}

int main()
{
	FILE* In=fopen("C.in","r");if(!In) return 1;
	FILE* Out=fopen("C.res","w");if(!Out) return 2;

	int nCount,i;
	fscanf(In,"%d",&nCount);
	for(int n=0;n<nCount;n++)
	{
		fprintf(Out,"Case #%d: ",n+1);
		printf("%d\n",n);
		fscanf(In,"%d%d%d",&N,&L,&H);
		for(int i=0;i<N;i++)
			fscanf(In,"%d",a+i);

		int res=f();
		if(!res)
			fprintf(Out,"%s\n","NO");
		else
			fprintf(Out,"%d\n",res);
	};
	fclose(In);
	fclose(Out);
	return 0;
}