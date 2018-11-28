#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define eps 1e-9
#define FOR(x, s, e) for(int x = (s); x < (e); ++x)
#define FORc(x, s, e, c) for(int x = (s); x < (e) && (c); ++x)
#define STEP(x, s, e, d) for(int x = (s); x < (e); x+=(d))
#define ROF(x, s, e) for(int x = (s); x >= (e); --x)
#define ROFc(x, s, e, c) for(int x = (s); x >= (e) && (c); --x)
#define vb vector<bool>
#define vi vector<int>
#define vii vector<pair<int, int> >
#define LL long long
#define pii pair<int, int>
#define vs vector<string>
#define pb push_back
#define mp make_pair
#define ALL(X) X.begin(), X.end()
#define countbit(X) __builtin_popcount(X)
#define gcd(x, y) __gcd(x, y)
#define x first
#define y second

using namespace std;

int main(int argc, char **argv){
	int T;
	cin >> T;
	FOR(Ca, 1, T+1){
		printf("Case #%d: ", Ca);
		int C, D, N;
		cin >> C;
		char ch[100][100];
		bool isclear[100][100];
		memset(ch, 0, sizeof(ch));
		memset(isclear, 0, sizeof(isclear));
		FOR(i, 0, C){
			string s;
			cin >> s;
			int x = s[0] - 'A', y = s[1] - 'A', z = s[2];
			ch[x][y] = ch[y][x] = z;
		}
		cin >> D;
		FOR(i, 0, D){
			string s;
			cin >> s;
			int x = s[0] - 'A', y = s[1] - 'A';
			isclear[x][y] = isclear[y][x] = 1;
		}
		cin >> N;
		string line;
		cin >> line;
		int f[100];
		memset(f, 0, sizeof(f));
		vector<char> res;
		FOR(i, 0, N){
			res.pb(line[i]);
			f[line[i]-'A']++;
			int added=0;
			if (res.size() > 1){
				int L = res.size();
				if (ch[res[L-1]-'A'][res[L-2]-'A']){
					char c = ch[res[L-1]-'A'][res[L-2]-'A'];
					f[res[L-1]-'A']--;
					f[res[L-2]-'A']--;
					res.pop_back(), res.pop_back(), res.pb(c);
					f[c-'A']++;
					added = 1;
				}
			}
			bool ok = !added;
			FORc(j, 0, 26, ok) FORc(k, 0, 26, ok) if (isclear[j][k]){
				if (f[j] && f[k] && j != k){
					memset(f, 0, sizeof(f));
					res.clear();
					ok = 0;
				}else if (j == k && f[j] > 1){
					memset(f, 0, sizeof(f));
					res.clear();
					ok = 0;
				}
			}
			//if (added && !ok) puts("!");
		}
		printf("[");
		FOR(i, 0, res.size()) printf("%c%s", res[i], (i+1==res.size())?"]\n":", ");
		if (!res.size()) puts("]");
	}
	return 0;
}
