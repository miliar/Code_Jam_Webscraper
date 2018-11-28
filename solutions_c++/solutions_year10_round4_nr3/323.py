#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <iterator>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

/* Prewritten code begins */
#define PII         pair<int,int>
#define FOR(i,a,b)  for(int i=(a); i<=(b); ++i)
#define REP(i,n)    for(int i=0; i<(n); ++i)
#define MP          make_pair
#define FORE(i,c)   for(VAR(i,(c).begin()); i!=(c).end(); ++i)
#define VAR(i,v)    __typeof(v) i=(v)
#define X           first
#define Y           second
/* Prewritten code ends */

int main() {
	int C, R, x1, x2, y1, y2, res;
	set<PII> old, nw;
	cin >> C;
	FOR(cs,1,C) {
		cin >> R;
		old.clear();
		REP(i,R) {
			cin >> x1 >> y1 >> x2 >> y2;
			FOR(x,x1,x2) FOR(y,y1,y2) old.insert(MP(x,y));
		}
		res = 0;
		while(!old.empty()) {
			nw.clear();
			FORE(i,old) {
				if(old.count(MP(i->X-1,i->Y))||old.count(MP(i->X,i->Y-1))) nw.insert(*i);
				if(old.count(MP(i->X-1,i->Y+1))) nw.insert(MP(i->X,i->Y+1));
				if(old.count(MP(i->X+1,i->Y-1))) nw.insert(MP(i->X+1,i->Y));
			}
			res++;
			old = nw;
		}
		cout << "Case #" << cs << ": " << res << endl;
	}
	return 0;
}
