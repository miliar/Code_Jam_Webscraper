#include <iostream>
#include <vector>
#include <utility>
#include <cstdlib>

using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int C;
	cin >> C;

	for ( int c = 1; c <= C; c++)
	{
		int N, K, B, T;
		cin >> N >> K >> B >> T;
		vector<pair<int, int> > v;
		pair<int, int> x;
		for ( int i = 0; i < N; i++)
		{
			cin >> x.first;
			v.push_back(x);
		}
		for ( int i = 0; i < N; i++)
		{
			cin >> v[i].second;
		}

		int ct = 0;
		int swaps = 0;
		int z = v.size() - 1;
		while ( ct < K && z >= 0)
		{
			z = v.size() - 1 - ct;
			while ( z >= 0 && (double)(B - v[z].first) / (double)v[z].second > (double)T)
			{
				z--;
				swaps++;
			} 

			if ( z >= 0)
			{
				pair<int, int> p = v[z];
				for (int j = z + 1; j <= v.size() - ct - 1; j++)
				{
					v[j - 1] = v[j];
				}
				v[v.size() - ct - 1] = p;
				ct++;
			}
		} 
 
		if ( z < 0)
		{
			cout << "Case #" << c << ": " << "IMPOSSIBLE" << endl;
		}
		else
		{
			cout << "Case #" << c << ": " << swaps << endl;
		}
	}
}