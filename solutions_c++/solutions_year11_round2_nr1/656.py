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
#define   rep(i,a,b)  for(int i=(a);i<(int)(b);i++)
#define   REP(i,n)     rep(i,0,n)
#define   FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define   clr(a)      memset((a),0,sizeof (a))
#define   SZ(a)         ((int)((a).size()))
#define   MP 		make_pair
#define   FI 		first
#define   SE 		second
#define   inf         1000000001
#define  MAXN     121
typedef long long  int64;
FILE *fin;
FILE *fout;
int T;
int N;
char cs[MAXN][MAXN];
int MOD=1000007;
double wp[MAXN];
double owp[MAXN];
double oowp[MAXN];
double rpi[MAXN];
int main()
{
   	fin=fopen("A-large.in","r");
	fout=fopen("output.txt","w");
	fscanf(fin,"%d",&T);
	for (int rounds=1;rounds<=T;rounds++)
	{
          printf("Case #%d:\n",rounds);
          fprintf(fout,"Case #%d:\n",rounds);
		  fscanf(fin,"%d",&N);
		  REP(i,N) fscanf(fin,"%s",cs[i]);
		  REP(i,N)
		  {
		      double t1=0,t2=0;
		      REP(j,N) if(cs[i][j]!='.') t2++,t1+=(cs[i][j]=='1');
		      wp[i]=t1/t2;
		  }
		  REP(i,N)
		  {
		      double t1=0,t2=0;
		      REP(j,N) if(cs[i][j]!='.')
		      {
		          t2++;double twp=0;double tt=0;
		          REP(k,N) if(i!=k&&cs[j][k]!='.') tt++,twp+=(cs[j][k]=='1');
		          t1+=twp/tt;
		      }
		      owp[i]=t1/t2;
		  }
		  REP(i,N)
		  {
		      double t1=0,t2=0;
		      REP(j,N) if(cs[i][j]!='.') t2++,t1+=owp[j];
		      oowp[i]=t1/t2;
		  }
		  REP(i,N) rpi[i]=0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
          REP(i,N)
          {
                printf("%.12lf\n",rpi[i]);
                fprintf(fout,"%.12lf\n",rpi[i]);
          }
	}
}
