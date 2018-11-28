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
	int n; cin >> n;
	vector<vi > v(n,vi(n,0));
	rep(i,n)
	{
		string s; cin >> s;
		rep(j,n)
			v[i][j] = (s[j] == '.' ? 0 : (s[j]=='1' ? 1 : -1));
	}
	
	vector<double> wp(n);
	rep(i,n)
	{
		int w=0,f=0;
		rep(j,n)
		{
			w += (v[i][j]==1);
			f += (v[i][j]==-1);
		}
		wp[i] = w / (0. + w + f);
	}
	
	vector<double> owp(n);
	
	rep(p,n)
	{
		int cnt = 0;
		double sum = 0.0l;
		rep(i,n)
		{
			if (v[i][p] == 0) continue;
			int w=0,f=0;
			rep(j,n)
			{
				if (j==p) continue;
				w += (v[i][j]==1);
				f += (v[i][j]==-1);
			}
			sum += w / (0. + w + f);
			cnt++;
		}
		owp[p] = sum / cnt;
	}
	
	vector<double> oowp(n);
	
	rep(i,n)
	{
		int cnt = 0;
		double sum = 0.0l;
		rep(j,n)
		{
			if (v[i][j] != 0)
			{
				sum += owp[j];
				cnt++;
			}
		}
		oowp[i] = sum / cnt;
	}
	
	cout << "Case #" << cs+1 << ":\n";
	cout.precision(13);
	rep(i,n)
		cout << fixed << 0.25l * wp[i] + 0.50l * owp[i] + 0.25l * oowp[i] << endl;
}

int main()
{
	int t; cin >> t;
	rep(i,t)
		solve(i);

	return 0;
}
