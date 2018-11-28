/*

 E-Mail : ahmed.aly.tc@gmail.com

 Just For You :)

 */

#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const int oo = (int) 1e9;
const double PI = 2 * acos(0);
const double eps = 1e-9;

inline int comp(const double &a, const double &b) {
	if (fabs(a - b) < eps)
		return 0;
	return a > b ? 1 : -1;
}

int di[] = { 1, -1, 0, 0, 1, -1, 1, -1 };
int dj[] = { 0, 0, 1, -1, 1, -1, -1, 1 };
int diK[] = { -2, -2, -1, 1, 2, 2, 1, -1 };
int djK[] = { -1, 1, 2, 2, 1, -1, -2, -2 };

int I, J;

inline bool val(const int &i, const int &j) {
	if (i < 0 || j < 0 || i >= I || j >= J)
		return false;
	return true;
}

int N;
int A1,A2,B1,B2;

struct st{
	int A,B;
	bool t;
	st(){}
	st(int aa,int bb,bool tt){
		A=aa;
		B=bb;
		t=tt;
	}
	bool operator <(const st &s)const{
		return mp(mp(A,B),t)<mp(mp(s.A,s.B),s.t);
	}
};
map<st,bool> dp;
bool calc(st s){
	if(s.A<=0 || s.B<=0)
		return s.t;
	map<st,bool>::iterator it=dp.find(s);
	if(it!=dp.end())
		return it->second;
	bool nb=0,na=0;
	if(s.A==s.B)
		return dp[s]=!s.t;
	/*if(s.A-s.B<=0 || s.B-s.A<=0)
		return dp[s]=s.t;*/
	for(int k=1;;k++){
		if(s.A-s.B*k<=0)
			na=1;
		if(s.B-s.A*k<=0)
			nb=1;
		if(na && nb)
			break;
		if(!na){
			if(nb&&0){
				/*if(s.A%s.B==0)
					return dp[s]=!s.t;
				else*/
					return dp[s]=s.t;
			}else{
				if(calc(st(s.A-s.B*k,s.B,!s.t))==s.t)
					return dp[s]=s.t;
			}
		}
		if(!nb){
			if(na&&0){
				/*if(s.B%s.A==0)
					return dp[s]=!s.t;
				else*/
					return dp[s]=s.t;
			}else{
				if(calc(st(s.A,s.B-s.A*k,!s.t))==s.t)
					return dp[s]=s.t;
			}
		}
	}
	return dp[s]=!s.t;
}
ll inter(ll a1,ll a2,ll b1,ll b2){
	a1=max(a1,b1);
	a2=min(a2,b2);
	if(a2<a1)
		return 0;
	return a2-a1+1;
}
#define SMALL
#define LARGE
int main() {
	freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("C-small-attempt3.in","rt",stdin);
	freopen("C-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("C-large.in","rt",stdin);
	freopen("C-large.out","wt",stdout);
#endif
	double sigma=(sqrt(5)-1)/2;
	cin >> N;
	rep2(nn,1,N+1) {
		cin>>A1>>A2>>B1>>B2;
		ll ret=0;
		for(int A=A1;A<=A2;A++){
			ll l=(ll)(floor(sigma*(A)));
			ret+=inter(1,l,B1,B2);
			l+=A+1;
			ret+=inter(l,1000000,B1,B2);
		}
		cout<<"Case #"<<nn<<": "<<ret<<endl;
	}
	return 0;
}
