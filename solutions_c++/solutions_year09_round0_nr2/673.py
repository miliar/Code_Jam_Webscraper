#include <vector>
#include <cstdio>
#include <set>
#include <map>
#include <ctime>
#include <string>
#include <sstream>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <cstring>
#include <cctype>
#include <queue>

#define inputfilename "input"
#define outputfilename "a.out"

using namespace std;

int mx[4] = {-1, 0, 0, 1};
int my[4] = { 0,-1, 1, 0};

int mat[200][200];
int a[200][200];
int n, m;

struct node
{
	int x, y ;
};

int search(int x, int y, int id)
{
	node first;
	first.x = x; first.y = y;
	queue<node> q;
	q.push(first);
	int i , j , l;
	while (!q.empty())
	{
		node now = q.front();
		q.pop();
		for (l = 0; l < 4; l++)
		{
			int x = now.x+mx[l];
			int y = now.y+my[l];
			if (x < 0 || x >= n || y < 0 || y >= m) continue;
			if (a[x][y] == -2) continue;
			if (a[x][y] + l != 3) continue;
			mat[x][y] = id;
			a[x][y] = -2;
			node wait;
			wait.x = x; wait.y = y;
			q.push(wait);
		}
	}
	return 0;
}

int main ()
{
	//freopen(inputfilename , "r" , stdin);
	/*freopen(outputfilename , "w" , stdout);*/

	int number , times;
	cin >> number;
	for (times = 0 ; times < number ; times++)
	{
		cin >> n >> m;
		int i, j, l;
		
		for (i = 0; i < n; i++)
		for (j = 0; j < m; j++)
		{
			cin >> mat[i][j];
		}

		for (i = 0 ; i < n ; i++)
		for (j = 0 ; j < m ;j++)
		{
			int id = -1, v = 20000;
			for (l = 0 ; l < 4; l++)
			{
				int x = i+mx[l];
				int y = j+my[l];
				if (x < 0 || x >= n || y < 0 || y >= m) continue;
				if (mat[i][j] <= mat[x][y]) continue;
				if (v > mat[x][y])
				{
					v = mat[x][y];
					id = l;
				}
			}
			a[i][j] = id;
		}
		
		int cnt = 0 ;
		for (i = 0 ; i < n ; i++)
		for (j = 0 ; j < m ; j++)
		{
			if (a[i][j] == -1)
			{
				mat[i][j] = cnt;
				a[i][j] = -2;
				search(i, j, cnt);
				cnt++;
			}
		}
		int  out[26];
		cnt = 0;
		memset(out, -1, sizeof(out));
		printf("Case #%d:\n" , times+1);
		for (i = 0 ; i < n ; i++)
		{
			for (j = 0 ; j < m ; j++)
			{
				int v = mat[i][j];
				if (out[v] == -1)
					out[v] = cnt++;
				char c = 'a'+out[v];
				putchar(c);
				if (j == m-1) putchar('\n');
				else putchar(' ');
			}
		}
	}


	return 0;
}

 
