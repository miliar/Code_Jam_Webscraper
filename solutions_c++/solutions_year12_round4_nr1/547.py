#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <climits>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <bitset>
#include <iomanip>
#include <utility>
#include <queue>
#include <map>
#include <set>
using namespace std;

const double EPS = 1e-10;
const double PI = acos(-1.0);

typedef long long LL;

const int MAXN = 10000+5;

int n,d[MAXN],l[MAXN];
int r[MAXN];

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int testn;
	scanf("%d",&testn);
	for (int loop = 1; loop<=testn; ++loop) {
		scanf("%d",&n);
		for (int i = 0; i<n; ++i) {
			scanf("%d%d",&d[i],&l[i]);
			r[i] = d[i];
		}
		scanf("%d",&d[n]);
		r[0] = 0;
		bool good = 0;
		for (int i = 0; i<n; ++i) {
			//cout<<i<<' '<<r[i]<<endl;
			int len = d[i]-r[i];
			int R = d[i]+len;
			if (R>=d[n]) {
				good = 1;
				break;
			}
			for (int j = i+1; j<n && d[j]<=R; ++j) {
				int tmp = d[j]-min(l[j],d[j]-d[i]);
				if (tmp<r[j]) r[j] = tmp;
			}
		}
		printf("Case #%d: ",loop);
		if (good) puts("YES");
		else puts("NO");
	}
	return 0;
}
