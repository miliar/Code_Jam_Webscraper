#include <stdio.h>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <memory.h>

using namespace std;
#define MAX 1009

long long dists[MAX];

long long L, C, Time, N;


int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		scanf("%lld%lld%lld%lld", &L, &Time, &N ,&C);
		for (int i = 0; i < C; i++)
			scanf("%lld", &dists[i]);
		long long res = 0;
		int cnt = 0;
		while (cnt < N && !(res <= Time && res + dists[cnt % C] * 2 > Time))
		{
			res += dists[cnt % C] * 2;
			cnt++;
		}
		if (cnt < N)
		{
			vector<long long> v;
			long long res1 = dists[cnt % C] * 2;
			cnt++;
			for (int i = cnt; i < N; i++)
				v.push_back(-dists[i % C]);
			sort(v.begin(), v.end());
			for (int i = 0; i < v.size() && i < L; i++)
				res1 -= v[i];
			for (int i = L; i < v.size(); i++)
				res1 -= v[i] * 2;
			long long res2 = res1;
			if (L > 0)
			{
				cnt--;
				v.clear();
				res2 = (Time - res) / 2 + dists[cnt % C];
				cnt++;
				L--;
				for (int i = cnt; i < N; i++)
					v.push_back(-dists[i % C]);
				sort(v.begin(), v.end());
				for (int i = 0; i < v.size() && i < L; i++)
					res2 -= v[i];
				for (int i = L; i < v.size(); i++)
					res2 -= v[i] * 2;
			}
			

			res += min(res1, res2);
		}
		printf("Case #%d: %lld\n", t+1, res);


	}


	return 0;
}