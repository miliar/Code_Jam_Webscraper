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
#include <functional>

using namespace std;

typedef long long int64;
#define abs64(A) _abs64((int64)A)
#define INT64_MAX   0x7fffffffffffffffLL
#define INT64_MIN   (-INT64_MAX - 1LL)

int L, N, C; 
int64 t;
int a[10000];

inline int getA(int pos)
{
	return a[pos%C]*2;
};

int64 f()
{	
	int64 time=0;
	int64 rem;
	int i;

	for(i=0;i<N;i++)
	{
		int nextA=getA(i);
		if(time+nextA>t)
		{
			rem=time+nextA-t;
			time+=nextA;
			break;
		}
		time+=nextA;
	}
	
	vector<int64> max;
	max.push_back(rem);
	
	for(++i;i<N;i++)
	{
		int nextA=getA(i);
		time+=nextA;
		max.push_back(nextA);
	}
	
	std::sort(max.begin(),max.end(),greater<int64>());

	for(int i=0;((i<L)&&(i<max.size()));i++)
	{
		time-=max[i]/2;
	}
			
	return time;
}

int main()
{
	FILE* In=fopen("B.in","r");if(!In) return 1;
	FILE* Out=fopen("B.res","w");if(!Out) return 2;

	int nCount,i;
	fscanf(In,"%d",&nCount);
	for(int n=0;n<nCount;n++)
	{
		fprintf(Out,"Case #%d: ",n+1);
		printf("%d\n",n);
		fscanf(In,"%d%I64d%d%d",&L,&t,&N,&C);
	
		for(int i=0;i<C;i++)
			fscanf(In,"%d",a+i);

		fprintf(Out,"%I64d\n",f());
	};
	fclose(In);
	fclose(Out);
	return 0;
}