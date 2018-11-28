#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

struct Node
{
	int income;
	int next;
};

const int N = 1050;

Node node[N];
int g[N];
int n, r, k;
bool b[N];
void work(int testcase)
{
	scanf("%d%d%d", &r, &k, &n);
	for (int i = 0; i < n; i++)
		scanf("%d", g+i);

	memset(node, 0, sizeof(node));

	int cnt = 0;
	int last = 0;
	int beg;
	while (++cnt)
	{
		int remain = k;
		int cur = last;
		memset(b, false, sizeof(b));
		while (1)
		{
			if (remain >= g[cur])
			{
				remain -= g[cur];
				b[cur] = true;
				cur = (cur + 1) % n;
				if (b[cur])
					break;
			}
			else
				break;
		}
		node[last].income = k - remain;
		node[last].next = cur;

		if (node[cur].income > 0)
		{
			beg = cur;
			break;
		}
		last = cur;
	}

	long long pre_sum = 0;
	int cur = 0;
	int pre_len = 0;
	while (cur != beg)
	{
		pre_len++;
		pre_sum += node[cur].income;
		cur = node[cur].next;
	}
	long long cir_sum = node[beg].income;
	
	cur = node[beg].next;
	while (cur != beg)
	{
		cir_sum += node[cur].income;
		cur = node[cur].next;
	}
	int cir_len = cnt - pre_len;
	//cout << "beg = " << beg << endl;
	//cout << "pre_sum = " << pre_sum << endl;
	//cout << "pre_len = " << pre_len << endl;
	//cout << endl;
	//cout << "cir_sum = " << cir_sum << endl;
	//cout << "cir_len = " << cir_len << endl;
	//cout << endl;
	//cout << "cnt = " << cnt << endl;
	long long sum = 0;

	if (r <= pre_len)
	{
		for (cur = 0; r > 0; cur = node[cur].next, r--)
			sum += node[cur].income;
	}
	else
	{
		for (cur = 0; cur != beg; cur = node[cur].next, r--)
			sum += node[cur].income;
		int tt = r / cir_len;
		r %= cir_len;
		sum += cir_sum * tt;
		for (cur = beg; r > 0; cur = node[cur].next, r--)
			sum += node[cur].income;
	}
	//cout << "sum = " << sum << endl;
	printf("Case #%d: %lld\n", testcase, sum);
}
int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		work(t);
	}
}

