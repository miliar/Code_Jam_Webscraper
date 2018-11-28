
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
using namespace std;

#define sz 105
#define sz2 30

bool edge[2*sz][2*sz];
int matrix[sz][sz2];
int temp[sz][sz2];
int index[sz];
int prev[2*sz];
bool done[sz];
bool mark[2*sz];

bool UDF(int i, int j)
{
	if (matrix[i][0] < matrix[j][0]) return true;
	else return false;
}

int main ()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large-out.txt", "w", stdout);
	int test_cases;
	scanf("%d", &test_cases);
	for (int numb = 0; numb < test_cases; numb++)
	{
		int n, k;
		scanf("%d %d", &n, &k);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < k; j++)
				scanf("%d", &matrix[i][j]);
		for (int i = 0; i < n; i++)
			index[i] = i;
		sort(index, index+n, UDF);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < k; j++)
				temp[i][j] = matrix[index[i]][j];
//		for (int i = 0; i < n; i++)
//		{
//			for (int j = 0; j < k; j++)
//				cout << temp[i][j] << ' ';
//			cout << endl;
//		}
		memset(edge, 0, sizeof(edge));
//		cout << "Edge" << endl;
		for (int i = 0; i < n; i++)
			for (int j = i+1; j < n; j++)
			{
				edge[i][sz+j] = true;
				for (int l = 0; l < k && edge[i][sz+j]; l++)
					if (temp[i][l] >= temp[j][l])
						edge[i][sz+j] = false;
//				if (edge[i][sz+j])
//					cout << i << ' ' << j << endl;
			}
		int ans = 0;
		for (int i = 0; i < 2*sz; i++)
			prev[i] = -1;
		bool val = false;
		int end;
		memset(done, 0, sizeof(done));
		for (int i = 0; i < n; i++)
		{
			// if you can find an augmenting path from i, ans++
			memset(mark, 0, sizeof(mark));
			mark[i] = true;
			deque <int> queue (1, i);
			val = false;
			while (!queue.empty())
			{
				int t = queue.front();
				for (int j = 0; j < 2*sz && !val; j++)
					if (edge[t][j])
						if (!mark[j])
						{
							mark[j] = true;
							prev[j] = t;
							queue.push_back(j);
							if (j >= sz && !done[j-sz])
							{
								done[j-sz] = true;
								ans++;
								val = true;
								end = j;
							}
						}
				if (val)
				{
					while (prev[end] != -1)
					{
						edge[prev[end]][end] = false;
						edge[end][prev[end]] = true;
						end = prev[end];
					}
					break;
				}
				queue.pop_front();
			}
		}
		printf("Case #%d: %d\n", numb+1, n-ans);
	}
	return 0;
}
