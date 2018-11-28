#include <iostream>
#include <vector>

using namespace std;

#define ll long long

struct Item
{
	int T;
	int step;
	int endIndex;
	ll sum;
};

int CountItem(vector<Item> &v, int index, const vector<int> &g, int n, int k, int step)
{
	ll csum;
	int i = index;
	for (csum = 0; csum <= k - g[i] && i < index + n; csum += g[i], ++i) {}
	v[index].sum = csum;
	v[index].endIndex = i%n;
	v[index].step = step;

	return v[index].endIndex;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	vector<int> g;
	vector<Item> v;
	int r, n, k, index; ll csum;

	int t;
	cin >> t;
	ll Tsum = 0, sum;

	for (int it = 1; it <= t; ++it)
	{
		cin >> r >> k >> n;
		g.resize(2*n);
		v.resize(n);
		index = 0;
		csum = 0;
		for (int i = 0; i < n; ++i)
		{
			cin >> g[i];
			g[i+n] = g[i];
		}
		for (int i = 0; i < n; ++i)
		{
			v[i].sum = 0;
			v[i].step = -1;
		}
		for (int i = 0; i < n+1; ++i)
		{
			if (v[index].step >= 0)
			{
				v[index].T = i - v[index].step;
				break;
			}
			index = CountItem(v, index, g, n, k, i);
		}

		Tsum = 0; sum = 0;
		for (int i = 0, tindex = index; i < v[index].T; ++i)
		{
			Tsum += v[tindex].sum;
			tindex = v[tindex].endIndex;
		}
		for (int i = 0, tindex = 0; i < v[index].step; ++i)
		{
			sum += v[tindex].sum;
			tindex = v[tindex].endIndex;
		}
		if (r - v[index].step > 0)
			sum += Tsum*((r-v[index].step)/v[index].T);
		for (int i = 0, tindex = index; i < (r-v[index].step)%v[index].T; ++i)
		{
			sum += v[tindex].sum;
			tindex = v[tindex].endIndex;
		}

		cout << "Case #" << it << ": " << sum << endl;

/*		for (int i = 0; i < n; ++i)
			cout << v[i].T << ' ' << v[i].sum << ' ' << v[i].step << ' ' << v[i].endIndex << endl;*/

	}
	return 0;
}