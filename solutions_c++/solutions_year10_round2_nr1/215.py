#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <string>
using namespace std;

#define CLR(a, x) memset(a, x, sizeof(a)) // x = 0|-1, true|false.
#define REP(i, n) for(int i=0; i<(n); i++)
#define FOR(i, a, b) for(int i=(a); i<=(b); i++)
#define FORD(i, b, a) for(int i=(b); i>=(a); i--)
#define FORE(ty, it, data) for(ty::iterator it=data.begin(); it!=data.end(); it++)
#define ALL(x) (x).begin(),(x).end()
#define TWO(X) (1<<(X))
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define EPS 1e-10
const double PI = acos(-1.0);

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef map<string, int> MSI;

template<typename T> string toString(const T &n) { ostringstream O; O<<n; return O.str(); }

////////////////////////////////////////////////////////////////////////////////////////////////////////


vector<string> split(string s, const string& t) {
	vector<string> ret;
	for(int p=s.find(t); p!=s.npos; p=s.find(t)) {
		ret.push_back(s.substr(0, p));
		s = s.substr(p + t.size());
	}
	ret.push_back(s);
	return ret;
}


struct tree{
	string name;
	set<int> child;
};

tree Tree[10000];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d\n", &T);
	FOR(tc, 1, T) {
		printf("Case #%d: ", tc);

		int N, M;
		scanf("%d %d", &N, &M);

		Tree[0].name = "root";
		Tree[0].child.clear();
		int tn(1), mid;

		REP(iter, N+M) {
			if(iter==N)	mid = tn;
			string s;
			cin >> s;
			VS words = split(s.substr(1, s.size()-1), "/");
			int cur(0);
			REP(i, words.size()) {
				string& w = words[i];
				bool found(false);
				FORE(set<int>, it, Tree[cur].child) {
					if(Tree[*it].name==w) {
						found = true;
						cur = *it;
						break;
					}
				}
				if(!found) {
					Tree[tn].name = w;
					Tree[tn].child.clear();
					Tree[cur].child.insert(tn);
					cur = tn;
					tn++;
				}
			}	
			if(tn==10000) {
				printf("no\n");
				return 0;
			}
		}
		printf("%d\n", tn - mid);




		



		fprintf(stderr, "Case #%d Finished!\n", tc);
	}

	return 0;
}