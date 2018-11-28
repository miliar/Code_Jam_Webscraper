#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int r,k,n;
int g[2000];
int f[2000];
int m[2000];
long long s[2000];
long long t[2000];

long long baoli() {
	long long ans = 0;
	int pos = 0;
	for(int i = 0 ; i < r; i++) {
		ans += s[pos];
		pos = m[pos];
	}
	return ans;
}

int main() {
	//freopen("input.txt", "r", stdin);
	freopen("G:\\C-large.in", "r", stdin);
	freopen("G:\\C-large.out", "w", stdout);
	int tt;
	cin >> tt;
	int cas = 0;
	while (tt--) {
		cin >> r >> k >> n;
		cas++;
		cout << "Case #" << cas << ": ";
		memset(f, -1, sizeof(f));
		for(int i = 0; i<n;i++) {
			cin >> g[i];
		}
		for(int i = 0;i<n;i++) {
			long long sum = 0;
			int j = 0;
			for(; j < n; j++) {
				int now = (i + j) % n;
				if(sum + g[now] > k) break;
				sum = sum + g[now];
			}
			m[i] = (i + j) % n;
			s[i] = sum;
		}
		long long ans = 0;
		int pos = 0;
		int left = 0;
		int leftfirst;
		for(int i = 0; i < r; i++) {
			if (f[pos] != -1) {
				int step = i - f[pos];
				int cc = (r - i) / step;
				long long price = t[i-1];
				if(f[pos] > 0) price -= t[f[pos]-1];
				ans += ((long long) cc) * price;
				left = (r - i) % step;
				leftfirst = pos;
				break;
			}
			f[pos] = i;
			ans += s[pos];
			if(i == 0) t[i] = s[pos]; else t[i] = t[i-1] + s[pos];
			pos = m[pos];
		}
		for(int  i = 0; i < left; i++) {
			ans += s[leftfirst];
			leftfirst = m[leftfirst];
		}
		cout << ans << endl;
		//cout << baoli() << endl;
	}
	return 0;
}







