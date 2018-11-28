#include <cstdio>
#include<iostream>
#include <string>
#include <vector>
#include <stack>

using namespace std;

int main ()
{
	freopen ("outla.txt","w",stdout);
	freopen ("A-large.in","r",stdin);

	int tc, n, m, i, j, k, z, cur, arr [1000][11];

	scanf ("%d", &tc);

	for (i = 1; i <= tc; i++)	{

		scanf ("%d", &n);

		for (j = 0; j <n; j++)	{

			scanf ("%d", &arr[j][0]);

			for (k= 1; k<=arr[j][0]; k++)
				scanf ("%d", &arr[j][k]);
		}

		stack<int> st;
		int visited [1000], flag = 0;

		for (z = 1; z <= n; z++)	{

			for (j = 0; j <n; j++)
				visited[j] = 0;

			st.push(z);
			flag = 0;

			while (!st.empty())	{

				cur	=	st.top();
				st.pop();

				for (k = 1; k <= arr[cur-1][0]; k++)	{
				
					st.push(arr[cur-1][k]);
					visited [arr[cur-1][k]-1]++;

					if (visited [arr[cur-1][k]-1] > 1)	{

						flag = 1;
						break;
					}
				}

				if (flag == 1)
					break;
			}

			if (flag == 1)
				break;

		}

		if (flag == 1)
			printf ("Case #%d: Yes\n", i);
		else
			printf ("Case #%d: No\n", i);
	}

	return 0;
}