#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>
using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define forv(i, v) forn(i, (v).size())
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;
typedef long double ld;

const int INF = int(1e8);

int pos[2];
int len[2];
int ans;

bool move(int who, int place)
{
	int add = max(0, abs(pos[who] - place) - len[who]);
	ans += add + 1;
	len[1-who] += add + 1;
	len[who] = 0;
	pos[who] = place;
}

int main()
{
	//freopen("input.txt", "rt", stdin);
	ios_base::sync_with_stdio(false);
	int tn; cin >> tn;
	forn(it, tn) {
		int n; cin >> n;
		ans = 0;
		pos[0] = pos[1] = 0;
		len[0] = len[1] = 0;
		forn(i, n) {
			char who; cin >> who;
			int pos; cin >> pos;
			move(int(who == 'B'), pos - 1);
		}
		cout << "Case #" << it+1 << ": " << ans << endl;
	}

	return 0;
}
