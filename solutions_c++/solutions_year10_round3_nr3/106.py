#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define all(a) a.begin(), a.end()
#define sz(a) a.size()
#define For(i, a, b) for(int i = a; i < b; i++)
#define Ror(i, a, b) for(int i = a - 1; i >= b; i--)

typedef pair<int, int> pii;
typedef long long lint;
typedef vector<int> vi;
typedef vector<vi> vvi;

const int Size = 10000;
char buffer[Size];

const int inf = 0x0fffffff;
const int white = 0, gray = 1, black = 2;

const double eps = 10e-6;

const int size = 32;

int ar[size][size];

int n, m;

int Solution(int nTest)
{
	scanf("%d%d", &m, &n);
	getchar();
	int ttt = n >> 2;
	For(i, 0, m)
	{
		gets(buffer);
		int l = strlen(buffer);
		for(int j = 0; j < n - l * 4; j++)
			ar[i][j] = 1;
		for(int j = n - l * 4, r = 0; j < n; j+= 4, r++)
		{
			char t = buffer[r];
			int ti =  isdigit(t) ? t - '0' : t - 'A' + 10;
			For(k, 0, 4)
			{
				ar[i][j + 3 - k] = (ti & 0x1) + 1;
				ti >>=1;
			}
		}
	}
	int d = max(m, n);
	map<int, int> sz;
	Ror(l, d+1, 1)
	{
		For(i, 0, m)
		{
			For(j, 0, n)
			{
				int flag = 1;
				For(ii, 0, l)
				{
					if(flag == 0)
						break;
					For(jj, 0, l)
					{
						int ni = i + ii;
						int nj = j + jj;
						if(ar[ni][nj] == 0)
						{
							flag = 0;
							break;
						}
						if(ii == 0 || jj == 0)
							continue;
						if(ni >= m || nj >= n)
						{
							flag = 0;
							break;
						}
						if(ar[ni][nj] == ar[ni-1][nj] || ar[ni][nj] == ar[ni][nj-1] || ar[ni][nj] != ar[ni-1][nj-1])
						{
							flag = 0;
							break;
						}
					}
				}
				if(flag == 1)
				{
					For(ii, 0, l)
					{
						For(jj, 0, l)
						{
							ar[i + ii][j + jj] = 0;
						}
					}
					if(sz.count(l))
						sz[l]++;
					else
						sz[l] = 1;
				}
			}
		}
	}
	printf("Case #%d: ", nTest + 1);

	printf("%d\n", sz.size());
	map<int, int>::iterator it = sz.end();
	do
	{
		it--;
		printf("%d %d\n", it->first, it->second);
	}
	while(it != sz.begin());




	return 1;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int i = 0, n = 9999;
	scanf("%d", &n);
	while(i < n && Solution(i))
		i++;

	return 0;
}