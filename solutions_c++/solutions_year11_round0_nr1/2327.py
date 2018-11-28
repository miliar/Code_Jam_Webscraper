#include <map>
#include <set>
#include <math.h>
#include <deque>
#include <stack>
#include <queue>
#include <vector>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <stdio.h>

using namespace std;

#include <ext/hash_set>
using namespace __gnu_cxx;

#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,s,m) for(int i=s;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define PI = (2.0 * acos(0.0));
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define OO ((int)1e9)

int dx[] = { 0, -1, 0, 1, -1, -1, 1, 1 };
int dy[] = { -1, 0, 1, 0, 1, -1, -1, 1 };

int main() {

	freopen("A.in", "rt", stdin);
	freopen("A.out", "wt", stdout);
	char c;
	int T, N, b;
	bool r;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		cin >> N;
		vector<pair<bool, int> > v(N);
		for (int i = 0; i < N; ++i) {
			cin >> c >> b;
			r = (c == 'O');
			v[i] = make_pair(r, b);
		}
		long long bO = 1, sO = 0, bB = 1, sB = 0, curTime = 0;
		for (int i = 0; i < v.size(); ++i) {
			if (v[i].first) {

				int move = abs(v[i].second - bO);
				int diffT = curTime - sO;
				//cout << move << " " << diffT << endl;
				if (move <= diffT)
					move = 0;
				else
					move -= diffT;
				//cout << move << " " << diffT << endl;
				//cout << endl;
				curTime += move + 1;
				sO = curTime;
				bO = v[i].second;
			} else {
				int move = abs(v[i].second - bB);
				int diffT = curTime - sB;
				if (move <= diffT)
					move = 0;
				else
					move -= diffT;
				curTime += move + 1;
				sB = curTime;
				bB = v[i].second;
			}
		}
		//printf("Case #%i: %i\n", t + 1, curTime);
		cout << "Case #" << t + 1 << ": " << curTime << endl;
	}

	return 0;
}
