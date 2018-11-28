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

vector <string> M;
int R, C;

int dx[] = {1, 1, 1, 0, 0, -1, -1, -1};
int dy[] = {0, 1, -1, 1, -1, 1, 0, -1};

bool memo[4][4][1<<16];
bool done[4][4][1<<16];

bool gana(int x, int y, int mask)
{
	if(done[x][y][mask]) return memo[x][y][mask];
	
	bool ans = 0;
	
	for(int i=0; i<8; i++)
	{
		int I = x + dx[i];
		int J = y + dy[i];
		
		if(I>=0 && I<R && J>=0 && J<C && M[I][J]=='.' && (mask&(1<<(I*C + J)))==0)
		{
			if(!gana(I, J, mask ^ (1<<(I*C + J)))) ans = 1;
		}
	}
	memo[x][y][mask] = ans;
	done[x][y][mask] = 1;
	return ans;
}

int main()
{
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int nCasos;
	cin>>nCasos;
	
	for(int caso=1; caso<=nCasos; caso++)
	{
		cout<<"Case #"<<caso<<": ";
		
		memset(done, 0, sizeof(done));
		
		cin>>R>>C;
		M = vector <string> (R);
		
		for(int i=0; i<R; i++)
			cin>>M[i];
		 
		int x, y;
		
		for(int i=0; i<R; i++)
		{
			int p = M[i].find("K");
			if(p!=-1)
			{
				x = i;
				y = p;
			}
		}
		
		M[x][y] = '.';
		
		if(gana(x, y, (1<<(x*C + y)))) cout<<"A";
		else cout<<"B";
		
		cout<<endl;
	}
	
	return 0;
}
