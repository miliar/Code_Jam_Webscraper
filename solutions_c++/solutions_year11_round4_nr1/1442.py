#define _USE_MATH_DEFINES

#include <stdio.h>
#include <iterator>
#include <memory.h>
#include <iostream>
#include <algorithm>
#include <limits>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <math.h>
#include <sstream>
#include <limits.h>
#include <assert.h>
#include <list>
#include <valarray>
#include <queue>
#include <set>
#include <iomanip>
#include <stdlib.h>

#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define rep(i,x) for(int i=0; i<x; ++i)
#define all(x) x.begin(),x.end()
#define rall(x) x.rbegin(),x.rend()
#define out(x,type) copy(all(x),ostream_iterator<type >(cout," ")); cout << endl
#define tr(type, iter, what) for(type::iterator iter=what.begin(); iter!=what.end(); ++iter)

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;

template<class T1,class T2>ostream& operator<<(ostream& os,const pair<T1,T2>& p){os<<"{"<<p.X<<", "<<p.Y<< "}";return os;}
template<class T>ostream& operator<<(ostream& os,const vector<T>& p)
{os<<"[";int i=0;for(typename vector<T>::const_iterator it=p.begin();it!=p.end();++it){os<<(i==0?"":", ")<<*it;i++;}os<<"]";return os;}
template<class T>ostream& operator<<(ostream& os,const set<T>& p)
{os<<"[";int i=0;for(typename set<T>::const_iterator it=p.begin();it!=p.end();++it){os<<(i==0 ?"":", ")<<*it;i++;}os<<"]";return os;}
template<class K,class V>ostream& operator<<(ostream& os,const map<K,V>& p)
{os<<"[";int i=0;for(typename map<K,V>::const_iterator it=p.begin();it!=p.end();++it){os<<(i==0?"":", ")<< *it;i++;}os<<"]";return os;}
template<class T> string toString(const T& o)
{ stringstream ss; ss<<o; string ret; getline(ss,ret);return ret; }
template<class T>
vector<T> subv(const vector<T>& v, int from, int to)
{ return vector<T>(v.begin()+min(max(0,from),(int)v.size()), v.begin()+min(max(0,to),(int)v.size())); }
pii operator+(const pii& a, const pii& b)
{ return mp(a.X+b.X, a.Y+b.Y); }
pii operator*(const int& a, const pii& b)
{ return mp(a*b.X, a*b.Y); }

void solve(int cs)
{
	ll x,s,r,t,n;
	cin >> x >> s >> r >> t >> n;
	vector<pair<ll,pair<ll,ll> > > v(n);
	rep(i,n)
		cin >> v[i].X >> v[i].Y.X >> v[i].Y.Y;
	
	vector<ll> seg;
	vector<ll> w;
	
	ll c = 0;
	rep(i,n)
	{
		ll st = v[i].X;
		ll end = v[i].Y.X;
		ll wh = v[i].Y.Y;
		
		assert(c<=st);
		
		if (c != st)
		{
			seg.pb(st-c);
			w.pb(s);
		}
		seg.pb(end-st);
		w.pb(wh+s);
		
		c = end;
	}
	
	if (c != x)
	{
		seg.pb(x-c);
		w.pb(s);
	}
	
	double ans = 0.0l;
	rep(i,seg.size())
		ans += (seg[i]*1.0l)/w[i];

	vector<pair<double,int> > a;
	rep(i,seg.size())
		a.pb(mp(w[i],i));
	
	sort(all(a));
	
	double rest = t;
	double add = r-s;
	
	rep(i,a.size())
	{
		int j = a[i].Y;
		double s = seg[j];
		double v = w[j];
		
		double need = s/(v+add);
		if (rest >= need)
		{
			rest -= need;
			ans = ans - s/v + need;
		}
		else
		{
			ans -= rest * add/v;
			rest = 0.0l;
			break;
		}
	}

	assert(ans > 0.0l);
	
	cout.precision(10);
	cout << "Case #" << cs+1 << ": ";
	cout << fixed << ans << endl;
}

int main()
{
	int t; cin >> t;

	rep(i,t)
		solve(i);

	return 0;
}
