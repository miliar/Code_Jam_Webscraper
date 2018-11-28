#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<cmath>
#include<string>
#include<cstring>
#include<cctype>
#include<algorithm>
#include<vector>
#include<bitset>
#include<queue>
#include<stack>
#include<utility>
#include<list>
#include<set>
#include<map>

using namespace std;

#define eps 1e-10
#define INF INT_MAX
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).end(),(v).begin()
#define mp make_pair
#define pb push_back

#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define REPSZ(i,v) REP(i,SZ(v))
#define CLEAR(t) memset((t),0,sizeof(t))

typedef pair < int, int > pii;
typedef long long LL;

double dist(int x1,int y1,int x2,int y2){
   return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

int N;
bool go(vector<int> x,vector<int> y,vector<int> r,double rad){

if(N==1) return r[0]<=rad;
if(N==2) return max(r[0],r[1])<=rad;
else{
   double d1=dist(x[0],y[0],x[1],y[1])+r[0]+r[1];
   double d2=dist(x[1],y[1],x[2],y[2])+r[1]+r[2];
   double d3=dist(x[0],y[0],x[2],y[2])+r[0]+r[2];

   if( d1<=2*rad|| d2<=2*rad|| d3<=2*rad) return true;
   return false;
}
}


void run1(int caso){
    cin>>N;
     vector<int> x(N),y(N),r(N);
     int val = -INF;
     REP(i,N){
        cin>>x[i]>>y[i]>>r[i];
        val = max(val,r[i]);
     }

     double left=val;
     double rig=2000;

     while(fabs(rig-left)>eps){
      double mid=(left+rig)/2.0;

      if(go(x,y,r,mid)) rig=mid;

      else left=mid;
     }

    double sol = (left+rig)/2.0;


	cout << "Case #"<<caso<<": "<< sol<<endl;
}
int main()
{
	int T; scanf("%d",&T);
	FORE(i,1,T) run1(i);
	return 0;
}
