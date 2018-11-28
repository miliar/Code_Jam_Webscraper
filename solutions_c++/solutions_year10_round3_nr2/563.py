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
#include <cstring>

using namespace std;

int memo[1001][1001];

int ff(int L, int P, int C)
{
	if(L*C >= P) return 0;
	
	if(memo[L][P]!=-1) return memo[L][P];
	int x = 1<<30;
	
	for(int i=L+1; i<P; i++)
	{
		int n1 = ff(L, i, C);
		int n2 = ff(i, P, C);
		x = min(x, 1 + max(n1, n2));
	}
	
	memo[L][P] = x;
	return x;
}

int f(int L, int P, int C)
{
	if(L*C >= P) return 0;
	
	int x = 0;
	while(1)
	{
		if(L * C >= P) break;
		
		L = L * C;
		x++;
		
		if(f(L, P, C) < x) break;
	}
	return x;
}

int main()
{
	freopen("B-small-attempt2.in", "r", stdin);
	//freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int nCasos;
	cin>>nCasos;

	for(int caso=1; caso<=nCasos; caso++)
	{
		cout<<"Case #"<<caso<<": ";
		
		int L, P, C;
		cin>>L>>P>>C;
		
		memset(memo, -1, sizeof(memo));
		int x = ff(L, P, C);
		cout<<x<<endl;
	}
	
	return 0;
}
