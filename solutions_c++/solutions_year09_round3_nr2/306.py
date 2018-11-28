#include<iostream>
//#include<fstream>
#include<sstream>
#include<unistd.h>
#include<complex>
#include<valarray>
#include<numeric>
#include<cstdio>
#include<cctype>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<bitset>
#include<utility>
#include<time.h>
using namespace std;

#define NDEBUG
#include<assert.h>
#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define FORD(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,N) for(int I=0;I<(N);I++)
#define VAR(V,init) __typeof(init) V=(init)
#define FOREACH(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
#define RFOREACH(I,C) for(VAR(I,(C).rbegin());I!=(C).rend();I++)
#define ALL(X) (X).begin(),(X).end()
#define PB push_back
#define PF(I,V) V.insert(V.begin(),I)
#define EB(V) V.erase(V.rbegin());
#define EF(V) V.erase(V.begin());
#define MP make_pair
#define MAX(A,B) (((A)>(B))?(A):(B))
#define MIN(A,B) (((A)<(B))?(A):(B))
#define FI first
#define SE second
#define SZ(x) ((int)x.size())
#define CLR(x) memset(x,0,sizeof(x))

const long long INFTY=(long long)(1000000000)*(long long)(1000000000);
const long double EPS=10e-12;

typedef long long ll;
typedef long double ld;
typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef list<int> LI;
typedef stack<int> SI;
typedef queue<int> QI;
typedef priority_queue<int> PQI;
typedef set<int> SETI;
typedef set<string> SETS;
typedef pair<int,int> PII;
typedef vector< PII > VII;
typedef pair<ll,ll> PLL;
typedef vector<string> VS;
typedef vector<vector<string> > VVS;

//numerics
template<class T> inline T ABS(T x){return x<0?-x:x;}
ll nwd(ll a,ll b){return !b?a:nwd(b,a%b);}
ll nwd(ll a,ll b,ll &x,ll &y){if(!a){x=0;y=1;return b;} int d=nwd(b%a,a,y,x);x-=(b/a)*y;return d;}
inline ll nww(ll a,ll b){return a*b/nwd(a,b);}
template<class T> inline T sqr(T a){return a*a;}
inline int isZero(long double x){if(x>=-EPS&&x<=EPS) return 1; else return 0;}

int T;
VI x,y,z,t,vx,vy,vz,vt;

#define LD(X) ((ld)(X))

int main(){
  scanf("%d",&T);
//printf("%d\n",T);
  for(int i=0; i<T; i++){
    int N;
    scanf("%d",&N);
//printf("%d\n",i);
    x.clear();y.clear();z.clear(); vx.clear();vy.clear();vz.clear();
    int p1,p2,p3,p4,p5,p6;
    for(int j=0; j<N; j++) {scanf("%d %d %d %d %d %d",&p1, &p2, &p3,&p4,&p5,&p6);
    x.PB(p1); y.PB(p2); z.PB(p3);vx.PB(p4);vy.PB(p5);vz.PB(p6);}
//    printf("para1 %d: %d %d %d %d %d %d\n",N,p1,p2,p3,p4,p5,p6);
    p1=0;p2=0;p3=0;p4=0;p5=0;p6=0;
//    printf("%d %d %d %d\n",x[0],x[1],x[2],x.size());
    for(int j=0; j<N; j++) {
      p1+=x[j];p2+=y[j];p3+=z[j];p4+=vx[j];p5+=vy[j];p6+=vz[j];
    }
//    printf("para: %d %d %d %d %d %d\n",p1,p2,p3,p4,p5,p6);
    ld tmin;
    if(isZero(p4)&&isZero(p5)&&isZero(p6)) tmin=0; else tmin=-(LD(p1)*LD(p4)+LD(p2)*LD(p5)+LD(p3)*LD(p6))/(sqr(LD(p4))+sqr(LD(p5))+sqr(LD(p6)));
    if(tmin<0) tmin=0;
    ld dmin=sqrtl(sqr((p1+tmin*p4)/LD(N))+sqr((p2+tmin*p5)/LD(N))+sqr((p3+tmin*p6)/LD(N)));
    if(isZero(tmin)) tmin=0; 
    if(isZero(dmin)) dmin=0; 
    printf("Case #%d: %.8f %.8f\n",i+1,(double)dmin,(double) tmin);
  }

	return 0;
}
