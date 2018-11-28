#include <cstdio>
#include <vector>

using namespace std;

int N;
vector<pair<int,int> > vec;

bool intersect(pair<int,int> a, pair<int,int> b)
{
	if (a.first < b.first)
		if (a.second > b.second)
			return true;
	if (a.first > b.first)
		if (a.second < b.second)
			return true;
	return false;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large_out.txt", "w", stdout);
	int T;
	scanf("%d",&T);
	for (int t=1; t<=T; t++)
	{
		scanf("%d", &N);
		vec.clear();
		for (int i=0; i<N; i++)
		{
			int a,b;
			scanf("%d%d", &a, &b);
			vec.push_back(make_pair(a,b));
		}
		int res = 0;
		for (int i=0; i<vec.size(); i++)
		{
			for (int j=0; j<i; j++)
			{
				if (intersect(vec[i],vec[j]))
					res++;
			}
		}
		printf("Case #%d: %d\n", t, res);
	}
}