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
#define  MAXN      33
typedef __int64 int64;
FILE *fin;
FILE *fout;
__int64 shu[MAXN];
int M;
int N,K;
int main()
{
   	fin=fopen("A-large.in","r");
	fout=fopen("output.txt","w");
	int i,j,k;
	fscanf(fin,"%d",&M);
	shu[1]=1;
	rep(i,2,31) shu[i]=2*shu[i-1]+1;
	rep(i,1,31)printf("%d %I64d\n",i,shu[i]);
    int rounds;
	for (rounds=1;rounds<=M;rounds++)
	{
		  fscanf(fin,"%d%d",&N,&K);
		  K%=(shu[N]+1);
		  if(K==shu[N])
		  {
                printf("Case #%d: ON\n",rounds);
                fprintf(fout,"Case #%d: ON\n",rounds);
		  }
		  else 
		  {
                printf("Case #%d: OFF\n",rounds);
                fprintf(fout,"Case #%d: OFF\n",rounds);
		  }
	}
}
