#include <cstdio>
#include <map>
#include <set>
#include <vector>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <fstream>
#include <queue>
#include <list>
#include <cstring>
#define FOR(i,a,n) for(int i=a;i<=n;i++)
#define REP(i,n) for (int i=0;i<n;i++)
#define FORD(i,n,a) for(int i=n;i>=a;i--)
#define PB push_back
#define MP make_pair
#define xx first
#define yy second
#define Min(a,b) a<b ? a:b
#define Max(a,b) a>b ? a:b
#define p2(a) ((a)*(a))
#define ALL(v) v.begin(),v.end()

using namespace std;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef double dd;
    
struct pos{
    dd x,y,z;
    pos(void): x(0.0),y(0.0),z(0.0) {}
};
const dd eps=0.00000001;
const int R=505;
int P[R][3];
int V[R][3];
int n;
pos mass_center(dd t){
    pos res;
    dd x=0.0,y=0.0,z=0.0;
    REP(i,n){
        x+=(dd)P[i][0]+(dd)V[i][0]*t;
        y+=(dd)P[i][1]+(dd)V[i][1]*t;
        z+=(dd)P[i][2]+(dd)V[i][2]*t;
    }
    res.x=x/(dd)n;
    res.y=y/(dd)n;
    res.z=z/(dd)n;
    return res;
}

dd dist(dd x,dd y,dd z){
    return sqrt(x*x+y*y+z*z);
}

void solve(int nr){
    pair<dd,dd> result;
    memset(P,0,sizeof(P));
    memset(V,0,sizeof(V));
    scanf("%d",&n);
    REP(i,n)
        scanf("%d %d %d %d %d %d\n",&P[i][0],&P[i][1],&P[i][2],&V[i][0],&V[i][1],&V[i][2]);
    pos pos0=mass_center(0.0);
    pos pos1=mass_center(1.0);
    dd vx=pos1.x-pos0.x;
    dd vy=pos1.y-pos0.y;
    dd vz=pos1.z-pos0.z;
    dd t;
    if(dist(pos0.x,pos0.y,pos0.z)<eps || (vx*vx+vy*vy+vz*vz<eps))
        t=0.0;
    else
        t= -1.0*(vx*pos0.x+vy*pos0.y+vz*pos0.z)/(vx*vx+vy*vy+vz*vz);
    if(t<0.0){
        result.xx=dist(pos0.x,pos0.y,pos0.z);
        result.yy=0.0;
    }
    else{
        pos posr= mass_center(t);
        result.xx=dist(posr.x,posr.y,posr.z);
        result.yy=t;
    }
    printf("Case #%d: %lf %lf\n",nr,result.xx,result.yy);
}
    
int main(){
    int tests;
    scanf("%d",&tests);
    FOR(i,1,tests)
        solve(i);
    return 0;
}
