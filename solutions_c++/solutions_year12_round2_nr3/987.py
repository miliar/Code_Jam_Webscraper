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

int n;
int v[501];
map<int, vector<int> > allSums;

int main() {
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		cin >> n;
		for (int i = 0; i < n; ++i) {
			cin >> v[i];
		}
		allSums.clear();
		bool foundSol = 0;
		printf("Case #%i:\n", t + 1);
		for (int i = 0; i <= (1 << n); ++i) {
			int sum = 0;
			for (int j = 0; j < n; ++j) {
				if ((i >> j) & 1)
					sum += v[j];
			}
			if (allSums[sum].size() == 1) {
				int firstSet = allSums[sum][0];
				bool firstS = 0;
				for (int k = 0; k < n; ++k) {
					if ((firstSet >> k) & 1) {
						if (firstS)
							printf(" ");
						printf("%i",v[k]);
						firstS = 1;
					}
				}
				cout << endl;
				firstS = 0;
				for (int k = 0; k < n; ++k) {
					if ((i >> k) & 1) {
						if (firstS)
							printf(" ");

						printf("%i",v[k]);
						firstS = 1;
					}
				}
				cout << endl;
				foundSol = 1;
				i = (1 << n + 1);
			} else
				allSums[sum].push_back(i);
		}
		if (!foundSol)
			printf("Impossible");

	}

	return 0;
}
