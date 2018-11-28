#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(var,pocz,koniec) for (int var=(pocz); var<=(koniec); ++var)
#define FORD(var,pocz,koniec) for (int var=(pocz); var>=(koniec); --var)
#define FOREACH(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define SWAP(x,y) int t;t=x;x=y;y=t

#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 


char buffer[100];
long long N;

double norm(double q,double s, double d){
	return sqrt(q*q+s*s+d*d);
};
int solve(){
	gets(buffer);
	int T;
	sscanf(buffer, "%d", &T);
	double x,y,z;
	double vx,vy,vz;
	x=0;
	y=0;
	z=0;
	vx=0;
	vy=0;
	vz=0;

	for(int i=0;i<T;i++){
		int a,b,c,d,e,f;
		a=0;b=0;c=0;d=0;e=0;f=0;
		gets(buffer);
		stringstream ss(buffer);
		ss >> a>>b>>c>>d>>e>>f;
		//printf("%d %d %d %d %d %d \n", a,b,c,d,e,f);

		x+=a;
		y+=b;
		z+=c;
		vx+=d;
		vy+=e;
		vz+=f;
		//printf("%f %f %f %f %f %f \n", x ,y ,z,vx,vy,vz);
	};
	
	x/=T;y/=T;z/=T;vx/=T;vy/=T;vz/=T;
	double V=norm(vx,vy,vz);
	if(x*vx+y*vy+z*vz>=0){
		printf("%.8f 0\n", norm(x,y,z));
		return 0;
	};
	//printf("%f %f %f %f %f %f %f\n", x ,y ,z,vx,vy,vz,V);
	if(V==0){
		printf("%.8f 0\n", norm(x,y,z));
		return 0;
	};
	double dis=norm(y*vz-z*vy,x*vz-z*vx,x*vy-y*vx)/V;
	
	printf("%.8f %.8f\n", dis,sqrt(x*x+y*y+z*z-dis*dis)/V);
	return 0;


};





int main(){
	
	freopen("/Users/nicolas/Desktop/input.txt","r",stdin);freopen("/Users/nicolas/Desktop/output.txt","w",stdout);
	gets(buffer);
	sscanf(buffer, "%d", &N);
	REP(i,N){
		printf("Case #%d: ",i+1);
		solve();
	};
	fflush(stdout);
	return 0;
}
