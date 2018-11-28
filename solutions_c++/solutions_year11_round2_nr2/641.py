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
#define  eps          1e-10
typedef long long  int64;
FILE *fin;
FILE *fout;
int T;
int N,D;
vector<double> vd;
double isok(double mid)
{
    double pre=vd[0]-mid;
    rep(i,1,SZ(vd))
    {
        double vpos=max(vd[i]-mid,pre+D);
        if(fabs(vpos-vd[i])>mid) return false;
        pre=vpos;
    }
    return true;
}
int main()
{
   	fin=fopen("B-small-attempt0.in","r");
	fout=fopen("output.txt","w");
	fscanf(fin,"%d",&T);
	for (int rounds=1;rounds<=T;rounds++)
	{
          printf("Case #%d: ",rounds);
          fprintf(fout,"Case #%d: ",rounds);
		  fscanf(fin,"%d%d",&N,&D);
		  vd.clear();
		  REP(i,N)
		  {
		      int p,v;fscanf(fin,"%d%d",&p,&v);
		      REP(j,v) vd.push_back(1.0*p);
		  }
		  sort(vd.begin(),vd.end());
          double l=0,r=1e8;
          REP(step,50)
          {
              double mid=(l+r)/2;
              if(isok(mid)) r=mid;
              else l=mid;
          }
          printf("%.10lf\n",r);
          fprintf(fout,"%.10lf\n",r);
	}
}
