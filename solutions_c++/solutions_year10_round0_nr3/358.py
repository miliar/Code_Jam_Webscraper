#include<cstdio>
#include<iostream>
using namespace std;

int r, k, n;
int a[1000];
pair<long long, int> b[1000][31];

long long work()
{
	scanf("%d%d%d", &k, &r, &n);
	for (int i = 0; i < n; i++)
		scanf("%d", a + i);
	for (int i = 0; i < n; i++) {
		int j = i, k = r;
		do {
			if (a[j] > k)
				break;
			k -= a[j];
			if (++j == n)
				j = 0;
		} while (j != i);
		b[i][0] = make_pair(r - k, j);
	}
		for (int j = 1; j < 31; j++) 
	for (int i = 0; i < n; i++){
			long long s = b[i][j-1].first;
			int t = b[i][j-1].second;
			s += b[t][j-1].first;
			t = b[t][j-1].second;
			b[i][j] = make_pair(s, t);
		}
	long long s = 0;
	int t = 0, j = 0;
	while (k) {
		if (k&1) {
			s += b[t][j].first;
			t = b[t][j].second;
		}
		k /= 2;
		++j;
	}
	return s;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
		cout << "Case #" << i << ": " << work() << endl;
}
