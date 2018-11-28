#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <math.h>
#include <string>
#include <memory.h>
#include <string.h>
using namespace std;

typedef long long LL;

vector<pair<LL, int> > gr;
LL summ, R, k, N, ts;
LL a[1024];
bool has[1024];

void Solve()
{
	memset(has, 0, sizeof(has));
	gr.clear();
	summ = 0;
	cin >> R >> k >> N;
	for(int i = 0; i < N; i++)
	{
		cin >> a[i];
		summ += a[i];
	}
	if(summ <= k)
	{
		cout << (summ * R) << endl;
		return;
	}
	summ = 0;
	int p = 0;
	while(!has[p])
	{
		int tp = p;
		has[p] = 1;
		ts = a[p];
		while(ts + a[(p + 1) % N] <= k)
		{
			p = (p + 1) % N;
			ts += a[p];
		}
		gr.push_back(make_pair(ts, tp));
		summ += ts;
		p = (p + 1) % N;
	}
	LL res = 0;
	if(R <= gr.size())
	{
		for(int i = 0; i < R; i++)
			res += gr[i].first;
	}
	else
	{
		res = summ;
		R -= gr.size();
		int nj = 0;
		while(gr[nj].second != p)
		{
			summ -= gr[nj].first;
			nj++;
		}
		res += summ * (R / (gr.size() - nj));
		R %= gr.size() - nj;
		for(int i = 0; i < R; i++)
			res += gr[i + nj].first;
	}
	cout << res << endl;
}

int main()
{
	freopen("d:\\test.in", "r", stdin);
	freopen("d:\\test.out", "w", stdout);
	int C;
	cin >> C;
	for(int r = 1; r <= C; r++)
	{
		cout << "Case #" << r << ": ";
		Solve();
	}
	return 0;
}
