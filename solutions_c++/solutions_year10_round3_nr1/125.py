/*
 * A.cpp
 * Another buggy code by mostafa_saad
 *
 *  Created on: May 22, 2010
 */


#include<set>
#include<map>
#include<list>
#include<iomanip>
#include<cmath>
#include<string>
#include<vector>
#include<queue>
#include<stack>
#include<complex>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<numeric>
#include<utility>
#include <functional>
#include<stdio.h>
#include<assert.h>
#include<memory.h>
using namespace std;

#define all(v)				((v).begin()), ((v).end())
#define sz(v)				((int)((v).size()))
#define clr(v, d)			memset(v, d, sizeof(v))
#define rep(i, v)		for(int i=0;i<sz(v);++i)
#define lp(i, n)		for(int i=0;i<(int)(n);++i)
#define lpi(i, j, n)	for(int i=(j);i<(int)(n);++i)
#define lpd(i, j, n)	for(int i=(j);i>=(int)(n);--i)
#define repa(v)				lpi(i, 0, sz(v)) lpi(j, 0, sz(v[i]))
#define P(x)				cout<<#x<<" = { "<<x<<" }\n"
#define pb					push_back
#define MP					make_pair

typedef vector<int>       vi;
typedef vector<double>    vd;
typedef vector< vi >      vvi;
typedef vector< vd >      vvd;
typedef vector<string>    vs;
typedef long long         ll;
typedef long double   	  ld;

const int OO = (int)1e8;	//Small -> WRONG, Large -> OVERFLOW

const double PI  = acos(-1.0);
const double EPS = (1e-7);

int dcmp(double x, double y) {	return fabs(x-y) <= EPS ? 0 : x < y ? -1 : 1;	}
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)
typedef complex<double> point;
typedef pair<point,point> segment;
bool lineInter(const point &A,const point &B,const point &P,const point &Q, point &R,bool isSegA=false,bool isSegB=false)
{
	double d1 = cross(P-A,B-A);
	double d2 = cross(Q-A,B-A);
	if(fabs(d1-d2) < EPS) return false;
	R = (d1*Q - d2*P) / (d1-d2);
	if(isSegA && dcmp(hypot(A.X-B.X,A.Y-B.Y),hypot(A.X-R.X,A.Y-R.Y)+hypot(B.X-R.X,B.Y-R.Y))!=0)
	   return false;
	if(isSegB && dcmp(hypot(P.X-Q.X,P.Y-Q.Y),hypot(P.X-R.X,P.Y-R.Y)+hypot(Q.X-R.X,Q.Y-R.Y))!=0)
	   return false;
	return true;
}
vector<pair<int,int> > v;
int main()
{
#ifndef ONLINE_JUDGE
	freopen("a.txt", "rt", stdin);
    freopen("b.txt", "wt", stdout);
#endif
	int cases;
	cin>>cases;

	lp(cc, cases) {
		int n,a,b;
		cin>>n;
		v.clear();
		lp(i,n){
			cin>>a>>b;
			v.pb(MP(a,b));
		}
		int ret=0;
		point r;
		lp(i,n)
			lpi(j,i+1,n)
				if(lineInter(point(0,v[i].first),point(100,v[i].second),point(0,v[j].first),point(100,v[j].second),r,1,1))
					ret++;
		printf("Case #%d: %d\n",cc+1,ret);
	}

	return 0;
}
