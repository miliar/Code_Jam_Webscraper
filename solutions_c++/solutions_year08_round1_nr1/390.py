#include "stdafx.h"

#include <vector>
#include <algorithm>
#include <cstdio>
#include <iostream>
#include <cassert>
using namespace std;
typedef long long ll;

ll calc1(const vector<int>& v1, const vector<int>& v2, vector<int>& used1, vector<int>& used2)
{
	ll ret = 0;
	int n = v1.size();
	for (int i = 0; i < n; ++i) if (!used1[i] && v1[i] < 0)
	{
		for (int j = n-1; j >= 0; --j) if (!used2[j] && v2[j] > 0)
		{
			used2[j] = 1;
			used1[i] = 1;
			ret += (ll) v1[i] * v2[j];
			break;
		}
	}
	return ret;
}

ll calc2(const vector<int>& v1, const vector<int>& v2, vector<int>& used1, vector<int>& used2)
{
	ll ret = 0;
	int n = v1.size();
	for (int i = 0; i < n; ++i) if (!used1[i] && v1[i] == 0)
	{
		int mx = -1;
		for (int j = n-1; j >= 0; --j) if (!used2[j] && (mx == -1 || abs(v2[j]) > abs(v2[mx])))
		{
			mx = j;
		}
		if (mx != -1)
		{
			used2[mx] = 1;
			used1[i] = 1;
			ret += (ll) v1[i] * v2[mx];
		}
	}
	return ret;
}

ll calc3(const vector<int>& v1, const vector<int>& v2, vector<int>& used1, vector<int>& used2)
{
	ll ret = 0;
	int n = v1.size();
	for (int i = 0; i < n; ++i) if (!used1[i])
	{
		for (int j = n-1; j >= 0; --j) if (!used2[j])
		{
			used1[i] = 1;
			used2[j] = 1;
			ret += (ll) v1[i] * v2[j];
			break;
		}
	}
	return ret;
}

ll solve(FILE* fin)
{
	int n;
	fscanf(fin, "%d", &n);

	vector<int> v1(n), v2(n);

	for (int i = 0; i < n; ++i) fscanf(fin, "%d", &v1[i]);
	for (int i = 0; i < n; ++i) fscanf(fin, "%d", &v2[i]);

	sort(v1.begin(), v1.end());
	sort(v2.begin(), v2.end());

	ll ret = 0;
	vector<int> used1(n), used2(n);

	ret += calc1(v1, v2, used1, used2);
	ret += calc1(v2, v1, used2, used1);
	ret += calc2(v1, v2, used1, used2);
	ret += calc2(v2, v1, used2, used1);
	ret += calc3(v1, v2, used1, used2);

	return ret;
}


int main()
{
	FILE *fin, *fout;
	fin = fopen("A.in", "rt");
	fout = fopen("A.out", "wt");
	assert(fin);
	assert(fout);

	int t;
	fscanf(fin, "%d", &t);
	for (int i = 0; i < t; ++i)
	{
		fprintf(fout, "Case #%d: %lld\n", i+1, solve(fin));
	}

	fclose(fin);
	fclose(fout);
	return 0;
}
