#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>
#include <string>
#include <set>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <cmath>
#include <vector>
using namespace std;

const long long MAXN = 5000, MAXP = 10, inf = 1000, infm = 2100000000;
long long T, P;
long long value[MAXN], M[MAXN], DP[MAXN][MAXP], themin[MAXN];

long long mymin(long long a, long long b)
{
	return a < b ? a : b;
}

long long findmin(long long now)
{
	if(themin[now] != inf) return themin[now];
	if((now<<1LL)+1 > (1<<P)) //leaf
	{
		long long delta = now - (1<<(P-1));
		themin[now] = mymin(M[delta*2], M[delta*2+1]);

		return themin[now];
	}
	
	themin[now] = mymin(findmin(now<<1), findmin((now<<1)+1));
}

long long treedp(long long nowmat, long long miss)
{
	if(DP[nowmat][miss] != infm) return DP[nowmat][miss];

	long long ret = infm, res, lc = nowmat<<1, rc = (nowmat<<1)+1;

	if((nowmat<<1)+1 > (1<<P)) //leaf
	{
		//miss this one
		if(miss+1 <= themin[nowmat])
			ret = 0;
		else  //don't miss this one
			ret = value[nowmat];
	}
	else
	{
		//miss this one
		if(miss+1 <= themin[rc] && miss+1 <= themin[lc])
			ret = treedp(rc, miss+1)+treedp(lc, miss+1);

		//don't miss this one
		res = treedp(rc, miss)+treedp(lc, miss)+value[nowmat];
		ret = ret < res ? ret : res;		
	}

	DP[nowmat][miss] = ret;
	return ret;
}
	
int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	
	cin>>T;

	for(int t = 0; t < T; t++)
	{
		//intialization
		for(int i = 0; i < MAXN; i++)
		{
			for(int j = 0; j < MAXP; j++)
				DP[i][j] = infm;
			themin[i] = inf;
		}
		cin>>P;
		
		for(int i = 0; i < (1<<P); i++)
			cin>>M[i];

		long long acc = (1<<P)-1 - (1 <<(P-1));
		
		for(int i = P-1; i>=0; i--)
		{
			long long upper = 1<<i;
			for(int j = 1; j <= upper; j++)
				cin>>value[acc+j];

			if(i) acc -= (1<<(i-1));
		}

		findmin(1);

		cout<<"Case #"<<t+1<<": "<<treedp(1, 0)<<endl;		
	}

	return 0;
}
