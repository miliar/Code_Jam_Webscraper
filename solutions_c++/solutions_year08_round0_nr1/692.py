#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <sstream>
#include <fstream>
#include <bitset>
using namespace std;
#define forn(i,n) for(int i=0;i<int(n);++i)
#define forsn(i,s,n) for(int i=s;i<int(n);++i)
#define forall(i,c) for(typeof(c.begin()) i=c.begin();i!=c.end();++i)
typedef long long tint;
typedef pair<int,int> pint;

int main() {
	int ttt; cin >> ttt;
	int s,q;
	forn(tt,ttt) {
		cout << "Case #" << tt+1 << ": ";
		cin >> s;
		vector<string> e(s);
		getline(cin, e[0]);
		forn(i,s) getline(cin, e[i]);
		set<string> alle;
		forn(i,s) alle.insert(e[i]);
		cin >> q;
		string t;
		getline(cin, t);
		set<string> used;
		int res = 0;
		forn(i,q) {
			getline(cin, t);
			used.insert(t);
			if (used == alle) {
				res++;
				used.clear();
				used.insert(t);
			}
		}
		cout << res << endl;
	}
	return 0;
}
