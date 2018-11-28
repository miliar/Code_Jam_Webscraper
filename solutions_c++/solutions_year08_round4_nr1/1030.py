#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
#define   max(a,b)    ((a)>(b)?(a):(b))
#define   min(a,b)    ((a)<(b)?(a):(b))
#define   sqr(a)         ((a)*(a))
#define   rep(i,a,b)  for(i=(a);i<(b);i++)
#define   REP(i,n)     rep(i,0,n)
#define   inf         1000000000
FILE *fin;
FILE *fout;
typedef struct node 
{
	int gate;
	int change;
	int value;
}node;
node tree[10010];
int M,V;
__int64 solve(int tid,int vue)
{
    if (tid>=(M-1)/2+1)
    {
		if (vue!=tree[tid].value)
		{
			return inf;
		}
		else 
			return 0;
    }
	if (tree[tid].change==0)
	{
		__int64 tret=0;
		if (tree[tid].gate==1)
		{
			if (vue==1)
			{
				tret=solve(tid*2,1)+solve(tid*2+1,1);
				return tret;
			}
			else
			{
				tret=min(solve(tid*2,0),solve(tid*2+1,0));
				return tret;
			}
		}
		else
		{
				if (vue==1)
				{
						tret=min(solve(tid*2,1),solve(tid*2+1,1));
					
					return tret;
				}
				else
				{
					tret=solve(tid*2,0)+solve(tid*2+1,0);
					return tret;
				}
		}
	}
	else 
	{
        __int64 stid21=solve(tid*2,1);
		__int64 stid20=solve(tid*2,0);
		__int64 stid211=solve(tid*2+1,1);
		__int64 stid210=solve(tid*2+1,0);
		if (vue==1)
		{
            if (tree[tid].gate==1)
            {
                __int64 tret1=stid21+stid211;
                __int64 tret2=1+min(stid21,stid211);
				return min(tret1,tret2);
            }
			else if (tree[tid].gate==0)
			{
				__int64 tret1=1+stid21+stid211;
                __int64 tret2=min(stid21,stid211);
				return min(tret1,tret2);
			}
		}
		else if (vue==0)
		{
			if (tree[tid].gate==1)
            {
				__int64 tret1=1+stid20+stid210;
                __int64 tret2=min(stid20,stid210);
				return min(tret1,tret2);
            }
			else if (tree[tid].gate==0)
			{
				__int64 tret1=stid20+stid210;
                __int64 tret2=1+min(stid20,stid210);
				return min(tret1,tret2);
			}
		}
	}
	return inf;
}
int main()
{
   	fin=fopen("A-small-attempt0.in","r");
	fout=fopen("output.txt","w");
	__int64 i,j,k;
	int N;
	fscanf(fin,"%d",&N);
    int rounds;
	for (rounds=1;rounds<=N;rounds++)
	{
		  REP(i,10010)  tree[i].gate=0,tree[i].change=0,tree[i].value=-1;
          fscanf(fin,"%d%d",&M,&V);
		  for (i=1;i<=(M-1)/2;i++)
		  {
			  fscanf(fin,"%d%d",&tree[i].gate,&tree[i].change);
		  }
		  for (i=(M-1)/2+1;i<=M;i++)
		  {
			  fscanf(fin,"%d",&tree[i].value);
		  }
		  __int64 ret=solve(1,V);
		  if (ret>=inf)
		  {
			  printf("Case #%d: IMPOSSIBLE\n",rounds);
              fprintf(fout,"Case #%d: IMPOSSIBLE\n",rounds);
			  continue;
		  }
		  printf("Case #%d: %I64d\n",rounds,ret);
          fprintf(fout,"Case #%d: %I64d\n",rounds,ret);
	}
}
