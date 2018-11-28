#include <iomanip>
#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <complex>
#include <cassert>
#include <bitset>
using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define dforall(i, c) for(decl(i, c.rbegin()); i!=c.rend(); ++i)
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define D(a) cout << #a << "=" << a << endl;
#define pb push_back
#define mp make_pair

typedef long long int tint;

#define MAXN 2500

int t,n,m, u[MAXN], v[MAXN], p[MAXN], cantcomp;

vector<int> comp[10];

bool g[MAXN][MAXN], f[MAXN][MAXN];

int cantcolor(vector<int> v, int c) {
	bool color[5];
	memset(color,false,sizeof(color));
	forn(i,si(v)) color[p[v[i]]] = true;
	int cantcolor = 0;
	forn(i,c) if (color[i]) cantcolor++;
	if (cantcolor == c)	 return true;
	return false;
}

bool valid(int c) {
	vector<int> v;
	forn(i,n) v.pb(i);
	if (!cantcolor(v,c)) return false;	
	forn(i,cantcomp) if (!cantcolor(comp[i],c)) return false;
	return true;
}

void llenarp(int mask, int c) {
	forn(i,n) {
		p[i] = mask%c;
		mask/=c;	
	}	
}

bool intersect(int a, int b, int x, int y) {
	if (a>b) swap(a,b); if (x>y) swap(x,y);
	// a x b y
	if (a<x && x<b && y>b) return true;
	//x a y b
	if (x<a && a<y && y<b) return true;
	
	return false;	
}

bool testcomp(int mask) {
	forn(i,n) forsn(j,i+1,n) if ( (mask&(1<<i)) && (mask&(1<<j)) ) {
		forn(k,m) if (intersect(i,j,u[k],v[k])) return false;
	}
	return true;
}

void buildcomp() {
	vector<int> comps, realcomps;
	forsn(mask,1,(1<<n)) {
		if (testcomp(mask))	{
			comps.pb(mask);
		}
	}	
	forn(i,si(comps)) {
		bool buena = true;
		forn(j,si(comps)) if (j!=i) {
			if ( (comps[i]&comps[j]) == comps[i] ) {
				buena = false;
				break;
			}
		}
		if (buena) realcomps.pb(comps[i]);
	}
	forn(i,si(realcomps)) {
		vector<int> v;
		forn(j,n) if (realcomps[i]&(1<<j)) v.pb(j);
		comp[cantcomp++] = v;
	}
}

void print() {
	forn(i,n-1) cout << p[i]+1 << " "; cout<< p[n-1]+1 << endl;	
}

void init() {
	memset(g,false,sizeof(g));	
	memset(f,true,sizeof(f));
	forn(i,10) comp[i].clear();
	cantcomp = 0;
}

int main () {
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	
	cin >> t;
	forn(caso,t) {
		cin >> n >> m;	
		init();
		forn(i,m) { cin >> u[i]; u[i]--;}
		forn(i,m) { cin >> v[i]; v[i]--;}		
		forn(i,m) {
			g[u[i]][v[i]] = g[v[i]][u[i]] = true;	
		}
		cout << "Case #" << caso+1 << ": ";
		
		if (n==8 && m==1 && abs(u[0]-v[0]) == 4) {
			cout << 5 << endl; 
			for(int i = u[0]; i< u[0]+8; i++) {
				int j = (i-u[0]+8)%8;
				p[i%8] = (j>4)?(8-j):j;	
			}
			print();
		} else {
			bool found = false;
			
			buildcomp();
			
		/*	cout << "cantcomp " << cantcomp << endl;
			forn(i,cantcomp) {
				forn(j, si(comp[i])) cout << comp[i][j] << " "; cout << endl;	
			}
			cout << endl;*/
			
			for(int c = 4; c>=3; c--) {
				int pot = 1; forn(i,n) pot*=c;
				forn(mask,pot) {
					llenarp(mask,c);
					if (valid(c)) {
						found = true;
						cout << c << endl;
						print();
						break;	
					}
				}
				if (found) break;
			}	
			
			if (!found) {
				forn(i,n) p[i] = i%2;
				cout << 2 << endl;
				print();	
			}
		}
		
	}
	return 0;
}
