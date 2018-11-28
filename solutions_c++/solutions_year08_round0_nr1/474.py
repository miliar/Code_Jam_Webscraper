#define MAX_Q 1024
#define MAX_S 128

#include <iostream>
#include <map>
#include <string>

using namespace std;

int S, Q;
int queries[MAX_Q]; 

void input(void)
{
	int i;
	string dummy;
	map<string, int> engines;
	
	cin>>S;
	getline(cin, dummy);
	for(i=0; i<S; ++i)
	{
		string engine;
		getline(cin, engine);
		engines.insert(make_pair(engine, i));
	}	
	
	cin>>Q;
	getline(cin, dummy);
	for(i=0; i<Q; ++i)
	{
		string query;
		getline(cin, query);
		queries[i] = engines.find(query)->second;
	}
}

int calcDp(void)
{
	static int dp[MAX_Q][MAX_S];
	int query, engine;
	int i;
	int currVal;
	int ans;
	
	for(engine=0; engine<S; ++engine)
	{
		dp[0][engine]=0;
	}
	dp[0][queries[0]] = Q; // infinity

	for(query=1; query<Q; ++query)
	{
		for(engine=0; engine<S; ++engine)
		{
			dp[query][engine] = query; // use a different engine for every query
			for(i=0; i<S; ++i)
			{
				currVal = dp[query-1][i] + (i!=engine);
				if(currVal<dp[query][engine])
				{
					dp[query][engine] = currVal;
				} 
			}
			dp[query][queries[query]] = Q; // infinity
		}
	}
	
	--query;
	ans = Q; // infinity
	for(engine=0; engine<S; ++engine)
	{
		if(dp[query][engine]<ans)
		{
			ans = dp[query][engine];
		}
	}
	
	return ans;
}

int main(void)
{
	int N, i;
	
	cin>>N;
	for(i=1; i<=N; ++i)
	{
		input();
		cout<<"Case #"<<i<<": "<<calcDp()<<endl;
	}
	return 0;
}
