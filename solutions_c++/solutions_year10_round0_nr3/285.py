#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>
#include <ctime>
#include <queue>
using namespace std;
#define   max(a,b)    ((a)>(b)?(a):(b))
#define   min(a,b)    ((a)<(b)?(a):(b))
#define   sqr(a)         ((a)*(a))
#define   rep(i,a,b)  for(i=(a);i<(b);i++)
#define   REP(i,n)     rep(i,0,n)
#define   clr(a)      memset((a),0,sizeof (a));
#define   mabs(a)     ((a)>0?(a):(-(a))) 
#define   inf         1000000000
#define  MAXM     (1<<7)  
#define  MAXN     1010
#define  eps      1e-6
#define  MOD      50261
typedef __int64 int64;
FILE *fin;
FILE *fout;
int T;
int R,K,N;
int64 v[MAXN];
bool visited[MAXN];
int64 dv[MAXN];
int64 dr[MAXN];
int64 doit(int now,int r,int n)
{
	if(r==0) return 0;
		clr(dv);clr(dr);
		int i;
		int64 tdv=0;
		int64 tdr=0;
		while(true)
		{
            i=now;
			dv[now]=tdv;
			dr[now]=tdr;
			int64 tv=0;
			while (true)
			{
				if(tv+v[i]>K)
                {
					break;
				}
				else 
				{
                    tv+=v[i];
					i=(i+1)%n;
				}
			}
			tdv=dv[now]+tv;
			tdr=dr[now]+1;
			if(tdr==r)
			{
				return tdv;
			}
			now=i;
		} 
}
int main()
{
   	fin=fopen("C-large.in","r");
	fout=fopen("output.txt","w");
	int i,j,k;
	int N;
	fscanf(fin,"%d",&T);
    int rounds;
	for (rounds=1;rounds<=T;rounds++)
	{
		clr(v);
		int64 total=0;
		fscanf(fin,"%d%d%d",&R,&K,&N);
		REP(i,N) 
		{
			int u;fscanf(fin,"%d",&u);
			v[i]=u;
			total+=u;
		}
		if(total<=K)
		{
			int64 ret=total*R;
            printf("Case #%d: %I64d\n",rounds,ret);
            fprintf(fout,"Case #%d: %I64d\n",rounds,ret);
			continue;
		}
		clr(dv);clr(dr);
		clr(visited);
		int now=0;
		int64 tdv=0;
		int64 tdr=0;
		int64 ddv,ddr,ret;
		while(!visited[now])
		{
			visited[now]=true;
			dv[now]=tdv;
			dr[now]=tdr;
            i=now;
			int64 tv=0;
			while (true)
			{
				if(tv+v[i]>K)
                {
					break;
				}
				else 
				{
                    tv+=v[i];
					i=(i+1)%N;
				}
			}
			tdv=dv[now]+tv;
			tdr=dr[now]+1;
			if(tdr==R)
			{
				int64 ret=tdv;
			   printf("Case #%d: %I64d\n",rounds,ret);
               fprintf(fout,"Case #%d: %I64d\n",rounds,ret);
			   goto nxt;
			}
			now=i;
		} 
		ddv=tdv-dv[now];
		ddr=tdr-dr[now];
		ret=dv[now];
		R-=dr[now];
		ret+=((R/ddr)*ddv);
		R%=ddr;
		ret+=doit(now,R,N);
	    printf("Case #%d: %I64d\n",rounds,ret);
        fprintf(fout,"Case #%d: %I64d\n",rounds,ret);
nxt:   ;
	}
}
