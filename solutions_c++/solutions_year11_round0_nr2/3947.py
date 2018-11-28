#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

const int N = 256;

char combine[N][N];
bool opposed[N][N];

int main()
{
	int ncases, c, d, n, i, j;
	char a, b, r;
	vector<char> list;
	
	cin >> ncases;
	for (int caseno = 1; caseno <= ncases; caseno++)
	{
		fill(combine[0], combine[N], 0);
		fill(opposed[0], opposed[N], false);
		list.clear();
			
		cin >> c;
		for (i = 0; i < c; i++)
		{
			cin >> a >> b >> r;
			combine[a][b] = combine[b][a] = r;
		}

		cin >> d;
		for (i = 0; i < d; i++)
		{
			cin >> a >> b;
			opposed[a][b] = opposed[b][a] = true;
		}

		cin >> n;
		for (i = 0; i < n; i++)
		{
			cin >> a;
			if (list.size() == 0)
			{
				list.push_back(a);
				continue;
			}

			if (combine[a][list.back()] > 0)
			{
				list.back() = combine[a][list.back()];
				continue;
			}

			for (j = 0; j < list.size(); j++)
				if (opposed[a][list[j]])
					break;

			if (j < list.size())
				list.clear();
			else
				list.push_back(a);
		}

		printf("Case #%i: [", caseno);

		for (i = 0; i < list.size(); i++)
		{
			if (i > 0)
				printf(", ");
			printf("%c", list[i]);
		}
		printf("]\n");
	}
}
