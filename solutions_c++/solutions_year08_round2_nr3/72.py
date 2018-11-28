#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef long long LL;

const int MAX=6000;
int idx[MAX];
int pos[MAX];
int val[MAX];

int main() {
	int T;
	cin >> T;
	for (int z=1;z<=T;++z) {
		int K;
		cin >> K;
		int n;
		cin >> n;
		for (int i=0;i<n;++i) cin >> idx[i];
		queue<int> q;
		for (int i=0;i<K;++i) q.push(i+1);
		int at = 1;
		for (int i=1;i<=K;++i) {
			for (int j=0;j<i-1;++j) {
				int x = q.front(); q.pop();
				q.push(x);
			}
			int t = q.front(); q.pop();
			val[t] = i;
			pos[i] = t;
			//printf("POS[%d]: %d\n", i, pos[i]);
		}
		printf("Case #%d:", z);
		for (int i=0;i<n;++i) printf(" %d", val[idx[i]]);
		printf("\n");
	}
}
