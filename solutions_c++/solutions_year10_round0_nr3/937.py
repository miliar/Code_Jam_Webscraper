#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>

using namespace std;

int sum[1000][2000];
int R,k,N;
int g[1000],idx[1000];

int main()
{
	int tcase;
	cin >> tcase;
	for(int i = 1; i <= tcase; i++)
	{
		memset(sum,0,sizeof(sum));
		cout << "Case #" << i << ": ";
		cin >> R >> k >> N;
		for(int i = 0; i < N; i++)
		{
			cin >> g[i];
		}
		for(int i = 0; i < N; i++)
		{
			for(int j = i; j < i+N; j++)
			{
				if(i == 0 && j == 0)sum[i][j] = g[i];
				sum[i][j] = sum[i][j-1]+g[j%N];
				if(sum[i][j] <= k)idx[i] = j;
			}
		}
		int now = 0;
		long long ret = 0;
		for(int i = 0; i < R; i++)
		{
			ret += sum[now][idx[now]];
			now = (idx[now]+1)%N;
		}
		cout << ret << endl;
	}
	return 0;
}