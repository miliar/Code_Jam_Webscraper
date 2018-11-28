#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>

using namespace std;

int n;
string mat[100];
int r[100];
int ans;

bool check(int s)
{
	int aa[100];
	for (int i = s; i < n; i++)
		aa[i] = r[i];
	sort(aa+s, aa+n);
	for (int i = s; i < n; i++)
		if (aa[i] > i) return false;
	return true;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cin >> n;
		memset(r, 0, sizeof(r));
		for (int i = 0; i < n; i++)
		{
			cin >> mat[i];
			for (int j = 0; j < n; j++)
				if (mat[i][j] == '1') r[i] = j;	
		}
		ans = 0;
		for (int i = 0; i < n-1; i++)
		{
			for (int j = i; j < n; j++)
			{
				if (r[j] <= i)
				{
					swap(r[i], r[j]);
					if (!check(i+1))
						swap(r[i], r[j]);
					else
					{
						if (j > i)
						{
							int tmp = r[j];
							for (int k = j; k > i+1; k--)
								r[k] = r[k-1];
							r[i+1] = tmp;
						}
						ans += j-i;
						break;
					}
				}
			}
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
}