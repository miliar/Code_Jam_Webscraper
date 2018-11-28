#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
using namespace std;

#ifndef ONLINE_JUDGE
#include<fstream>
  ifstream in("A-large.in.txt");
  ofstream out("a.out");
#define cin in
#define cout out
#endif


const int maxn = 10010;
int node[maxn], change[maxn];
int dp[maxn][2];
int value[maxn];
int n,v, iner;

void cal(int index)
{
	if(value[index] != -1)
		return;

	cal(index * 2);
	cal(index * 2 + 1);

	if(node[index] == 1)
		value[index] = value[index *2] && value[index * 2 + 1];
	else value[index] = value[index * 2] || value[index * 2 + 1];

}

void search(int index)
{
	if(dp[index][0] != -1 && dp[index][1] != -1)
	{
		return;
	}

	search(index * 2);
	search(index * 2 + 1);

	dp[index][value[index]] = 0;

	int best = maxn;
	int cur;
	int left = index * 2, right = index * 2 + 1;

		if(node[index] == 1) //and
		{
			if(value[index] == 0) 
			{
				cur = dp[left][1] + dp[right][1];
				if(cur < best)
					best = cur;
				
			}
			else
			{
				cur = dp[left][0];
				if(cur < best) 
					best = cur;
				cur = dp[right][0];
				if(cur < best) 
					best = cur;
			}

		}
		else        //or
		{
			if(value[index] == 0) {
				cur = dp[left][1];
				if(cur < best) 
					best = cur;
				cur = dp[right][1];
				if(cur < best) 
					best = cur;

			}
			else 
			{
				cur = dp[left][0] + dp[right][0];
				if(cur < best)
					best = cur;
			}

		}

	if(change[index])
	{
		
		if(node[index] == 1) //and
		{
			//changed to or

			if(value[index] == 0) {
				cur = dp[left][1] + 1;
				if(cur < best) 
					best = cur;
				cur = dp[right][1] + 1;
				if(cur < best) 
					best = cur;

			}
			else 
			{
				cur = dp[left][0] + dp[right][0] + 1;
				if(cur < best)
					best = cur;
			}

		}
		else
		{
			//changed to and
			if(value[index] == 0) 
			{
				cur = dp[left][1] + dp[right][1] + 1;
				if(cur < best)
					best = cur;
				
			}
			else
			{
				cur = dp[left][0] + 1;
				if(cur < best) 
					best = cur;
				cur = dp[right][0] + 1;
				if(cur < best) 
					best = cur;
			}


		}


	}

	dp[index][1-value[index]] = best;


}

int main()
{
	int cs;
	cin>>cs;
	for(int ct = 1; ct <= cs; ct ++)
	{
		cout << "Case #"<<ct<<": ";
		memset(dp, 0xff, sizeof(dp));
		memset(value, 0xff, sizeof(value));

		cin >> n >> v;
		iner = (n-1)/2;

		for(int i = 1; i <= iner; i ++)
			cin>>node[i]>>change[i];

		for(int i = iner+1; i <= n; i ++)
		{
			cin >> node[i];
			value[i] = node[i];
			dp[i][value[i]] = 0;
			dp[i][1-value[i]] = maxn;
		}
		cal(1);
		search(1);
		if(dp[1][v] >= maxn)
			cout << "IMPOSSIBLE"<<endl;
		else cout<<dp[1][v]<<endl;

		
	}
}
