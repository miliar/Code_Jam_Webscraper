#include <iostream>
#include <string>
#include <string.h>
#include <vector>
#include <math.h>
#include <set>
#include <time.h>
#include <algorithm>
using namespace std;

const int MAX = 15;

int g[MAX];
int R, k, N;

int go()
{
	vector<int>v;
	vector<int>s;
	for(int i = 0; i < R; i++)  for(int j = 0; j < N; j++)
		v.push_back(g[j]);
	int t = 0;
	for(int i = 0; i < v.size(); i++)
	{
		if(v[i] > k)  continue;
		if(t + v[i] <= k)  t += v[i];
		else
		{
			s.push_back(t);
			t = v[i];
		}
	}
	if(t)  s.push_back(t);
	int res = 0;
	for(int i = 0; i < s.size() && i < R; i++)  res += s[i];
	return res;
}

int main()
{
	freopen("d:\\C-small-attempt0.in", "r", stdin);
	freopen("d:\\C-small-attempt0.out", "w", stdout);

	int T;
	int c = 0;
	scanf("%d", &T);
	while(T--)
	{
		scanf("%d%d%d", &R, &k, &N);
		for(int i = 0; i < N; i++)  scanf("%d", &g[i]);
		printf("Case #%d: %d\n", ++c, go());
	}
}