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
	freopen("C.in", "rt", stdin);
	freopen("C.out", "wt", stdout);
	int T, N;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		cin >> N;
		vector<int> v(N);
		int XOR = 0, sum = 0;
		for (int i = 0; i < N; ++i) {
			cin >> v[i];
			XOR ^= v[i];
			sum += v[i];
		}
		if (XOR != 0)
			printf("Case #%i: NO\n", t + 1);
		else {
			sort(all(v));
			sum -= v[0];
			printf("Case #%i: %i\n", t + 1, sum);
		}
		/*
		 int maxS = -1;
		 for (int i = 1; i < (1 << N) - 2; ++i) {
		 int rSum1 = 0, rSum2 = 0, sum1 = 0, sum2 = 0;
		 for (int j = 0; j < N; j++) {
		 if ((1 << j) & i)
		 rSum1 += v[j], sum1 ^= v[j];
		 else
		 rSum2 += v[j], sum2 ^= v[j];
		 }
		 if (sum1 == sum2) {
		 maxS = max(maxS, max(rSum1, rSum2));
		 }
		 }
		 if (maxS == -1)
		 printf("Case #%i: NO\n", t + 1);
		 else
		 printf("Case #%i: %i\n", t + 1, maxS);*/

	}
	return 0;
}
