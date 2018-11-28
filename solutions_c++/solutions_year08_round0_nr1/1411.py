#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

#include <iostream>
#include <fstream>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <list>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;

string eng[100],query[1000];
int cnt[100];
int S,Q;
int dp[100][1000];

int main()
{
	int ncase;
	int m;
	ofstream cout("1.out");
	cin >> ncase;
	m = 0;
	while (ncase--)
	{
		m++;
		cout << "Case #"<< m << ": ";
		memset(cnt,0,sizeof(cnt));
		cin >> S;
		getchar();
		int i,j;
		
		for (i = 0 ; i < S ; i++)
			getline(cin,eng[i]);
		cin >> Q;
		getchar();
		for (i = 0 ; i < S ; i++)
		{
			for (j = 0 ; j < Q ; j++)
			{
				dp[i][j] = 100000;
			}
		}
		if (Q == 0)
		{
			cout << 0 << endl;
		}
		else
		{
			getline(cin,query[0]);
			int k = 1;
			int flag = 0;
			for (i = 0 ; i < S ; i++)
			{
				if (cnt[i] == 0 &&query[0] == eng[i])
				{
					cnt[i]++;
					flag++;
					break;
				}
			}
			for (j = 1 ; j < Q ;j++)
			{
				string sztmp;
				getline(cin,sztmp);
				if (sztmp != query[k-1])
					query[k++] = sztmp;
				for (i = 0 ; i < S ; i++)
				{
					if (cnt[i] == 0 &&query[k-1] == eng[i])
					{
						cnt[i]++;
						flag++;
						break;
					}
				}
			}
			Q = k;
			if (flag != S)
			{
				cout << 0 << endl;
			}
			else
			{
				for (i = 0 ; i < S ; i++)
				{
					if (eng[i] != query[Q-1])
						dp[i][Q-1] = 0;
				}
				for (j = Q - 2 ; j >= 0 ; j--)
				{
					for (i = 0 ; i < S ; i++)
					{
						if (eng[i] == query[j])
						{
							dp[i][j] = 100000;
						}
						else
						{
							for (k = 0 ; k < S ; k++)
							{
								if (k == i)
								{
									if (dp[i][j] > dp[k][j+1])
										dp[i][j] = dp[k][j+1];
								}
								else
								{
									if(dp[i][j] > dp[k][j+1] + 1)
										dp[i][j] = dp[k][j+1]+1;
								}
									
							}	
						}												
					}
				}
				int res = 1000000;
				for ( i = 0 ; i < S ; i++)
				{
					if (res > dp[i][0])
						res = dp[i][0];
				}
				cout << res << endl;
			}
		}
		
	}
	return 0;
}