
#include <iostream>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <queue>
#include <map>
#include <vector>
#include <ctime>
#include <cctype>
using namespace std;

long long int tree[100000][2];

void solve(int testcase)
{
	int n;
	cin >> n;

	long long int A, B, C, D, x0, y0, M;
	cin >> A >> B >> C >> D >> x0 >> y0 >> M;

	tree[0][0] = x0;
	tree[0][1] = y0;
	for (int i = 1; i < n; i++)
	{
		tree[i][0] = (A*tree[i-1][0] + B) % M;
		tree[i][1] = (C*tree[i-1][1] + D) % M;
	}
	
	long long int total = 0;
	for (int i = 0; i < n; i++)
		for (int j = i+1; j < n; j++)
			for (int k = j+1; k < n; k++)
			{
				if ((tree[i][0]+tree[j][0]+tree[k][0])%3 == 0)
					if ((tree[i][1]+tree[j][1]+tree[k][1])%3 == 0)
					{
						total++;
					}
			}

	printf("Case #%d: %lld\n", testcase, total);
}



int main()
{
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
		solve(i+1);
	return 0;
}
