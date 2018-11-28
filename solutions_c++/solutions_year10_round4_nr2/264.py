// cheburashka, bear-mouse, team template

#include <cstdlib>
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>
#include <cstdio>
#include <sstream>
#include <stack>
#include <cstring>
#include <cmath>
#include <queue>
#include <set>
using namespace std;

typedef long long ll;
typedef vector < string > vs;
typedef vector <int> vi;
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define deb(x) cout << #x << ": " << x << endl;
#define debv(x) for(int i = 0; i < (x).size(); i++) cout << x[i] << ' '; cout << endl;
#define pb(x) push_back(x)

const int MAXM = 1025;
const int MAXR = 11;
int maxmiss[MAXM];
int NR,NM;
int cost[MAXM][MAXR];
int misslow[MAXM][MAXR];

int init()
{
	for(int i = 0; i < (1<<(NR-1)); i++)
	{
		misslow[i][0] = min(maxmiss[2*i],maxmiss[2*i+1]);
	}
	for(int r = 1; r < NR; r++)
	{
		for(int i = 0; i < (1<<(NR-1-r)); i++)
		{
			misslow[i][r] = min(misslow[2*i][r-1],misslow[2*i+1][r-1]);
		}
	}
}

int memo[MAXM][MAXR][MAXR];

int rec(int match, int round, int miss)
{
	if(round == -1) return 0;
	int & ret = memo[match][round][miss];
	if(ret != -1) return ret;
	ret = rec(match*2,round-1,miss) + rec(match*2+1,round-1,miss);
	if(miss == misslow[match][round])
	{
		return ret;
	}
	else if(miss > misslow[match][round])
	{
		deb("FAIL");
	}
	else
	{
		int neu = cost[match][round];
		neu += rec(match*2,round-1,miss+1) + rec(match*2+1,round-1,miss+1);
		ret = max(ret,neu);
		return ret;
	}
}
	
	
int main()
{
	int T;
	cin >> T;
	for(int tcase = 1; tcase <= T; tcase++)
	{
		cin >> NR;
		NM = (1<<NR);
		for(int i = 0; i < NM; i++)
			cin >> maxmiss[i];
		
		int total = 0;
		for(int r = 0; r < NR; r++)
		{
			for(int m = 0; m < (1<<(NR-r-1)); m++)
			{
				cin >> cost[m][r];
				total += cost[m][r];
			}
		}
		init();
		memset(memo,-1,sizeof(memo));
		int ret = total - rec(0,NR-1,0);
		
		
		printf("Case #%d: %d\n",tcase,ret);
	}
	return 0;
}
