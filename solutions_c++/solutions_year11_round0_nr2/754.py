#include <algorithm>
#include <cmath>
#include <cstring>
#include <cctype>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(c) (c).begin(),(c).end()
#define TRACE(x) cerr << "TRACE(" #x ")" << endl;
#define DEBUG(x) cerr << #x << " = " << x << endl;

typedef long long ll;
typedef long double ld;
typedef unsigned long ulong;
typedef unsigned long long ull;

int main() {
	int tnum;
	cin >> tnum;
	REP(ti,tnum) {
		int n;
		vector<pair<pair<char, char>, char> > combine;
		vector<pair<char, char> > oppose;
		cin >> n;
		string s, res;
		REP(i,n) {
			cin >> s;
			combine.push_back(make_pair(make_pair(s[0], s[1]), s[2]));
			combine.push_back(make_pair(make_pair(s[1], s[0]), s[2]));
		}
		cin >> n;
		REP(i,n) {
			cin >> s;
			oppose.push_back(make_pair(s[0], s[1]));
			oppose.push_back(make_pair(s[1], s[0]));
		}
		cin >> n;
		cin >> s;
		FOREACH(it,s) {
			res.push_back(*it);
			if (res.size() > 1) {
				bool success = false;
				FOREACH(c,combine)
					if (c->first.first == res.at(res.size()-1) &&
					c->first.second == res.at(res.size()-2)) {
						res.erase(res.size()-1);
						res.erase(res.size()-1);
						res.push_back(c->second);
						success = true;
						break;
					}
				if (success || res.size() < 2)
					continue;
				success = false;
				for (size_t i1 = 0; i1 < res.size()-1 && !success; ++i1)
					for (size_t i2 = i1+1; i2 < res.size()  && !success; ++i2)
						FOREACH(c,oppose)
							if (c->first == res.at(i1) &&
								c->second == res.at(i2)) {
								res.clear();
								success = true;
								break;
							}				
			}
		}
		printf("Case #%d: [", ti+1);
		if (res.size())
			cout << res[0];
		for (size_t i = 1; i < res.size(); ++i)
			cout << ", " << res[i];
		cout << "]" << endl;
	}
	return 0;
}

