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

const string s[3] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","de kr kd eoya kw aej tysr re ujdr lkgc jv"};
const string t[3] = {"our language is impossible to understand","there are twenty six factorial possibilities","so it is okay if you want to just give up"};

int T, cant;
bool esta[30], esta2[30];
char mapa[30];


int main () {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	cin >> T;
	getchar();
	
	cant = 0;
	memset(esta,false, sizeof(esta));
	memset(esta2,false, sizeof(esta2));
	forn(i,3) forn(j,si(s[i])) if (s[i][j]!= ' '){
		int u = s[i][j]-'a';
		if (!esta[u]) {
			esta[u] = true;
			cant++;	
			mapa[u] = t[i][j];
			esta2[mapa[u]-'a'] = true;
		}	
	}
	mapa['z'-'a'] = 'q';
	mapa['q'-'a'] = 'z';
		
//	cout << cant << endl;
//	forn(i,26) if (!esta[i]) cout << (char)(i+'a') << endl;
//	forn(i,26) if (!esta2[i]) cout << (char)(i+'a') << endl;
	
	forn(rep,T) {
		string a;
		getline(cin,a);
		string b;
		forn(i,si(a)) {
			if (a[i] == ' ') b+= ' ';
			else b+= mapa[a[i]-'a'];	
		}
		cout << "Case #" << rep+1 << ": " << b << endl;
	}


	return 0;
}
