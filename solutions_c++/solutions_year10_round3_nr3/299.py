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


int M,N;
int grid[600][600];
int num[600][600];

bool checkcol(int r,int c)
{
	int n = num[r-1][c-1];
	int s = num[r][c];
	
	int cr=r-1,cc=c;
	while(cr>=0 && n && (s!=num[cr][cc]) && (num[cr][cc]!=num[cr][cc-1]))
	{
		s = num[cr][cc];
		cr--;
		n--;
	}

	return !n;
}

bool checkrow(int r,int c)
{
	int n = num[r-1][c-1];
	int s = num[r][c];
	
	int cr=r,cc=c-1;
	while(cc>=0 && n && (s == !num[cr][cc]) && (num[cr][cc] != num[cr-1][cc]))
	{
		s = num[cr][cc];
		cc--;
		n--;
	}

	return !n;
}

bool check(int r, int c,int n)
{
	for(int i=r ; i<r+n-1 ; i++)
	{
		for(int j=c ; j<c+n-1 ; j++)
		{
			if(grid[i][j] == -1) return 0;
			if(grid[i][j] != grid[i+1][j+1] || grid[i+1][j+1]==-1) return 0;
			if(grid[i][j] == grid[i+1][j] || grid[i+1][j]==-1) return 0;
			if(grid[i][j] == grid[i][j+1] || grid[i][j+1]==-1) return 0;

		}
	}
	return 1;
}

int largest()
{
	int n=min(M,N);

	while(n)
	{
		for(int i=0 ; (i+n-1)<M ; i++)
		{
			for(int j=0 ; (j+n-1)<N ; j++)
				if(grid[i][j] != -1 && check(i,j,n))
				{
					for(int l=0 ; l<n ; l++)
						for(int m=0 ; m<n ; m++)
							grid[i+l][j+m] = -1;
					return n;
				}
		}
		n--;
	}
	return n;
}

int main()
{
	int Te;
	cin >> Te;
	for(int te=0 ; te<Te  ; te++)
	{
		cout << "Case #"<<te+1 << ": ";
		cin >> M >> N;

		cin.ignore();

		for(int i=0 ; i<M ; i++)
		{
			string s;
			cin >> s;
			int j=0;
			for(int l=0 ; l<s.size() ; l++)
			{
				int n = s[l] - '0';
				if(n > 9) n = s[l]-'A'+10;

				for(int b=3 ; b>=0  ; b--,j++)
					grid[i][j] = (n&(1<<b))!=0;
			}
		}

		num[0][0] = 1;
		long long res[513]={0};
		long long sum=0;

		while(1)
		{
			int v = largest();
			if(v == 0) break;
			res[v]++;
		}

		for(int i=0 ; i<33 ; i++)
			if(res[i])
				sum++;
		
		/*for(int i=0 ; i<M ; i++)
		{
			for(int j=0  ; j<N ; j++)
			{	
				num[i][j] = 1;
				
				if(i>0 && j>0)
					if(grid[i-1][j-1] == grid[i][j] && checkcol(i,j) && checkrow(i,j))
						num[i][j] = num[i-1][j-1]+1;
					
				res[num[i][j]]++;
				
				int n = num[i][j]-1;
				while(n)
				{
					res[n]--;
					n--;
				}
			}
		}*/



		cout << sum << endl;
		for(int i=33 ; i>0 ; i--)
		 	if(res[i])
				 cout << i << " " << res[i] << endl;
	}
}
