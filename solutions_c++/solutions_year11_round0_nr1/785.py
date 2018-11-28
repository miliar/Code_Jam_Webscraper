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
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<tint> vt;
typedef vector<vt> vvt;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

#define MAX 512

int t, v[MAX], n;
int posO, posB, pos, nextO, nextB, tiempo;
bool aprete;


int setnext(char c) {
	if (pos>=n) return -1;
	if (c == 'O') {
		int i = pos;
		while(i<n) {
			if (v[i]<100) return v[i];
			i++;
		}
		return -1;	
	} else {
		int i = pos;
		while(i<n) {
			if (v[i]>=100) return v[i]-100;	
			i++;
		}
		return -1;
	}
}

void move(char c) {
	if (c == 'O') {
		if (posO == v[pos])	{
			pos++;
			aprete = true;
			nextO = setnext('O');	
		} else {
			if (nextO!=-1 && nextO!=posO) {
				if (posO<nextO)	posO++;
				else posO--;
			}	
		}
	} else {
		if (!aprete && posB == v[pos]-100) {
			pos++;
			nextB = setnext('B');	
		} else {
			if (nextB!=-1 && nextB!=posB) {
				if (posB<nextB)	posB++;
				else posB--;
			}	
		}		
	}	
}


int main () {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	cin >> t;
	forn(caso,t) {
		cin >> n;
		forn(i,n) {
			char c; int tmp;
			cin >> c >> tmp;
			if (c=='O')	v[i] = tmp-1;
			else v[i] = tmp+100-1;
		}
		
		posO = 0, posB = 0, pos = 0, tiempo = 0;
		nextO = setnext('O');
		nextB = setnext('B');
		
		while(pos<n) {
			tiempo++;
			aprete = false;
			move('O');
			move('B');
		}
		cout << "Case #" << caso+1 << ": " << tiempo << endl;
	}
	
	
	return 0;
}
