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

int memo[101][101];
bool M[101][101];

int H, W;

int f(int x, int y)
{
	if(x>H || y>W) return 0;
	if(x==H && y==W) return 1;
	if(M[x][y]) return 0;
	
	if(memo[x][y]!=-1) return memo[x][y];
	
	memo[x][y] = (f(x+1, y+2) + f(x+2, y+1))%10007;
	return memo[x][y];
}

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int nC;
	cin>>nC;
	
	for(int caso=1; caso<=nC; caso++)
	{
		cout<<"Case #"<<caso<<": ";
		
		memset(M, 0, sizeof(M));
		memset(memo, -1, sizeof(memo));
		
		int R;
		cin>>H>>W>>R;
		
		for(int i=0; i<R; i++)
		{
			int r, c;
			cin>>r>>c;
			M[r][c] = 1;
		}
		
		cout<<f(1, 1)<<endl;
	}
	
	return 0;
}
