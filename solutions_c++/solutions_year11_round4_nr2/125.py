#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <sstream>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cmath>
using namespace std;

#define CLEAR(t) memset((t),0,sizeof(t))
#define FOR(i,a,b) for(__typeof(a)i=(a);i<=(b);++i)
#define FORD(i,a,b) for(__typeof(a)i=(a);i>=(b);--i)
#define REP(i,n) for(__typeof(n)i=0;i<(n);++i)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)

long long x[500][500][2];
long long y[500][500][2];
int s[500][500][2];
int w[500][500];

void _case(int casenum)
{
  int r,c,_d; scanf("%d%d%d ",&r,&c,&_d);
  int res=0;
  char ch;
  REP(i,r)REP(j,c) { scanf("%c ",&ch); w[i][j]=ch-'0'; }
  REP(i,r)REP(j,c) { s[i][j][1]=x[i][j][1]=y[i][j][1]=w[i][j]; }
  REP(i,r-1)REP(j,c-1)
  { 
    x[i][j][0]=x[i][j][1]+3*x[i+1][j][1]+x[i][j+1][1]+3*x[i+1][j+1][1];
    y[i][j][0]=y[i][j][1]+y[i+1][j][1]+3*y[i][j+1][1]+3*y[i+1][j+1][1];
    s[i][j][0]=s[i][j][1]+s[i+1][j][1]+s[i][j+1][1]+s[i+1][j+1][1];
  }
  FOR(k,3,min(r,c))
  {
    int z=k%2; int zz=z^1;
    REP(i,r-k+1)REP(j,c-k+1)
    {
      x[i][j][z]=x[i][j][zz]+x[i+1][j][zz]+2*s[i+1][j][zz]+x[i][j+1][zz]+x[i+1][j+1][zz]+2*s[i+1][j+1][zz];
      x[i][j][z]-=2*(x[i+1][j+1][z]+2*s[i+1][j+1][z]);
      x[i][j][z]+=w[i][j]+w[i][j+k-1]+(2*k-1)*w[i+k-1][j]+(2*k-1)*w[i+k-1][j+k-1];
      x[i][j][z]/=2;
      y[i][j][z]=y[i][j][zz]+y[i][j+1][zz]+2*s[i][j+1][zz]+y[i+1][j][zz]+y[i+1][j+1][zz]+2*s[i+1][j+1][zz];
      y[i][j][z]-=2*(y[i+1][j+1][z]+2*s[i+1][j+1][z]);
      y[i][j][z]+=w[i][j]+w[i+k-1][j]+(2*k-1)*w[i][j+k-1]+(2*k-1)*w[i+k-1][j+k-1];
      y[i][j][z]/=2;
      s[i][j][z]=s[i][j][zz]+s[i+1][j][zz]+s[i][j+1][zz]+s[i+1][j+1][zz];
      s[i][j][z]-=2*s[i+1][j+1][z];
      s[i][j][z]+=w[i][j]+w[i+k-1][j]+w[i][j+k-1]+w[i+k-1][j+k-1];
      s[i][j][z]/=2;

      long long xx=x[i][j][z]-(w[i][j]+w[i][j+k-1]+(2*k-1)*w[i+k-1][j]+(2*k-1)*w[i+k-1][j+k-1]);
      long long yy=y[i][j][z]-(w[i][j]+w[i+k-1][j]+(2*k-1)*w[i][j+k-1]+(2*k-1)*w[i+k-1][j+k-1]);
      long long ss=s[i][j][z]-(w[i][j]+w[i+k-1][j]+w[i][j+k-1]+w[i+k-1][j+k-1]);
      if((xx==ss*k)&&(yy==xx)) res=k;
/*
      long long xxx=0,yyy=0,sss=0;
      REP(ii,k)REP(jj,k)
        if(((ii!=0)&&(ii!=k-1))||((jj!=0)&&(jj!=k-1)))
        {
          xxx+=(2*ii+1)*w[i+ii][j+jj];
          yyy+=(2*jj+1)*w[i+ii][j+jj];
          sss+=w[i+ii][j+jj];
        }

//      printf("[%d,%d](%d)  %lld %lld  %lld\n",i,j,k,xx,yy,ss);
      if((xx!=xxx)||(yy!=yyy)||(ss!=sss))
      {
        printf("Daco sa posralo.\n");
//        printf("             %lld %lld  %lld\n",xxx,yyy,sss);
      }
*/
    }
  }
  printf("Case #%d: ",casenum);
  if(res) printf("%d\n",res); else printf("IMPOSSIBLE\n");
}

int main()
{
  int n;
  scanf("%d ",&n);
  FOR(i,1,n) _case(i);
  return 0;
}
