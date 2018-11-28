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

using namespace std;

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

int N;
long long arr[1000];
bool vis[1000] = { 0 };
long long ride[1000] = { 0 };
long long cost[1000] = { 0 };

long long getCycle(queue<int> q, int K, int R) {
	long long r = 0, cur = 0;
	long long sum = 0, prevS = 0;
	memset(vis, 0, sizeof(vis));
	memset(ride, 0, sizeof(ride));
	memset(cost, 0, sizeof(cost));

	while (!q.empty()) {

		if (r == R)
			return prevS;
		cur = q.front();
		if (vis[cur]) {
			long long sol = cost[cur];
			//cout << "cost[cur] = " << sol << endl;
			R -= ride[cur];
			//cout << R << " " << (R / (r - ride[cur])) << " " << (prevS
			//		- cost[cur]) << endl;
			sol += ((R / (r - ride[cur])) * (prevS - cost[cur]));

			R = (R % (r - ride[cur]));
		//	cout << R << endl;
		//	cout << "rep.s = " << sol << endl;

			while (R > 0) {
				sum = 0l;
				while (sum + arr[cur] <= K) {
					sum += arr[cur];
					q.pop();
					q.push(cur);
					cur = q.front();
				//	cout << cur << " " << sum << endl;
				}
				//cout << r << " " << cur << " " << sum << endl;
				R--;
				sol += sum;
				sum = 0l;

			}
			return sol;
		}
		vis[cur] = 1;
		cost[cur] = prevS;
		ride[cur] = r;
		while (sum + arr[cur] <= K) {
			sum += arr[cur];
			q.pop();
			q.push(cur);
			cur = q.front();
		//	cout << cur << " " << sum << endl;
		}
		//cout << r << " " << cur << " " << sum << endl;
		r++;
		prevS += sum;
		sum = 0l;
	}
	return N;
}

int main() {

	freopen("C.in", "rt", stdin);
	freopen("C.out", "wt", stdout);
	int T;
	long long r, k, t = 0, sum;
	cin >> T;
	while (t++ < T) {
		sum = 0;
		queue<int> q;
		cin >> r >> k >> N;
		for (int i = 0; i < N; i++) {
			cin >> arr[i];
			sum += arr[i];
			q.push(i);
		}
		long long sol = r*sum;
		if (sum <= k)
			cout << "Case #" << t << ": " <<sol << endl;
		else
			cout << "Case #" << t << ": " << getCycle(q, k, r) << endl;
	}
	//  system("pause");
	return 0;
}
