#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
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
#include <ctime>
using namespace std;

#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FOREACH(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define SZ(x) ((int)(x).size())

typedef pair<int,int> pi; typedef vector<int> vi; typedef vector<string> vs; typedef long long ll;

struct s_train {
	int start, end;
	bool dir;
} train[300];
vector<int> vec[300];
int m1[300], m2[300];
bool v[300];

int readtime() {
	int h, m;
	char c;
	cin >> h >> c >> m;
	return h*60+m;
}

bool match(int x) {
	if (x < 0) return true;
	if (v[x]) return false;
	v[x] = true;
	REP(k, SZ(vec[x])) {
		int y = vec[x][k];
		if (match(m2[y])) {
			m1[x] = y;
			m2[y] = x;
			return true;
		}
	}
	return false;
}

int main() {
	int casos, turnaround;
	int na, nb;
	cin >> casos;
	REP(caso, casos) {
		cin >> turnaround >> na >> nb;
		REP(i, na+nb) {
			train[i].start = readtime();
			train[i].end = readtime();
			train[i].dir = (i >= na);
			//cout << train[i].start << " " << train[i].end << " " << train[i].dir << endl;
		}
		REP(i, na+nb) {
			vec[i].clear();
			REP(j, na+nb) {
				if (train[i].dir != train[j].dir &&
				    train[i].start >= train[j].end + turnaround) {
					vec[i].pb(j);
					//cout << i << " " << j << endl;
				}
			}
		}
		CLEAR(m1, -1); CLEAR(m2, -1);
		REP(i, na+nb) {
			CLEAR(v, false);
			match(i);
		}
		//REP(i, na+nb) cout << m1[i] << endl;
		int sol[2] = {0,0};
		REP(i, na+nb) if (m1[i] < 0) sol[train[i].dir]++;
		cout << "Case #" << caso+1 << ": ";
		cout << sol[0] << " " << sol[1] << endl;
	}
	return 0;
}
