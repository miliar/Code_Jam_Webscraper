#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

typedef pair<int,int>		PII;
typedef vector<PII>			VPII;
typedef vector<int>			VI;

int col[16];
int where[16];

int n, m;
VPII edges;
int best;

bool cmp(const PII &a, const PII &b)
{
	return a.second - a.first < b.second - b.first;
}

bool check(int num)
{
	VI poly(n);
	for (int i = 0; i < n; i++)
		poly[i] = i;

	for (int e = 0; e < edges.size(); e++)
	{
		int a = 0, b = 0;
		while (edges[e].first != poly[a])
			a++;
		while (edges[e].second != poly[b])
			b++;

		bool found[16] = {false};
		for (int i = a; i <= b; i++)
			found[col[poly[i]]] = true;
		for (int c = 1; c <= num; c++)
			if (!found[c])
				return false;

		VI next;
		for (int i = 0; i <= a; i++)
			next.push_back(poly[i]);
		for (int i = b; i < poly.size(); i++)
			next.push_back(poly[i]);
		poly = next;

//		for (int i = 0; i < poly.size(); i++)
//			cout << poly[i] << " ";
//		cout << endl;
	}

	bool found[16] = {false};
	for (int i = 0; i < poly.size(); i++)
		found[col[poly[i]]] = true;
	for (int c = 1; c <= num; c++)
		if (!found[c])
			return false;

	return true;
}

void track(int pos, int highest)
{
	if (pos == n)
	{
//		for (int i = 0; i < n; i++)
//			cout << col[i] << " ";
//		cout << endl;
//		cout << ": " << check(highest) << endl;
		if (highest > best && check(highest))
		{
			best = highest;
			for (int i = 0; i < n; i++)
				where[i] = col[i];
		}
		return;
	}
	for (int c = 1; c <= highest + 1; c++)
	{
		col[pos] = c;
		track(pos+1, max(highest, c));
	}
}

int main()
{
	int kases;
	cin >> kases;
	for (int kase = 1; kase <= kases; kase++)
	{
		cin >> n >> m;
		edges.resize(m);

		for (int i = 0; i < m; i++)
			cin >> edges[i].first;
		for (int i = 0; i < m; i++)
			cin >> edges[i].second;
		for (int i = 0; i < m; i++)
		{
			edges[i].first--;
			edges[i].second--;
			if (edges[i].first > edges[i].second)
				swap(edges[i].first, edges[i].second);
		}
		sort(edges.begin(), edges.end(), cmp);
		//reverse(edges.begin(), edges.end());

		best = 0;
		track(0, 0);

		cout << "Case #" << kase << ": " << best << endl << where[0];
		for (int i = 1; i < n; i++)
			cout << " " << where[i];
		cout << endl;
	}
	return 0;
}
