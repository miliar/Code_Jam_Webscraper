#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int crosses(pair<int,int> fst, pair<int,int> snd)
{
	return ( fst.first < snd.first )!=(fst.second < snd.second);
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	vector< pair<int,int> > wires;

	int t;
	scanf("%d", &t);
	for(int it=1;it<=t;it++)
	{
		int n;
		scanf("%d", &n);
		wires.resize(n);
		for(int i=0;i<n;i++)
		{
			scanf("%d%d", &wires[i].first, &wires[i].second);
		}
		int xs = 0;
		for(int i=0;i<n;i++)
		{
			for(int j=i+1;j<n;j++)
			{
				xs += crosses(wires[i], wires[j]);
			}
		}
		printf("Case #%d: %d\n", it, xs);
	}
	return 0;
}