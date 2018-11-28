//Tadrion
#include <cstdio>
#include <vector>
#include <iostream>
#include <deque>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
using namespace std;
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define CLEAR(x) (memset(x,0,sizeof(x)))
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define VAR(v, n) __typeof(n) v = (n)
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define FOREACH(i, c) for(VAR(i,(c).begin()); i != (c).end(); ++i)
#define DBG(v) cout<<#v<<" = "<<v<<endl; 
#define IN(x,y) ((y).find(x)!=(y).end())
#define ST first
#define ND second
#define PB push_back
#define PF push_front
typedef long long int LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
int T,S,R,N,t,X;
int w[1010],b[1010],e[1010],pos;
vector<pair < int, pair<int,int> > > v;
vector<PII> v2,v3;
double ti;
int main() {
  scanf("%d",&T);
  for(int c = 1; c <= T; c++) {
    ti = 0.0;
    pos = 0;
    scanf("%d %d %d %d %d",&X,&S,&R,&t,&N);
    v.clear();
    v2.clear();
    for(int i = 1; i <= N; i++) {
      scanf("%d %d %d",&b[i],&e[i],&w[i]);   
      v.push_back(pair<int, pair<int,int> >( b[i], PII(e[i],w[i]) ) );
    }
    sort(v.begin(),v.end());
    int j = 0;
    while(pos < X) {
      if(j < v.size()) {
	if(v[j].ST == pos) {
	  v2.push_back(PII(v[j].ND.ST - v[j].ST,v[j].ND.ND));
	  pos = v[j].ND.ST;
	  j++;
      }
	else {
	  v2.push_back(PII(v[j].ST - pos,0));
	  pos = v[j].ST;
	}
      }
      else {
	v2.push_back(PII(X-pos,0));
	pos = X;
      }
    }
    v3.clear();
    for(int k = 0; k < v2.size(); k++)
      v3.push_back(PII(v2[k].ND,v2[k].ST));
    sort(v3.begin(),v3.end());
    for(int k = 0; k < v3.size(); k++) {
      if(ti >= t) {
	//printf("1 %lf\n",((double) v2[k].ST) / ((double) (v2[k].ND + S) ));
	ti += ((double) v3[k].ND) / ((double) (v3[k].ST + S) );
      }
      else if(ti < t && ti + ((double) v3[k].ND) / ((double) (v3[k].ST + R) ) <= t) {
	//	printf("2 %lf\n",((double) v2[k].ST) / ((double) (v2[k].ND + R) ));
	ti += ((double) v3[k].ND) / ((double) (v3[k].ST + R) );
      }
      else {
        double odl = (R+v3[k].ST)*(t-ti);
	ti += odl / ( (double) (v3[k].ST + R) );
	ti += (v3[k].ND - odl) / ( (double) (v3[k].ST + S) );
	//printf("!\n");
//printf("3 %lf\n",((double) v2[k].ST) / ((double) (v2[k].ND + R) ));
      }
      //printf("%d %d %lf\n",v2[k].ST,v2[k].ND,ti);
    }
    printf("Case #%d: %.10lf\n",c,ti);

  }

  return 0;
}
