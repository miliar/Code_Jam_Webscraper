#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <cstdio>
#include <cmath>
#include <cstdlib>

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

#define eps 1e-8
#define pi acos(-1)

using namespace std;

int R, C;
vector <string> V;

int memo[10][1<<10];

int f(int r, int mask)
{
	if(memo[r][mask]!=-1) return memo[r][mask];
	
	
	if(r==0)
	{
		int maxN = 0;
		
		for(int m=0; m<(1<<C); m++)
		{
			bool ok = true;
		
			for(int j=0; j<C; j++)
				if( (m & (1<<j)) && (V[r][j]=='x' || (mask & (1<<j))) )
					ok = false;
		
			for(int j=0; j<C-1; j++)
				if( (m & (1<<j)) && (m & (1<<(j+1))) )
					ok = false;
		
			if(ok)
			{
				maxN = max(maxN, __builtin_popcount(m));
			}
		}
	
		memo[r][mask] = maxN;
		return maxN;
	}
	
	int maxN = 0;
	
	for(int m=0; m<(1<<C); m++)
	{
		bool ok = true;
		
		for(int j=0; j<C; j++)
			if( (m & (1<<j)) && (V[r][j]=='x' || (mask & (1<<j))) )
				ok = false;
		
		for(int j=0; j<C-1; j++)
			if( (m & (1<<j)) && (m & (1<<(j+1))) )
				ok = false;
		
		if(ok)
		{
			int newmask = 0;
			for(int j=0; j<C; j++)
			{
				if(V[r-1][j]=='x') newmask ^= (1<<j);
				else
				{
					if(j>0 && (m & (1<<(j-1)))) newmask ^= (1<<j);
					else if(j+1 < C && (m & (1<<(j+1)))) newmask ^= (1<<j);
				}
			}
			maxN = max(maxN, __builtin_popcount(m) + f(r-1, newmask));
		}
	}
	
	memo[r][mask] = maxN;
	return maxN;
}

int main()
{
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int nC;
	cin>>nC;
	
	for(int caso=1; caso<=nC; caso++)
	{
		cout<<"Case #"<<caso<<": ";
		
		cin>>R>>C;
		V = vector <string> (R);
		for(int i=0; i<R; i++)
			cin>>V[i];
		
		memset(memo, -1, sizeof(memo));
		
		cout<<f(R-1, 0)<<endl;
	}
	
	return 0;
}
