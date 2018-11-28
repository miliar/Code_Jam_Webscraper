#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
using namespace std;
 
typedef long long LL;
typedef vector<int> vi;
typedef vector< pair<int, int> > vii;

#define MP(x,y) make_pair(x, y)

class Data{
	public:
		double b, e, w;
		friend bool operator<(const Data&a, const Data&b);
};
bool operator<(const Data&a, const Data&b) {
	return a.w > b.w;
}

double X, S, R, t;
int n;
Data a[1005];

int main(void) {
    int T, cs, i;
    scanf("%d", &T);
    for(cs=1;cs<=T;cs++) {
		scanf("%lf%lf%lf%lf", &X, &S, &R, &t);
		scanf("%d", &n);
		priority_queue<Data> Q;
		double len = X;
		for(i=0;i<n;i++) {
			scanf("%lf%lf%lf", &a[i].b, &a[i].e, &a[i].w);
			len -= a[i].e - a[i].b;
			Q.push(a[i]);
		}
		Data pp;
		pp.b = 0; 
		pp.e = len;
		pp.w = 0;
		Q.push(pp);
		double ans = 0;
		while (!Q.empty()) {
			Data tmp = Q.top();
			Q.pop();
			double rt = (tmp.e - tmp.b) / (R+tmp.w);
			if (rt <= t) {
				t -= rt;
				ans += rt;
			} else {
				ans += t;
				double Z = tmp.e - tmp.b - t*(R+tmp.w);
				ans += Z / (S + tmp.w);
				t = 0.0;
			}
		}
		printf("Case #%d: %.9lf\n", cs, ans);
        fprintf(stderr, "Case #%d: %.9lf\n", cs, ans);
    }
    return 0;
}

