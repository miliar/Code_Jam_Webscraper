#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>

#define FOR(i,a,b) for(int i=a;i<b;++i)
#define RFOR(i,a,b) for(int i=a;i>=b;--i)
#define REP(i,n) FOR(i,0,n)
#define RREP(i,n) RFOR(i,n-1,0)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define INF (int)1<<30
#define vi vector<int>
#define vs vector<string>
#define pb push_back
#define mkp make_pair
#define ll long long int
#define uli unsigned long long int
#define MAX (int)1e6

using namespace std;

ifstream fin ("D-small-attempt0.in");
#define cin fin
//ofstream fout ("D-small.out");
//#define cout fout

double area(int x1, int y1, double r1, int x2, int y2, double r2) {
		double c=hypot(x1-x2,y1-y2);
		double CBD = 2.0*acos((r2*r2 + c*c - r1*r1)/(2.0*r2*c));
		double CAD = 2.0*acos((r1*r1 + c*c - r2*r2)/(2.0*r1*c));
		double Area = CBD*r2*r2/2.0 - r2*r2*sin(CBD)/2.0+ CAD*r1*r1/2.0 - r1*r1*sin(CAD)/2.0;
		return Area;//return printf("%.3lf\n",Area);
}
int main() {
	int t=0;
	cin>>t;
	REP(T,t) {
		int N,M,Px[100],Qx[100],Py[100],Qy[100];
		cin>>N>>M;
		REP(i,N) cin>>Px[i]>>Py[i];
		REP(i,M) cin>>Qx[i]>>Qy[i];
		cout<<"Case #"<<T+1<<": ";
		REP(i,M) printf("%.7lf ",area(Px[0],Py[0],hypot(Px[0]-Qx[i],Py[0]-Qy[i]),Px[1],Py[1],hypot(Px[1]-Qx[i],Py[1]-Qy[i])));cout<<endl;
	}
	return 0;
}
