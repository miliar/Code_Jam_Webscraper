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
#include <ctime>
using namespace std;
int dp[1005][105],N,S,Q;
vector<int> A;
int solve(int pos,int prev)
{
	if(pos>=Q)
		return 0;
	int &res=dp[pos][prev];
	if(res!=-1) return res;
	res=2000000000;
	if(A[pos]==prev)
	{
		for(int i=0;i<S;++i)
		{
			if(prev!=i)
				res=min(res,1+solve(pos+1,i));
		}
	}
	else
		res=solve(pos+1,prev);
		
	return res;
}
 
int main()
{
	int count=0;
	string s;
	scanf("%i",&N);
	while(N--)
	{
		count++;
		memset(dp,-1,sizeof(dp));
		scanf("%i",&S);
		getline(cin,s);
		map<string,int> M; 
		for(int i=0;i<S;++i)
		{
			getline(cin,s);
			M[s]=i;
		}
		scanf("%i",&Q);
		getline(cin,s);
		A.clear();
		for(int i=0;i<Q;++i)
		{
			getline(cin,s);
			A.push_back(M[s]);			
		}
		int ans=2000000000;
		if(Q==0)
			printf("Case #%i: 0\n",count);
		else
		{
			for(int i=0;i<S;++i)
				if(A[0]!=i)
					ans=min(ans,solve(1,i));
			printf("Case #%i: %i\n",count,ans);
		}
	}
}

