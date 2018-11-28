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

FILE *fin=fopen("B-large.in","r");
FILE *fout=fopen("B-large.out","w");

int mx,my,a;

void init()
{
	fscanf(fin,"%d %d %d",&mx,&my,&a);
}

void search()
{
	int xa,ya,xb,yb,temp;

	for (xa=1; xa<=mx; xa++)
		for (yb=1; yb<=my; yb++)
			if (xa*yb-a>=0)
			{
				temp=xa*yb-a;
				if (temp==0)
				{
					xb=0;
					ya=0;
					fprintf(fout,"%d %d %d %d %d %d\n",0,0,xa,ya,xb,yb);
					return;
				}
				else
					for (xb=mx; xb>=1; xb--)
					{
						if (temp/xb>my)
							break;
						else
						{
							if (temp%xb==0)
							{
								ya=temp/xb;
								fprintf(fout,"%d %d %d %d %d %d\n",0,0,xa,ya,xb,yb);
								return;
							}
						}
					}
			}
	fprintf(fout,"IMPOSSIBLE\n");
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
