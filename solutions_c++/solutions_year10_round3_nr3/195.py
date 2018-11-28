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

const int N = 537;

int tab[N][N];

int dl[N][N];

char buf[N];

int D;

typedef pair<int, para> troj;

priority_queue<troj> pq;

int lw,tw[N];

bool ok(int a, int b, int d){
  return tab[a][b]<2 && tab[a+d-1][b]<2
        && tab[a][b+d-1]<2 && tab[a+d-1][b+d-1]<2;
}

int main()
{
  scanf("%d",&D);
  FOR(I,1,D){
    printf("Case #%d: ",I);
    int n,m;
    scanf("%d %d",&n,&m);
    REP(j,n){
      scanf("%s",buf);
      REP(i,m/4){
        int l=buf[i]-'0';
        if('A'<=buf[i] && buf[i]<='Z')
          l=buf[i]-'A'+10;
        FORD(b,3,0){
          if(l & (1<<b))
            tab[j][i*4+(3-b)]=1;
          else
            tab[j][i*4+(3-b)]=0;
        }
      }
    }
  /*  REP(j,n){
      printf("\n");
      REP(i,m)
        printf("%d",tab[j][i]);
    }*/
    while(!pq.empty())
      pq.pop();
    FORD(j,n-1,0)
      FORD(i,m-1,0){
        if(j==n-1 || i==m-1){
          dl[j][i]=1;
          pq.push(MP(dl[j][i],MP(-j,-i)));
          continue;
        }
        //j<n-1 && i<m-1
        if(tab[j+1][i] != tab[j][i+1] || tab[j][i]!=tab[j+1][i+1] || tab[j][i]==tab[j+1][i]){
          dl[j][i]=1;
          pq.push(MP(dl[j][i],MP(-j,-i)));
          continue;
        }
        int x = min(dl[j+1][i], dl[j][i+1]);
        if(tab[j+x][i+x]==tab[j][i])
          dl[j][i]=x+1;
        else
          dl[j][i]=x;
        pq.push(MP(dl[j][i],MP(-j,-i)));
      }
    REP(i,n+1)
      tw[i]=0;
    lw=0;
    while(!pq.empty()){
      troj akt = pq.top();
      pq.pop();
      int a1=-akt.S.F,b1=-akt.S.S;
      int d=akt.F;
      if(ok(a1,b1,d)){
        tw[d]++;
        if(tw[d]==1)
          lw++;
        FOR(j,a1,a1+d-1)
          FOR(i,b1,b1+d-1)
          tab[j][i]=2;
      }
      else{
        //not ok
        if(tab[a1][b1]==2)
          d=0;
        while(d>0 && !ok(a1,b1,d))
          d--;
        if(d>0) // bo mogl byc lewy gorny rog zuzyty
          pq.push(MP(d,MP(-a1,-b1)));
      }
    }
    printf("%d\n",lw);
    FORD(i,n,1)
      if(tw[i]>0)
        printf("%d %d\n",i,tw[i]);
  }
	return 0 ;
}

