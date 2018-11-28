#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
	FILE *in = fopen("C-large.in", "r");
	FILE *out = fopen("out.txt", "w");
	__int64 ts, tc, i, j;
	__int64 r, k, n, tp, sm, fg[1111];
	vector <__int64> ns, res;
	fscanf(in, "%I64d", &ts); fgetc(in);
	for (tc = 1; tc <= ts; ++tc)
	{
		fscanf(in, "%I64d %I64d %I64d", &r, &k, &n);
		ns.clear(); ns.resize(n);
		res.clear();
		for (i = 0; i <= n; ++i)
		{
			fg[i] = -1;
		}
		for (i = 0; i < n; ++i)
		{
			fscanf(in, "%I64d", &ns[i]);
		}
		for (i = 0; i < n; ++i)
		{
			ns.push_back(ns[i]);
		}
		for (i = 0; ; )
		{
			if (fg[i] != -1)
			{
				res.push_back(i);
				break;
			}
			for (tp = j = 0; j < n; ++j)
			{
				if (tp + ns[i + j] > k)
				{
					break;
				}
				tp += ns[i + j];
			}
			fg[i] = tp;
			res.push_back(i);
			i = (i + j) % n;
		}
		for (i = 0, j = res.size(); res[i] != res[j - 1]; ++i)
		{
			;
		}
		for (tp = 0; i < j - 1; ++i)
		{
			tp += fg[res[i]];
		}
		for (sm = i = 0; res[i] != res[j - 1] && r > i; ++i)
		{
			sm += fg[res[i]];
		}
		r -= i;
		sm += r / (j - i - 1) * tp;
		r = r % (j - i - 1);
		for ( ; r > 0; --r, ++i)
		{
			sm += fg[res[i]];
		}
		fprintf(out, "Case #%I64d: %I64d\n", tc, sm);
	}
	return 0;
}
