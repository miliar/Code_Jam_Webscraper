#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <fstream>
#include <map>
#include <set>
using namespace std;

const int Inf = 10000000;

int M;
int M1;
vector<int> v1;
vector<int> v2;

struct My
{
	int v[2];
};

My Do(int node)
{
	My res;
	if (node >= M1)
	{
		res.v[v1[node]] = 0;
		res.v[1-v1[node]] = Inf;
		return res;
	}

	My sub1 = Do((node+1)*2);
	My sub2 = Do((node+1)*2-1);

	int ror0 = sub1.v[0] + sub2.v[0];
	int ror1 = min(sub1.v[1], sub2.v[1]);
	int ran0 = min(sub1.v[0], sub2.v[0]);
	int ran1 = sub1.v[1] + sub2.v[1];

	if (v1[node] == 0)
	{
		res.v[0] = ror0;
		res.v[1] = ror1;
	}
	else
	{
		res.v[0] = ran0;
		res.v[1] = ran1;
	}

	if (v2[node] == 1)
	{
		if (v1[node] == 0)
		{
			if (ror0 > ran0 + 1) res.v[0] = ran0+1;
			if (ror1 > ran1 + 1) res.v[1] = ran1+1;
		}
		else
		{
			if (ran0 > ror0 + 1) res.v[0] = ror0+1;
			if (ran1 > ror1 + 1) res.v[1] = ror1+1;
		}
	}
	return res;
}

int main()
{
	int N;
	cin >> N;

	for(int i = 1; i <= N; ++i)
	{
		cin >> M;
		int V;
		cin >> V;
		M1 = (M-1)/2;
		v1.clear();
		v2.clear();

		for(int j = 0; j < M1; ++j)
		{
			int vv1;
			int vv2;
			cin >> vv1 >> vv2;
			v1.push_back(vv1);
			v2.push_back(vv2);
		}

		for(int j = M1; j < M; ++j)
		{
			int vv1;
			cin >> vv1;
			v1.push_back(vv1);
		}

		My res = Do(0);

		if (res.v[V] > 10000)
		{
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
		}
		else
		{
			cout << "Case #" << i << ": " << res.v[V] << endl;
		}
	}
}