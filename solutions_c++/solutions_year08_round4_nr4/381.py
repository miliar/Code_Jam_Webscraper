#include <algorithm> 
#include <iostream> 
#include <sstream> 
#include <string> 
#include <vector> 
#include <queue> 
#include <set> 
#include <map> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 
using namespace std; 

#define REP(i,n) for(int i=0;i<(n);++i) 
#define FOR(i,a,b) for(int i=(a);i<=(b);++i) 
#define RFOR(i,a,b) for(int i=(a);i>=(b);--i) 
#define FOREACH(it,c) for(typeof((c).begin())it=(c).begin();it!=(c).end();++it) 
#define CLR(x) memset((x),0,sizeof((x))) 
typedef long long LL; 
typedef vector<int> VI; 
typedef vector<string> VS; 

#define INF 2000000000

int k;
string s;

void run() {
	cin >> k >> s;
	int len = s.length();
	int n = len / k;
	vector<int> mm;
	REP(i,k) mm.push_back(i);

	int res = INF;

	do {
		string str = "";
		REP(i,n) {
			string a = s.substr(i * k, k);
			REP(j,k) {
				str += a[mm[j]];
			}
		}
		int last = str[0];
		bool flag = true;
		int t = 1;
		FOR(i,1,str.length()-1) {
			if (str[i] != last) {
				last = str[i];
				++t;
			}
		}
		res = min(res, t);
	} while (next_permutation(mm.begin(), mm.end()));

	cout << res << endl;
}

int main() {
	int kase;
	cin >> kase;
	REP(k,kase) {
		cout << "Case #" << k + 1 << ": ";
		run();
	}
	return 0;
}
