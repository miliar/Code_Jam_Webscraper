#include <iostream>
#include <cstring>
using namespace std;

const int MAXN = 100;
const int MAXK = 25;

int n, k;
int price[MAXN][MAXK];
bool edge[MAXN][MAXN];
bool footmark[MAXN];
int match[MAXN];

inline bool smaller(int a, int b)
{
	for(int i=0; i<k; i++)
		if (price[a][i] >= price[b][i])
			return false;
	return true;
}

void read()
{
	cin >> n >> k;
	for(int i=0; i<n; i++)
		for(int j=0; j<k; j++)
			cin >> price[i][j];
	memset(edge, false, sizeof(edge));
	for(int i=0; i<n; i++)
		for(int j=0; j<n; j++)
			if (smaller(i, j))
				edge[i][j] = true;
}

bool hdfs(int v)
{
	if (v == -1)
		return true;
	if (footmark[v])
		return false;
	footmark[v] = true;
	for(int i=0; i<n; i++)
		if (edge[v][i] && hdfs(match[i]))
		{
			match[i] = v;
			return true;
		}
	return false;
}

int maxMatch()
{
	int res = 0;
	memset(match, -1, sizeof(match));
	for(int i=0; i<n; i++)
	{
		memset(footmark, false, sizeof(footmark));
		if (hdfs(i))
			res++;
	}
	return res;
}

int main()
{
	int T;
	cin >> T;
	for(int ic=0; ic<T; ic++)
	{
		read();
		printf("Case #%d: %d\n", ic+1, n-maxMatch());
	}
}

