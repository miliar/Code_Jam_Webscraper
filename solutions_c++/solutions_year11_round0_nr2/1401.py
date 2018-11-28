#include <vector>
#include <numeric>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <limits>
#include <iomanip>

using namespace std;

#define FOR(i,a,b)		for(int i=(a),_b=(b);i<(_b);++i)
#define FORD(i,a,b)		for(int i=(a),_b=(b);i>(_b);--i)
#define pb			push_back
#define mp			make_pair
#define	all(c)			(c).begin(),(c).end()
#define	tr(c,i)	for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define	present(c,x)		((c).find(x) != (c).end())
#define	cpresent(c,x)		(find(all(c),x) != (c).end())

typedef long long			ll;
typedef unsigned long long	ull;
typedef unsigned char	 	byte;
typedef vector<int>			vi;
typedef pair<int, int>		pii;
typedef pair<ll, ll>		pll;
typedef vector<pii>			vpii;

const int N = 25;

bool op[26][26];
char comb[26][26];

int main(int argc, char *argv[])
{
#if 0
	freopen(argv[1],"r",stdin);
#endif
#if 1
	ifstream cin(argv[1]);
#endif
#if 1
	ofstream cout(argv[2]);
#endif
	int T,n,c,d;
	string s;
	char ch;
	cin >> T;
	FOR(t,1,T+1) {
		cin >> c;
		memset(comb,' ',sizeof(comb));
		FOR(i,0,c) {
			cin >> s;
			comb[s[0]-'A'][s[1]-'A'] = comb[s[1]-'A'][s[0]-'A'] = s[2];
		}
		memset(op,false,sizeof(op));
		cin >> d;
		FOR(i,0,d) {
			cin >> s;
			op[s[0]-'A'][s[1]-'A'] = op[s[1]-'A'][s[0]-'A'] = true;
		}
		cin >> n;
		vector<char> v;
		FOR(i,0,n) {
			cin >> ch;
			if (!v.size()) {
				v.pb(ch);
				continue;
			}
			char x = v.back();
			if (comb[x-'A'][ch-'A'] != ' ') {
				v.pop_back();
				ch = comb[x-'A'][ch-'A'];
			}
			v.pb(ch);
			FOR(j,0,v.size()-1) {
				if (op[ch-'A'][v[j]-'A']) {
					v.clear();
					break;
				}
			}
		}
		cout << "Case #" << t << ": [";
		FOR(i,0,v.size()) {
			if (i)
				cout << ", ";
			cout << v[i];
		}
		cout << "]" << endl;
	}
	return 0;
}
