/*
 * C.cpp
 * Another buggy code by mostafa_saad
 *
 *  Created on: Sep 26, 2009
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
#include<stdio.h>
using namespace std;

#define all(v)				((v).begin()), ((v).end())
#define sz(v)				((int)((v).size()))
#define clr(v, d)			memset(v, d, sizeof(v))
#define repi(i, j, n) 		for(int i=(j);i<(int)(n);++i)
#define repd(i, j, n) 		for(int i=(j);i>=(int)(n);--i)
#define repa(v)				repi(i, 0, sz(v)) repi(j, 0, sz(v[i]))
#define rep(i, v)			repi(i, 0, sz(v))
#define lp(i, cnt)			repi(i, 0, cnt)
#define lpi(i, s, cnt)		repi(i, s, cnt)
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

typedef complex<double> point;
#define X real()
#define Y imag()
#define angle(a)                (atan2((a).imag(), (a).real()))
#define vec(a,b)                ((b)-(a))
#define same(p1,p2)             (dp(vec(p1,p2),vec(p1,p2)) < EPS)
#define dp(a,b)                 ( (conj(a)*(b)).real() )	// a*b cos(T), if zero -> prep
#define cp(a,b)                 ( (conj(a)*(b)).imag() )	// a*b sin(T), if zero -> parllel
#define length(a)               (hypot((a).imag(), (a).real()))
#define normalize(a)            (a)/length(a)
#define polar(r,ang)            ((r)*exp(point(0,ang)))
#define rotateO(p,ang)          ((p)*exp(point(0,ang)))
#define rotateA(p,angle,about)  (rotateO(vec(about,p),ang)+about)



int ccw( point p0, point p1, point p2 ) {
	point v1(p1-p0), v2(p2-p0);
	if ( cp(v1, v2) > +EPS)				return +1;
	if ( cp(v1, v2) < -EPS)				return -1;
	if (v1.X*v2.X < -EPS || v1.Y*v2.Y < -EPS)
		return -1;
	if ( norm(v1) < norm(v2)-EPS )	return +1;
	return  0;
}


// Does segments p1p2 & p3p4 intersect
bool intersect(point p1, point p2, point p3, point p4) {

	if(p1 == p3 || p1 == p4)	return true;
	if(p2 == p3 || p2 == p4)	return true;

	return  ccw(p1, p2, p3) * ccw(p1, p2, p4) <= 0  &&
			ccw(p3, p4, p1) * ccw(p3, p4, p2) <= 0;
}

const int MAX = 17;
bool can[MAX][MAX];
bool valid[1<<MAX];

int memo[1<<MAX];
int n, k;

vector< vector<point> > lst;

void print(point a)
{
	cout<<"("<<a.X<<", "<<a.Y<<")  ";
}

bool doNotInter(int a, int b) {
	lp(i, sz(lst[a])-1) {
		lp(j, sz(lst[b])-1)
		{
			bool ans = intersect(lst[a][i], lst[a][i+1], lst[b][j], lst[b][j+1]);

			if(ans)
				return false;
		}
	}
	/*

	lp(i, sz(lst[a])-1) {
		lp(j, sz(lst[b])-1)
		{
			bool ans = intersect(lst[a][i], lst[a][i+1], lst[b][j], lst[b][j+1]);


			if(ans == false) {

				print(lst[a][i]);	print(lst[a][i+1]);
				print(lst[b][j]);	print(lst[b][j+1]);
				cout<<ans<<"\n";
			}
		}
	}
	*/

	return true;
}






ll setBit(ll num, ll idx, ll value = 1) {
	return (value) ? (num |(1LL<<idx) ) : (num &~(1LL<<idx));
}

ll getBit(ll num, ll idx) {
  return ((num >> idx) & 1LL) == 1;
}

int go(int mask)
{
	if(mask == 0)	return 0;

	int &ret = memo[mask];
	if(ret != -1)	return ret;

	ret = OO;
	for(int subMask = mask ; subMask ; subMask = (subMask - 1) & mask) {// control from loop start/stoping condition
		if(valid[subMask]) {
			ret = min(ret, 1+go(~subMask&mask) );
		}
		if(!subMask) 	break;
	}

	return ret;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("c.in", "rt", stdin);
	freopen("c.txt", "wt", stdout);
#endif

	int cases;
	cin>>cases;

	lp(cc, cases)
	{
		clr(can, 0);
		clr(valid, 0);
		clr(memo, -1);
		lst.clear();

		cin>>n>>k;


		lp(i, n) {
			vector<point> v;
			lp(j, k) {
				int f;
				cin>>f;
				v.push_back( point(j+1, f));
			}
			lst.push_back(v);
		}

		lp(i, n) lp(j, n) if(i != j)
		{
			can[i][j] = doNotInter(i, j);
			//if(can[i][j])				cout<<i<<" "<<j<<"\n";
		}


		lp(i, 1<<n) {
			int pass = 1;
			lp(j, n) if(getBit(i, j))
			{
				lpi(k, j+1, n) if(getBit(i, k) && !can[j][k]){
					pass = 0;
					goto end;
				}
			}
			end:;
			valid[i] = pass;
		}
		valid[0] = 0;

		int mn = go( (1<<n)-1 );

		printf("Case #%d: %d\n", cc+1, mn);


	}



	return 0;
}
