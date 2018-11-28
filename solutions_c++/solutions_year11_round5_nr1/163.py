#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>


 
using namespace std;
 
const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;
 
#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

double xh[1100],xl[1100],yh[1100],yl[1100];
int L,H,W,TC,G;
double calc(int lo, int hi){
	double res = 0.0;
	FOR(i,1,lo){
		res+=xl[i]*yl[i-1]-yl[i]*xl[i-1];
	}
		res+=xh[hi-1]*yl[lo-1]-yh[hi-1]*xl[lo-1];
	FOR(i,1,hi){
		res+=xh[i-1]*yh[i]-yh[i-1]*xh[i];
	}
		res+=xh[0]*yl[0]-yh[0]*xl[0];
	return -res;
}
double calc(int lo,int hi, double x){
	double txl,txh,tyl,tyh;
	int L = 1,H=1;
	while(x > xl[L]&&L+1<lo)L++;
	while(x > xh[H]&&H+1<hi)H++;
	txl = xl[L], tyl = yl[L], txh= xh[H], tyh = yh[H];
	double mh = (yh[H]-yh[H-1])/(xh[H]-xh[H-1]);
	double ml = (yl[L]-yl[L-1])/(xl[L]-xl[L-1]);
	xl[L]=x; xh[H]=x;
	yl[L]=yl[L-1]+ml*(x-xl[L-1]);
	yh[H]=yh[H-1]+mh*(x-xh[H-1]);
	double res = calc(L+1,H+1);
	xl[L]=txl, yl[L]=tyl, xh[H]=txh, yh[H]=tyh;
	return res;
}
int main(){
	scanf("%d",&TC);
	FOR(tc,1,TC+1){
		scanf("%d%d%d%d",&W,&L,&H,&G);
		FOR(i,0,L)scanf("%lf%lf",xl+i,yl+i);
		FOR(i,0,H)scanf("%lf%lf",xh+i,yh+i);
		printf("Case #%d:\n",tc);
		double A = calc(L,H);
	//	cout << A << endl;
		FOR(i,1,G){
			double AT = (A*i)/G;
	//		cout << AT << endl;
			double lo = 0, hi = W;
			int ST = 50;
			while(ST--){
				double mid = lo+(hi-lo)*0.5;
				double ca = calc(L,H,mid);
	//			cout << mid << " "<< ca << endl;
				if(ca<AT){
					lo = mid;
				} else {
					hi = mid;
				}
			}
			printf("%.9lf\n",lo+(hi-lo)*0.5);
		}
	}
	return 0;
}
