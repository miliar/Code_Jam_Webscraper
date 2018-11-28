#include "stdafx.h"

#include <vector>
#include <string>
#include <algorithm>
#include <numeric>
#include <functional>
#include <cstdio>
#include <cassert>
#include <cmath>

using namespace std;

char buf[50010];

int solve(const string& s, int a)
{
	vector<int> v(a);
	for (int i = 0; i < a; ++i) v[i] = i;

	int ret = INT_MAX;
	do 
	{
		string ns = s;
		for (int i = 0; i < ns.size(); i += a)
		{
			for (int j = 0; j < a; ++j)
			{
				ns[i+j] = s[i+v[j]];
			}
		}

		int ans = 0;
		for (int j = 0; j < ns.size();)
		{
			int i = j+1;
			while (i < ns.size() && ns[i] == ns[j]) ++i;
			ans++;
			j = i;
		}
		ret = min(ret, ans);
	} while (next_permutation(v.begin(), v.end()));

	return ret;
}

int main()
{
	FILE* fin = fopen("D.in", "rt");
	FILE* fout = fopen("D.out", "wt");

	assert(fin && fout);

	
	int n;
	fscanf(fin, "%d\n", &n);
	for (int k = 1; k <= n; ++k)
	{
		int a;
		fscanf(fin, "%d\n", &a);
		fgets(buf, sizeof(buf), fin);
		buf[strlen(buf)-1] = 0;
		fprintf(fout, "Case #%d: %d\n", k, solve(buf, a));
	}

	fclose(fin);
	fclose(fout);
	return 0;
}
