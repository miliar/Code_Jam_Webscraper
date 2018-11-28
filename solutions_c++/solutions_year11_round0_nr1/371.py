#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

const int MAXN = 128;

int p[MAXN], q[MAXN];
vector <int> ob[2];

int work()
{
	int n;   char ch, c1;
	scanf("%d%c", &n, &c1);
	ob[0].clear();   ob[1].clear();
	for (int i = 0; i < n; i ++)
	{
		scanf("%c%c%d%c", &ch, &c1, &q[i], &c1);
		if (ch == 'B')	p[i] = 1;
		else p[i] = 0;
		ob[p[i]].push_back(q[i]);
	}
	int ans = 0;
	int v[2], os[2] = {0};
	v[0] = v[1] = 1;
	for (int i = 0; i < n; i ++)
	{
		int ens = abs(q[i] - v[p[i]]) + 1;
		v[p[i]] = q[i];   os[p[i]] ++;

		if (os[1-p[i]] < ob[1-p[i]].size())
		{
			int obj = ob[1-p[i]][os[1-p[i]]];
			if (obj > v[1-p[i]])
			{
				v[1-p[i]] += ens;
				if (v[1-p[i]] > obj)  v[1-p[i]] = obj;
			} else {
				v[1-p[i]] -= ens;
				if (v[1-p[i]] < obj)  v[1-p[i]] = obj;
			}
		}

		ans += ens;
	}
	return ans;
}

int main()
{
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int k = 1; k <= T; k ++)
		printf("Case #%d: %d\n", k, work());
//	fclose(stdin);
//	fclose(stdout);
	return 0;
}