#include <cstdio>
#include <vector>

using namespace std;

struct pt_s
{
	int size;
	int next;
	int earning;

	pt_s() : size(0), next(0), earning(0) { }
	pt_s(int sz) : size(sz), next(0), earning(0) { }
};

vector<pt_s> pt;

int cap;
int runs;
int N;

long long go(int runs)
{
	vector<int> first_run(pt.size(), -1);
	vector<long long> earn(pt.size(), 0LL);
	int i;
	int cur = 0;
	long long ret = 0;
	for (i = 0;i < runs;)
	{
		if (first_run[cur] != -1)
		{
			int cycle_runs = i - first_run[cur];
			int runs_left = runs - i;
			int cycle_times = runs_left / cycle_runs;
			i += cycle_times * cycle_runs;
			long long earn_diff = ret - earn[cur];
			ret += cycle_times * earn_diff;
			break;
		}
		first_run[cur] = i;
		earn[cur] = ret;
		ret += pt[cur].earning;
		cur = pt[cur].next;
		i++;
	}
	for (;i < runs;)
	{
		ret += pt[cur].earning;
		cur = pt[cur].next;
		i++;
	}
	return ret;
}

int main()
{
	int t, ti;
	scanf("%d", &t);
	for (ti = 1;ti <= t;ti++)
	{
		pt.clear();
		scanf("%d %d %d", &runs, &cap, &N);
		int i;
		for (i = 0;i < N;i++)
		{
			int v;
			scanf("%d", &v);
			pt.push_back(pt_s(v));
		}

		for (i = 0;i < N;i++)
		{
			int j;
			int &earn = pt[i].earning;
			for (j = i;;j = (j + 1) % N)
			{
				if (earn != 0 && j == i)
					break;
				int ne = earn + pt[j].size;
				if (ne > cap)
					break;
				earn = ne;
			}
			pt[i].next = j;
		}

		long long ans = go(runs);
		printf("Case #%d: %I64d\n", ti, ans);
		fprintf(stderr, "Case #%d: %I64d\n", ti, ans);
	}
	return 0;
}
