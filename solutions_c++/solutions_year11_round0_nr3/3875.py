#include <stdio.h>

#include <iostream>
#include <vector>

using namespace std;
int add(int a, int b)
{
	int ret = 0;

	for(int i = 0;i<20;i++)
	{
		ret |= ((1 & ((a >> i) + (b >> i)))) << i;
	}

	return ret;
}

int value[1006]; // value of each candy.

//int dp[1005][(1 << 20)+1]; // Too large to do memset.
int dp1[1<<21], dp2[1<<21];
int flag[(1<<21)];
vector<int> local1, local2; // Start from.

int check_max(int n, vector<int> *local, int *p)
{
	int sum = 0;
	for(int i = 0;i<n;i++)
	{
		sum = add(sum, value[i]);
	}

	int ans = -1;
	for(int i = 0;i<local->size();i++)
	{
		if(sum != (*local)[i] && add(sum, (*local)[i]) == (*local)[i])
		{
			ans = max(ans, p[(*local)[i]]);
		}
	}

	return ans;
}

void work()
{
	int *p1 = dp1, *p2 = dp2;
	vector<int> *p3 = &local1, *p4 = &local2;
	
	memset(dp1, 0, sizeof(dp1));
	memset(dp2, 0, sizeof(dp2));

	int n;
	scanf("%d", &n);
	for(int i = 0;i<n;i++)
	{
		scanf("%d", &value[i]);
	}

	// init dp
	p1[0] = 0;
	p1[value[0]] = value[0];
	p3->clear();
	memset(flag, 0, sizeof(flag));
	flag[0] = flag[value[0]] = 1;
	p3->push_back(0);
	p3->push_back(value[0]);

	int sum;
	for(int i = 1;i<n;i++)
	{
		p4->clear();
		memset(flag, 0, sizeof(flag));
		for(int j = 0; j<p3->size();j++)
		{
			p2[(*p3)[j]] = max(p2[(*p3)[j]], p1[(*p3)[j]]);
			if(!flag[(*p3)[j]])
			{
				p4->push_back((*p3)[j]);
				flag[(*p3)[j]] = 1;
			}
			sum = add((*p3)[j], value[i]);
			p2[sum] = max(p2[sum], p1[(*p3)[j]] + value[i]);

			if(!flag[sum])
			{
				flag[sum] = 1;
				p4->push_back(sum);
			}
		}

		// Rotate.
		int *tmp = p1;
		p1 = p2;
		p2 = tmp;

		vector<int> *vec_tmp = p3;
		p3 = p4;
		p4 = vec_tmp;
	}

	int ans = check_max(n, p3, p1);

	static int cas = 1;
	if(ans < 0)
		printf("Case #%d: NO\n", cas ++);
	else
		printf("Case #%d: %d\n", cas ++, ans);
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	for(int i = 0;i<t;i++)
	{
		work();
	}

	return 0;
}