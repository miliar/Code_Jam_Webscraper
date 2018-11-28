/*Written by Vladimir Ignatiev*/
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

#define rep(A,B) for(int A=0;A<B;++A)
#define repi(A,I,B) for(int A=I;A<B;++A)
#define repd(A,B) for(int A=B-1;A>=0;--A)
#define repdi(A,I,B) for(int A=B-1;A>=I;--A)
#define repall(A,F) for_each(A.begin(),A.end(),F);

typedef long long int64;
#define abs64(A) _abs64((int64)A)
#define INT64_MAX   0x7fffffffffffffffLL
#define INT64_MIN   (-INT64_MAX - 1LL)

#define MAX 500
int N, S[MAX];

map<int64,vector<int> > subsets;


int64 GetSum(int x)
{
	int64 sum=0;
	rep(i,20)
	{
		if(x&(1<<i)) sum+=S[i];
		if(x<(1<<i)) break;
	}
	return sum;
};

void print(FILE* Out,int x)
{
	rep(i,20)
	{
		if(x&(1<<i))
		{
			fprintf(Out,"%d",S[i]);
			if(x<(1<<i)) break;
			fprintf(Out," ");
		}
	}
	fprintf(Out,"\n");
};

int main()
{
	FILE* In=fopen("C.in","r");if(!In) return 1;
	FILE* Out=fopen("C.res","w");if(!Out) return 2;

	int nCount;
	fscanf(In,"%d",&nCount);
	rep(i,nCount)
	{
		fprintf(Out,"Case #%d:\n",i+1);
		printf("%d\n",i);
		fscanf(In,"%d",&N);
		
		rep(j,N)
			fscanf(In,"%d",S+j);

		subsets.clear();
		repi(j,1,(1<<20))
		{
			subsets[GetSum(j)].push_back(j);
			if(subsets[GetSum(j)].size()>1) break;
		}

		if(subsets.size()==0)
			fprintf(Out,"%s\n","Impossible");
		else
		{
			for(map<int64,vector<int> >::iterator pos=subsets.begin();pos!=subsets.end();++pos)
			{
				if(pos->second.size()>1)
				{
					rep(j,pos->second.size())
						print(Out,pos->second[j]);

				    break;		
				}
			}
		}
	};
	fclose(In);
	fclose(Out);
	return 0;
}