#include<iostream>
#include<vector>
using namespace std;

const int maxn = 1000000 + 10;
bool p[maxn];
vector<int> a;


void solve()
{
	long long n;
	cin >> n;
	if (n == 1) {
		printf("0\n");
		return;
	}
	int ans = 1;
	for (int i = 0; i < a.size(); i++) {
		if ((long long)a[i] * a[i] > n) break;
		long long v = a[i];
		while (v * a[i] <= n) {
			v *= a[i];
			ans++;
		}
	}	
	printf("%d\n", ans);
	
}

void make_table()
{
	p[1] = true;
	for (int i = 2; i < maxn; i++) {
		if (p[i]) continue;
		a.push_back(i);
		for (int j = i; (long long)j * i < maxn; j++)
			p[j * i] = true;
	}
}

int main()
{	
	make_table();
	//cout << a.size() << endl;
	int t, T;
	
	for (scanf("%d", &T), t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		solve();
	}
}