#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <map>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <numeric>

#define all(x) x.begin() , x.end()
#define pb(x) push_back(x)
#define sz(x) ((int) x.size())
#define INF 0x7fffffff
#define LL long long
#define LD long double
#define VI vector<int>
#define VS vector<string>

using namespace std;

bool check(char G[][60], int i, int j, int M, int N)
{
	if(i+1>=M || j+1>=N || G[i+1][j] != '#'
		|| G[i][j+1] != '#' || G[i+1][j+1] != '#') return false;

	G[i][j] = '/';
	G[i][j+1] = '\\';
	G[i+1][j] = '\\';
	G[i+1][j+1] = '/';
	return true;
}

int main()
{
	int Te;
	cin >> Te;
	for(int te=0 ; te<Te  ; te++)
	{
		cout << "Case #"<<te+1 << ":\n";
		
		int M,N;
		char G[60][60];

		cin >> M >> N;
		for(int i=0 ; i<M ; i++)
			cin >> G[i];

		bool good = true;
		for(int i=0 ; i<M && good; i++)
		{
			for(int j=0 ; j<N && good; j++)
			{
				if(G[i][j] == '#' && !check(G,i,j,M,N))
					good = false;
			}
		}

		if(!good) cout << "Impossible\n";
		else
		{
			for(int i=0 ; i<M ; i++)
				cout << G[i] << endl;
		}
	}
}
