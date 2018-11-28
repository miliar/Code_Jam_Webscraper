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

struct node
{
	int index;
	bool andgate;
	bool changable;
	bool value;
	bool inter;
	bool done;
};

bool gate(bool andgate, bool v1, bool v2)
{
	return andgate ? (v1 && v2) : (v1 || v2);
}

bool calc(int index, vector<node>& nodes)
{
	if (nodes[index-1].done) return nodes[index-1].value;
	nodes[index-1].done = true;
	return nodes[index-1].value = gate(nodes[index-1].andgate, calc(index*2, nodes), calc(index*2+1, nodes));
}

const int INF = 1000000;
int A[10001][2];

int go(int index, bool target, vector<node>& nodes)
{
	int idx = index-1;
	if (!nodes[idx].inter) return target == nodes[idx].value ? 0 : INF;
	int& ret = A[idx][target];
	if (ret != -1) return ret;
	ret = INF;
	if (nodes[idx].value == target) return ret = 0;

	for (int g = 0; g < 2; ++g)
	{
		for (int left = 0; left < 2; ++left)
		{
			for (int right = 0; right < 2; ++right)
			{
				if (g != nodes[idx].andgate && !nodes[idx].changable) continue;
				if (gate(g, left, right) == target)
				{
					int r = go(index*2, left, nodes) + go(index*2+1, right, nodes);
					if (g != nodes[idx].andgate) ++r;
					ret = min(ret, r);
				}
			}
		}
	}
	return ret;
				
}

void solve(vector<node>& nodes, bool target, FILE* fout)
{
	memset(A, -1, sizeof(A));
	calc(1, nodes);
	int res = go(1, target, nodes);
	if (res < INF)
	{
		fprintf(fout, "%d\n", res);
	}
	else
	{
		fprintf(fout, "IMPOSSIBLE\n");
	}
}

int main()
{
	FILE* fin = fopen("A.in", "rt");
	FILE* fout = fopen("A.out", "wt");

	assert(fin && fout);

	int n;
	fscanf(fin, "%d", &n);

	for (int k = 1; k <= n; ++k)
	{
		int m, v;
		fscanf(fin, "%d%d", &m, &v);
		vector<node> input(m);
		for (int i = 0; i < m; ++i)
		{
			if (i < (m-1)/2)
			{
				int g,c;
				fscanf(fin, "%d%d", &g, &c);
				input[i].andgate = g;
				input[i].changable = c;
				input[i].index = i+1;
				input[i].inter = true;
				input[i].done = false;
			}
			else
			{
				int x;
				fscanf(fin, "%d", &x);
				input[i].index = i+1;
				input[i].value = x;
				input[i].inter = false;
				input[i].done = true;
			}
		}

		fprintf(fout, "Case #%d: ", k);
		solve(input, v, fout);
	}

	fclose(fin);
	fclose(fout);
	return 0;
}
