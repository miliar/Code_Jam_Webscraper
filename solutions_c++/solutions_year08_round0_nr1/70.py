// program.cpp : Defines the entry point for the console application.
//

// BEGIN CUT HERE
#pragma warning(disable:4786)
#include <stdafx.h>
// END CUT HERE
#include <string>
#include <map>
#include <set>
#include <vector>
#include <deque>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <numeric>
using namespace std;

int dp[2000][200];

void process(int num)
{
	int S,Q;
	string ser[200];
	int qur[2000];
	char ts[2000];

	cin>>S;cin.getline(ts,1000);
	for(int i=0;i<S;i++) {cin.getline(ts,1000);ser[i]=string(ts);}
	cin>>Q;cin.getline(ts,1000);
	for(int i=0;i<Q;i++)
	{
		cin.getline(ts,1000);
		string ss=string(ts);
		for(int j=0;j<S;j++) if(ss==ser[j]) {qur[i]=j;break;}
	}

	for(int i=0;i<S;i++) dp[Q][i]=0;
	for(int i=Q-1;i>=0;i--)
	{
		for(int j=0;j<S;j++)
		{
			if(qur[i]!=j) dp[i][j]=dp[i+1][j];
			else
			{
				dp[i][j]=10000;
				for(int k=0;k<S;k++) if(k!=j&&dp[i+1][k]+1<dp[i][j]) dp[i][j]=dp[i+1][k]+1;
			}
		}
	}

	int ret=10000;
	for(int i=0;i<S;i++) if(dp[0][i]<ret) ret=dp[0][i];
	cout<<"Case #"<<num<<": "<<ret<<endl;
}

int main(void)
{
	int n;
	cin>>n;
	for(int i=1;i<=n;i++) process(i);
	return 0;
}

