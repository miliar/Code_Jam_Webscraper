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

#define pb push_back
#define all(v) v.begin(),v.end()
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
#define sz 10010

int di[] = { -1, 0, 1, 0 };
int dj[] = { 0, 1, 0, -1 };
/*
 int n;
 int arr[52][52];

 void floyd() {
 for (int k = 0; k < n; ++k) {
 for (int i = 0; i < n; ++i) {
 for (int j = 0; j < n; ++j) {
 arr[i][j] += (arr[i][k] * arr[k][j]);
 }
 }
 }
 }

 int main() {
 freopen("in.txt", "rt", stdin);
 //freopen("out.txt", "wt", stdout);
 int T, m, ci;
 cin >> T;
 for (int t = 0; t < T; ++t) {
 memset(arr, 0, sizeof(arr));
 cin >> n;
 for (int i = 0; i < n; ++i) {
 cin >> m;
 for (int j = 0; j < m; ++j) {
 cin >> ci;
 arr[i][ci - 1]++;
 }
 }
 floyd();
 bool flag = false;

 for (int i = 0; i < n; ++i) {
 for (int j = 0; j < n; ++j) {
 if (arr[i][j] > 1) {
 flag = true;
 i = n;
 break;
 }
 }
 }
 if (!flag)
 printf("Case #%i: No\n", t + 1);
 else
 printf("Case #%i: Yes\n", t + 1);
 }
 return 0;
 }
 */

int n;
int arr[1011][1011];
bool vis[1011];

bool dfs(int cur) {
	if (cur == n)
		return false;
	for (int i = 0; i < n; ++i) {
		if (arr[cur][i]) {
			if (vis[i])
				return true;
			vis[i] = 1;
			if (dfs(i))
				return true;
		}
	}
	return false;
}

int main() {
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int T, m, ci;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		memset(arr, 0, sizeof(arr));
		cin >> n;
		for (int i = 0; i < n; ++i) {
			cin >> m;
			for (int j = 0; j < m; ++j) {
				cin >> ci;
				arr[i][ci - 1]++;
			}
		}

		bool flag = false;
		for (int i = 0; i < n; i++) {
			memset(vis, 0, sizeof(vis));
			vis[i] = 1;
			if (dfs(i))
				flag = true;
		}

		if (!flag)
			printf("Case #%i: No\n", t + 1);
		else
			printf("Case #%i: Yes\n", t + 1);
	}
	return 0;
}
