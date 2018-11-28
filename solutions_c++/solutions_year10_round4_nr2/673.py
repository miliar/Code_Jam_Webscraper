#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cctype>
#include<cstdlib>
#include<cmath>
#include<cassert>
#include<iostream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<list>
#include<queue>
#include<deque>
#include<algorithm>
#include<cassert>
using namespace std ;

typedef long long LL ;
typedef vector<int> VI ;
typedef pair<int,int> para ;

const int INF = 1000000000 ;

#define PB push_back
#define MP make_pair
#define F first
#define S second
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define FOREACH(i,c) for(__typeof((c).begin())i = (c).begin();i!=(c).end(); ++i)
#define ALL(x) x.begin(),x.end()

const int N = 1077,P=13;

int D,p;

int w[2*N][P], kb[2*N], mop[N];

int main()
{
  scanf("%d",&D);
  FOR(I,1,D){
    printf("Case #%d: ",I);
    scanf("%d",&p);
    int ld=1<<p;
    REP(i,ld)
      scanf("%d",&mop[i]);
    int pocz = 1<<(p-1);
    REP(i,P){
      REP(j,pocz)
        scanf("%d",&kb[pocz+j]);
      pocz /= 2;
    }
    assert(pocz==0);
    pocz = 1<<p;
    REP(i,ld){
      // wypelniamy w[pocz+i][..]
      REP(j,p+1)
        w[pocz+i][j]=-1;
  //    w[pocz+i][p-mop[i]] = 0;
      FOR(x,p-mop[i],p)
        w[pocz+i][x]=0;
    }
    FORD(i,pocz-1,1){
      FOR(j,0,p){
        // wypelniamy w[i][j]
        int & aw = w[i][j];
        aw = -1;
        if(w[2*i][j]>=0 && w[2*i+1][j]>=0)
          aw = w[2*i][j] + w[2*i+1][j];
        if(j<p && w[2*i][j+1]>=0 && w[2*i+1][j+1]>=0){
          int kd = w[2*i][j+1] + w[2*i+1][j+1];
          kd += kb[i];
          if(aw == -1 || (aw>kd)){
            aw = kd;
          }
        }
      }
    }
    printf("%d\n",w[1][0]);
  }
	return 0 ;
}

