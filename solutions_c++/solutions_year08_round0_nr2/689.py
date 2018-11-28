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

int readTime() {
	int a,b;
	scanf("%d:%d",&a,&b);
	return b+a*60;
}

typedef pair<pint, bool> trip;
#define dep first.first 
#define arr first.second
#define a2b second

int main() {
	int ttt; cin >> ttt;
	forn(tt,ttt) {
		cout << "Case #" << tt+1 << ": ";
		int nab,nba,t; cin >> t >> nab >> nba;
		vector<trip> trips(nab+nba);
		forn(i,nab+nba) {
			trips[i].dep = readTime();
			trips[i].arr = readTime();
			trips[i].a2b = (i<nab);
		}
		sort(trips.begin(), trips.end());
		multiset<int> ta,tb;
		int resa = 0, resb = 0;
		forn(i,nab+nba) {
			trip tr = trips[i];
			multiset<int>* pts = (tr.a2b?&ta:&tb);
			multiset<int>& ts = *pts;
			multiset<int>* pots = (!tr.a2b?&ta:&tb);
			multiset<int>& ots = *pots;
			if (ts.empty() || *ts.begin() > tr.dep) {
				if (tr.a2b) resa++; else resb++;
			} else {
				ts.erase(ts.begin());
			}
			ots.insert(tr.arr+t);
		}
		cout << resa << " " << resb << endl;
	}
	return 0;
}
