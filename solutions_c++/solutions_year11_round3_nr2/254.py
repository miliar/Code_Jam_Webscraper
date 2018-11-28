#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;

vector<pair<int, int> > tmp;
int a[1005];

int cnt(int N, int C, int i)
{
	int cnt = N / C;
	if (i % C <= N % C) cnt ++;
	return cnt;
}

void solve(int cID)
{
	int L, N, C;
	long long t;
	cin >> L >> t >> N >> C;
/*	cout << N << " " << C << endl;
	for (int j = 0; j < N; j ++)
		for (int i = 0; i < C; i ++)
			cout << j << " " << i << " " << cnt(j, C, i) << endl;
*/
	long long ans = 0;
	for (int i = 0; i < C; i ++)
	{
		cin >> a[i];
//		ans += a[i] * cnt(N - 1, C, i) * 2;
	}
	for (int i = 0; i < N; i ++) ans += a[i % C] * 2;
	int k;
	long long s = 0;
	for (k = 0; k < N; k ++)
	{
		s += (long long)(a[k % C] * 2);
		if (s >= t) break;
	}
//	cout << ans << " " << k << endl;
	if (k >= N) {
		cout << "Case #" << cID << ": " << ans << endl;
		return;
	}

	tmp.clear();
	tmp.push_back(make_pair((s - t) / 2, 1));
	for (int i = 0; i < C; i ++)
		tmp.push_back(make_pair(a[i], cnt(N - 1, C, i) - cnt(k, C, i)));

	sort(tmp.rbegin(), tmp.rend());
	for (int i = 0; i < tmp.size(); i ++)
		if (tmp[i].second <= L)
		{
			ans -= (long long)tmp[i].first * (long long)tmp[i].second;
			L -= tmp[i].second;
		}
		else
		{
			ans -= (long long)tmp[i].first * (long long)L;
			L = 0;
			break;
		}
	cout << "Case #" << cID << ": " << ans << endl;
}

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; t ++)
		solve(t);
}
