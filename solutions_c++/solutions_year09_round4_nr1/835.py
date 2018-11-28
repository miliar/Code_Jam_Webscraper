#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <ctime>
using namespace std;

int t, n;
char c[100][100];
int a[100];

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	cin >> t;
	for (int T = 1; T <= t; T++)
	{
		cin >> n;
		memset(a, 0, sizeof a);

		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
			{
				cin >> c[i][j];
				if (c[i][j] == '1')
					a[i] = j;
			}

		int res = 0;

		for (int i = 0; i < n; i++)
			if (a[i] > i)
				for (int j = i+1; j < n; j++)
					if (a[j] <= i)
					{
						for (int k = j; k > i; k--)
						{
							res++;
							swap(a[k], a[k-1]);
						}

						break;
					}

		cout << "Case #" << T << ": " << res << endl;
	}


	return 0;
}