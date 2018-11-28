#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <list>
#include <set>
#include <map>
using namespace std;

#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define CLEAR(a,v) memset((a), (v), sizeof(a))

const double eps = 1e-9;
const int INF = 1000000000;
const long long LLINF = (long long)INF * INF;
const double PI = 2 * acos(.0);

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;

const int DELTA = 1000400;
int v[DELTA*2+10];
struct SS {int p, v;} a[210];

int main() {
	freopen("c-small-attempt1.in","r",stdin);
	freopen("c-small-attempt1.out","w",stdout);
	int T, n, ca, i;
	scanf("%d",&T);
	for (ca = 1 ; ca <= T ; ++ca) {
		scanf("%d",&n);
		CLEAR(v, 0);
		int left, right;
		left = INF;
		right = 0;
		for (i = 0 ; i < n ; i++) {
			scanf("%d%d",&a[i].p,&a[i].v);
			v[a[i].p+DELTA] = a[i].v;
			left <?= a[i].p+DELTA;
			right >?= a[i].p+DELTA;
		}
		int ans = 0;
		while (1) {
			for (i = left ; i <= right ; i++) {
				if (v[i] > 1) break;
			}
			if (i > right) break;
			++ans;
			v[i] -= 2;
			v[i-1]++;
			v[i+1]++;
			if (i-1 < left) left = i -1;
			if (i+1 > right) right = i + 1;
		}
		printf("Case #%d: ",ca);
		printf("%d\n",ans);
	}
	return 0;
}
/*
2
3
-1 2
0 1
1 2
2
-1000 1
2000 1
*/
