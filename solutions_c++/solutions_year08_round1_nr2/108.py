#include <iostream>
#include <vector>
using namespace std;

const int MAXN = 2000;

bool multed[MAXN];
int likeMulted[MAXN];
vector<int> likeUnmulted[MAXN];
int nOfTest, n, m;

void read()
{
	cin >> n >> m;
	memset(likeMulted, -1, sizeof(likeMulted));
	for(int i=0; i<m; i++)
	{
		likeUnmulted[i].clear();
		int T;
		cin >> T;
		for(int j=0; j<T; j++)
		{
			int a, b;
			cin >> a >> b;
			a--;
			if (b == 1)
				likeMulted[i] = a;
			else
				likeUnmulted[i].push_back(a);
		}
	}
}

inline bool check(int p)
{
	if (multed[likeMulted[p]])
		return true;
	for(int i=0; i<likeUnmulted[p].size(); i++)
		if (!multed[likeUnmulted[p][i]])
			return true;
	return false;
}

void work()
{
	read();
	memset(multed, false, sizeof(multed));

	bool pass = false;
	while (!pass)
	{
		pass = true;
		for(int i=0; i<m; i++)
			if (!check(i))
			{
				pass = false;
				if (likeMulted[i] == -1)
				{
					cout << " IMPOSSIBLE" << endl;
					return;
				}
				else
					multed[likeMulted[i]] = true;
			}
	}
	for(int i=0; i<n; i++)
		cout << " " << multed[i];
	cout << endl;
}

int main()
{
//	freopen("b.in", "r", stdin);
//	freopen("b.out", "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);
	cin >> nOfTest;
	for(int testCase=0; testCase<nOfTest; testCase++)
	{
		printf("Case #%d:", testCase+1);
		work();
	}
}
