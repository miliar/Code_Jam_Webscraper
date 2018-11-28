#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <sstream>
#include <iomanip>
using namespace std;
template <class T> void checkmin(T &t,T x){if (x < t) t = x;}
template <class T> void checkmax(T &t,T x){if (x > t) t = x;}
typedef pair <int,int> PII;
typedef pair <double,double> PDD;
#define foreach(it,v) for (__typeof((v).begin()) it = (v).begin();it != (v).end();it++)
const int N = 15555;
int n,m;
int d[N],l[N];
bool F[N];
bool ans;
set < pair <int, int> > all;
set < pair <int, int> > want;

void update(int x, int y) {
	if (all.count(make_pair(x,y))) return;
	all.insert(make_pair(x,y));
	want.insert(make_pair(x,y));
}

long long getH(int st, int cen, int x) {
	long long r = cen - st;
	return r * r - 1LL * (x - cen) * (x - cen);
}

int main(){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int Tc;
	scanf("%d", &Tc);
	for (int ri=0;ri<Tc;ri++) {
		printf("Case #%d: ", ri + 1);
		scanf("%d", &n);
		for (int i=0;i<n;i++) {
			scanf("%d%d",&d[i],&l[i]);
		}
		scanf("%d", &m);
		want.clear();
		all.clear();
		ans = false;
		all.insert(make_pair(0, 0));
		want.insert(make_pair(0, 0));
		while (!want.empty() && !ans) {
			pair <int, int> it = *want.begin();
			want.erase(want.begin());
			int dis = d[it.second] - it.first;
			if (it.first + 2 * dis >= m) {
				ans = true;
				break;
			}
			for (int i=0;i<n;i++) {
				if (d[i] > it.first && d[i] <= it.first + 2 * dis /*&& getH(it.first,d[it.second], d[i]) <= 1LL * l[i] * l[i]*/) {
					update(max(d[it.second], d[i] - l[i]), i);
				}
			}
		}
		if (ans) {
			puts("YES");
		} else {
			puts("NO");
		}
	}
}
