/*
 * Author: rush
 * Created Time:  2010年05月08日 星期六 09时54分34秒
 * File Name: icpc/GCJ/C.cpp
 */
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

typedef long long LL;

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	// ! long long
	int T, R, k, N;
	int g[1005];
	int head[1005];
	LL once[1005];
	int roller[1005], lr;
	LL sum[1005];

	cin >> T;
	for (int id = 1; id <= T; ++id)
	{
		cin >> R >> k >> N;
		queue<int> q;
		for (int i = 0; i < N; ++i)
		{
			cin >> g[i];
			q.push(i);
		}
		for (int i = 1; i <= N + 1; ++i)
		{
			head[i] = q.front();
			once[i] = 0;
			lr = 0;
			while (!q.empty() && once[i] + g[q.front()] <= k)
			{
				once[i] += g[q.front()];
				roller[lr++] = q.front();
				q.pop();
			}
			for (int j = 0; j < lr; ++j)
				q.push(roller[j]);
		}
		sum[0] = 0, sum[1] = once[1];
		for (int i = 2; i <= N + 1; ++i)
			sum[i] = sum[i - 1] + once[i];

		int off, cycle;
		LL cycle_sum;
		for (int i = 1; i <= N + 1; ++i)
		{
			int j = i + 1;
			while (j <= N + 1 && head[j] != head[i])
				++j;
			if (j <= N + 1)
			{
				off = i;
				cycle = j - i;
				cycle_sum = sum[j] - sum[i];
				break;
			}
		}
		int d = (R - off) / cycle;
		int m = (R - off) % cycle + off;
		LL ans;
		if (R <= off - 1)
			ans = sum[R];
		else
			ans = sum[off - 1] + d * cycle_sum + sum[m] - sum[off - 1];
		cout << "Case #" << id << ": " << ans << endl;
	}
    return 0;
}
