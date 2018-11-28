#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <vector>
#define MAX 1000005
using namespace std;

int n;
long long t;
bool b[MAX];
long long a[MAX];
long long x[MAX];
long long ttt[MAX];
struct N{
	long long pos;
	long long dis;
	N(){}
	N(long long a, long long z): pos(a), dis(z){};
};

bool operator< (const N &a, const N &b){
	return a.dis > b.dis;
}
vector<N> v;


long long int func() {
	ttt[0] = 0ll;

	for (int i = 1; i <= n; i++)
		if (b[i]) {
			if (t <= ttt[i-1])
				ttt[i] = ttt[i-1] + (x[i] - x[i-1]);
			else if (x[i] - x[i-1] - (t - ttt[i-1]) / 2 > 0)
				ttt[i] = ttt[i-1] + (t - ttt[i-1]) + (x[i] - x[i-1]) - ((t - ttt[i-1]) / 2);
			else
				ttt[i] = ttt[i-1] + 2 * (x[i] - x[i-1]);
		}
		else
			ttt[i] = ttt[i-1] + 2 * (x[i] - x[i-1]);
	
	return ttt[n];
}

int main() {
	int case_no, c, l, T;
	long long int ans, tmp;

	scanf("%d", &T);
	for (case_no = 1; case_no <= T; case_no++) {
		scanf("%d%lld%d%d", &l, &t, &n, &c);
		for (int i = 0; i < c; i++)
			scanf("%lld", &a[i]);
		x[0] = 0;
		for (int i = 0; i < n; i++)
			x[i+1] = x[i] + a[i%c];

		v.clear();
		if (l >= 1){
			for (int i = 1; i <= n; i++){
				// starting point that can place
				if (x[i] * 2 >= t){
					for (int j = i; j <= n; j++){
						v.push_back(N(j, a[(j-1)%c]));
					}
					break;
				}
			}
		}
		
		sort(v.begin(), v.end());
		memset(b, 0, sizeof b);
		for (int i = 0; i < l; i++){
			b[v[i].pos] = 1;
		}
		ans = func();
		//cout << ans << endl;
		
		v.clear();
		if (l >= 1){
			for (int i = 1; i <= n; i++){
				// starting point that can place
				if (x[i] * 2 >= t){
					for (int j = i+1; j <= n; j++){
						v.push_back(N(j, a[(j-1)%c]));
					}
					break;
				}
			}
		}
		
		sort(v.begin(), v.end());
		memset(b, 0, sizeof b);
		for (int i = 0; i < l; i++){
			b[v[i].pos] = 1;
		}
		ans <?= func();
		//cout << ans << endl;

		printf("Case #%d: %lld\n", case_no, ans);
	}

	return 0;
}
