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

int D,r,k,n,wg[2007],byla[1007];
LL zar,zm[1007];

int main()
{
  scanf("%d",&D);
  FOR(I,1,D){
    printf("Case #%d: ",I);
    scanf("%d %d %d",&r,&k,&n);
    REP(i,n){
      scanf("%d",&wg[i]);
      wg[i+n] = wg[i];
      byla[i] = 0;
    }
    int ag = 0, rest = 0;
    zar = 0;
    FOR(i,1,r){
      if(byla[ag]>0){
        LL dz = zar - zm[ag];
        int okres = i-byla[ag];
        int lot = (r-i+1)/okres;
        zar += dz * lot;
        rest = (r-i+1)%okres;
        break;
      }
      zm[ag]=zar;
      byla[ag]=i;
      int lm=0;
      for(int j=ag;j<ag+n;j++){
        if(lm+wg[j] > k){
          ag=j%n;
          break;
        }
        zar+=wg[j];
        lm+=wg[j];
      }
    }
    while(rest>0){
      rest--;
      int lm=0;
      for(int j=ag;j<ag+n;j++){
        if(lm+wg[j] > k){
          ag=j%n;
          break;
        }
        zar+=wg[j];
        lm+=wg[j];
      }
    }
    printf("%lld\n",zar);
  }
	return 0 ;
}

