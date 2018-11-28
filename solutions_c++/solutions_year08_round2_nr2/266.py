#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<algorithm>
#define MinNum(a,b) ((a)>(b)?(b):(a))
#define MaxNum(a,b) ((a)<(b)?(b):(a))
#define INF INF32
#define NA (-1)

#define uint64 unsigned long long
#define _1 ((uint64)1)
#define int64 long long
/*
#define uint64 unsigned __int64
#define _1 ((uint64)1)
#define int64 __int64
*/

const int64 INF64=(_1<<63)-1;
const int INF32=(_1<<31)-1;

using namespace std;

/*
class Temp{
public:
	void Ret()
	{
	}
};
*/

FILE *fin=fopen("B-small-attempt0.in","r");
FILE *fout=fopen("B-small-attempt0.out","w");

#define MAXN 1000011

int n,nd;
int64 a,b,p;
int64 d[MAXN];
int f[MAXN];
set<int64> s;

int e[MAXN];
int size[MAXN];

void init()
{
	int i;
	fscanf(fin,"%I64d %I64d %I64d",&a,&b,&p);
	n=b-a+1;
	for (i=0; i<n; i++)
		f[i]=0;
	nd=0;
	s.clear();
	for (i=0; i<MAXN; i++)
	{
		e[i]=i;
		size[i]=1;
	}
}

int find(int id)
{
	if (id==e[id])
		return id;
	e[id]=find(e[id]);
	return e[id];
}

void comb(int e1,int e2)
{
	e1=find(e1);
	e2=find(e2);
	if (size[e1]>=size[e2])
	{
		size[e1]+=size[e2]; e[e2]=e1;
	}
	else
	{
		size[e2]+=size[e1]; e[e1]=e2;
	}
}


void search()
{
	int ret=0;
	int64 i,j,k,x;

	for (i=a; i<=b; i++)
	{
			x=i;
			for (j=2; j*j<=i; j++)
			{
				if (x%j==0&&j>=p)
				{
					if (s.find(j)==s.end())
					{
						d[nd++]=j;
						s.insert(j);
						for (k=i; k<=b; k+=j)
							comb(i-a,k-a);
					}
				}
				while (x%j==0)
					x/=j;
			}
			if (x>=p)
			{
				if (s.find(x)==s.end())
				{
					d[nd++]=x;
					s.insert(x);
					for (k=i; k<=b; k+=x)
						comb(i-a,k-a);
				}
			}
	}
	for (i=a; i<=b; i++)
		f[find(i-a)]=1;
	for (i=a; i<=b; i++)
		ret+=f[i-a];
	fprintf(fout,"%d\n",ret);
}

int main()
{
	int testdata,i;

	fscanf(fin,"%d",&testdata);
	for (i=0; i<testdata; i++)
	{
		fprintf(fout,"Case #%d: ",i+1);
		init();
		search();
	}
	return 0;
}
