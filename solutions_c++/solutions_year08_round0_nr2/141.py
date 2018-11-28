#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)
const int inf = 1000000009;
const double eps = 1e-8;
int dx[]={-1,0,1,0};
int dy[]={0,-1,0,1};

struct Event {
	int Time1;
	int Time2;
	int From;
	Event(int time1, int time2, int from) : Time1(time1), Time2(time2), From(from) {}
};
int cc(const Event& A, const Event& B) { 
	return A.Time1 < B.Time1;
}

int i, j, k, m, l, o, t, tt;
int n[2];

int get() {
	string s;
	cin >> s;
	return 600 * (s[0] - '0') + 60 * (s[1] - '0') + 10 * (s[3] - '0') + (s[4] - '0');
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
		
	scanf("%d", &t);
	F1(tt,t) {
		vector<Event> events;
		int T;
		scanf("%d", &T);
		scanf("%d%d", &n[0], &n[1]);
		F0(k,2) F0(i,n[k]) {
			int t1 = get();
			int t2 = get() + T;
			events.push_back(Event(t1, t2, k));
		}
		sort(events.begin(), events.end(), cc);
		multiset<int> S[2];
		int ans[2] = {0, 0};
		F0(k,SZ(events)) {
			Event x = events[k];
			i = x.From;
			if (!S[i].empty() && (*S[i].begin()) <= x.Time1) {
				S[i].erase(S[i].begin());
			} else {
				ans[i]++;
			}
			S[1-i].insert(x.Time2);
		}

		printf("Case #%d: %d %d\n", tt, ans[0], ans[1]);
	}

	return 0;
}
