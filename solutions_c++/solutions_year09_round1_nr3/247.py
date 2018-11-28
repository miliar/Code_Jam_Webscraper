#include  <cstdio> 
#include  <cstdlib> 
#include  <cstring> 
#include  <string> 
#include  <vector> 
#include  <cmath> 
#include  <algorithm> 
#include  <cassert> 
#include  <set> 
#include  <map> 
#include  <queue> 
#include  <iostream> 
#include <fstream> 
using namespace std; 
#define pb push_back 
#define REP(i,n) for(int i=0;i<(n);i++ )  

typedef long long LL; 
typedef pair<int,int> pii; 


double dp[1<<10];
int C, N;

double gao(int t)
{
	if (t == ((1<<C) - 1))
		return 0;
	if (dp[t] >= 0 )
		return dp[t];
	double &res = dp[t];
	res = 1;
	double p = 0;
	int count = 0;
	REP(i, 1<<C)
	{
		int b = 0;
		REP(j, C)
		{
			if ((1<<j) & i)
				b++;
		}
		if (b == N)
			count++;
	}
	//cout<<t<<' '<<count<<endl;
	REP(i, 1<<C)
	{
		int b = 0;
		REP(j, C)
		{
			if ((1<<j) & i)
				b++;
		}
		if (b == N)
		{
			int U = i | t;
			if (U == t)
				p += 1.0/count;
			else
				res += 1.0/count * gao(U);
		}
	}
	res /= 1 - p;
	//cout<<t<<' '<<res<<' '<<p<<endl;
	return res;
}


int main()
{

	int cases;
	scanf("%d", &cases);
	REP(caseIndex, cases)
	{
		cin>>C>>N;
		printf("Case #%d: ", caseIndex + 1);
		REP(i, 1024)
			dp[i]= -1;
		printf("%.10lf\n", gao(0));
	}
}
