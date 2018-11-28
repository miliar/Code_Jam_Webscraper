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

vi st,end;

vector<vi> split(vi line, int ind)
{
	if (ind < 0) return vector<vi>(1,line);
	
	int n = line.size();

	int ok = 0;
	int s = st[ind], e = end[ind];
	rep(i,n)
		ok += (line[i] == s || line[i] == e);
	if (ok != 2) return split(line, ind-1);
	
	vi a, b;
	
	int i = 0;
	for(;i<n; ++i) if (line[i]==s) break;
	while(1)
	{
		a.pb(line[i]);
		if (line[i] == e) break;
		i = (i+1)%n;
	}
	
	i = 0;
	for(;i<n; ++i) if (line[i]==e) break;
	while(1)
	{
		b.pb(line[i]);
		if (line[i] == s) break;
		i = (i+1)%n;
	}
	
	//cerr << mp(s,e) << a << b << line << endl;

	vector<vi> ra = split(a,ind-1);
	vector<vi> rb = split(b,ind-1);
	
	rep(i,rb.size()) ra.pb(rb[i]);
	
	return ra;
}

int clr[8];

bool checkColor(vector<vi>& lines, vi& color, int nclr)
{
	int n = lines.size();
	
	rep(i,n)
	{
		int cnt = 0;
		memset(clr,0,sizeof(clr));
		
		rep(j,lines[i].size())
		{
			int v = lines[i][j]-1;
			if (clr[color[v]] == 0)
			{
				clr[color[v]]++;
				cnt++;
			}
		}
		if (cnt != nclr) return false;
	}
	return true;
}

void solve(int cs)
{
	int n, m; cin >> n >> m;
	
	vi line(n);
	rep(i,n) line[i] = i+1;
	
	st.resize(m);
	end.resize(m);
	
	rep(i,m) cin >> st[i];
	rep(i,m) cin >> end[i];
	
	vector<vi> lines = split(line, m-1);
	
	//cerr << lines << endl;
	if (lines.size() != m+1)
	{
		cerr << st << end << endl;
		cerr << n << endl;
		abort();
	}
	
	for(int nclr = n; nclr >= 1; --nclr)
	{
		int nvar = 1;
		rep(j,n) nvar *= nclr;
		vi colors(n+1,0);
		
		rep(p,nvar)
		{
			if (checkColor(lines,colors,nclr))
			{
				cout << "Case #" << cs + 1 << ": " << nclr << endl;
				rep(i,n)
					cout << colors[i]+1 << " ";
				cout << endl;
				return;
			}
			
			colors[0]++;
			rep(i,n)
				if (colors[i] == nclr)
				{
					colors[i] = 0;
					colors[i+1]++;
				}
				else break;
		}
	}
}

int main()
{
	int t; cin >> t;
	rep(i,t)
	{
		cerr << i+1 << " / " << t << endl;
		solve(i);
	}

	return 0;
}
