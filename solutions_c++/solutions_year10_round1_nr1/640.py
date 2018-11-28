#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

char mp0[100][100];
char mp1[100][100];
int n, K;

int dx[] = {1, -1, 1, -1};
int dy[] = {1, -1, -1, 1};

bool Inside(int x, int y)
{
	return x>=0 && x<n && y>=0 && y<n;
}

int main()
{
	freopen("A-large.in", "r", stdin);
//	freopen("1-small.out", "w", stdout);
	freopen("1-large.out", "w", stdout);
	int test, cas = 1;
	cin>>test;
	while(test--)
	{
		
		cin >> n >> K;
		int i, len, j;
		char buf[1000];
		for(i=0; i<n; i++)
		{
			scanf("%s", buf);
			len = n;
			for(j=0; j<n; j++) mp0[i][j] = buf[j];
		}

		for(i=0; i<n; i++)
		{
			for(j=0; j<n; j++)
			{
				mp1[i][j] = mp0[n-j-1][i];
			}
		}

		//for(i=0; i<n; i++)
		//{
		//	for(j=0; j<n; j++)
		//	{
		//		cout << mp1[i][j] << " ";
		//	}cout << endl;
		//}

		for(i=0; i<n; i++)
		{
			for(int k=0; k<n; k++)
			{
				for(j=n-2; j>=0; j--) if(mp1[j+1][i] == '.')
				{
					mp1[j+1][i] = mp1[j][i];
					mp1[j][i] = '.';
				}
			}
		}

		//for(i=0; i<n; i++)
		//{
		//	for(j=0; j<n; j++)
		//	{
		//		cout << mp1[i][j] << " ";
		//	}cout << endl;
		//}

		int x, y;

		bool hasRed = false, hasBlue = false;
		int rCt = 0, bCt = 0;
		for(i=0; i<n; i++)
		{
			for(j=0; j<n; j++)
			{
				rCt = 0, bCt = 0;
				if(mp1[i][j] == 'R')
				{
					x = i; y = j;
					while(Inside(x, y))
					{
						if(mp1[x][y] == 'R') rCt++;
						else break;
						y ++;
					}
				}
				if(mp1[i][j] == 'B')
				{
					x = i; y = j;
					while(Inside(x, y))
					{
						if(mp1[x][y] == 'B') bCt++;
						else break;
						y ++;
					}
				}
				if(rCt>=K) hasRed = true;
				if(bCt>=K) hasBlue = true;
			}
		}

		//cout << hasBlue << " " << hasRed << endl;

		for(i=0; i<n; i++)
		{
			for(j=0; j<n; j++)
			{
				rCt = 0, bCt = 0;
				if(mp1[i][j] == 'R')
				{
					x = i; y = j;
					while(Inside(x, y))
					{
						if(mp1[x][y] == 'R') rCt++;
						else break;
						x --;
					}
				}
				if(mp1[i][j] == 'B')
				{
					x = i; y = j;
					while(Inside(x, y))
					{
						if(mp1[x][y] == 'B') bCt++;
						else break;
						x--;
					}
				}
				if(rCt>=K) hasRed = true;
				if(bCt>=K) hasBlue = true;
			}
		}

			//cout << hasBlue << " " << hasRed << endl;

		for(i=0; i<n; i++)
		{
			for(j=0; j<n; j++)
			{
				if(mp1[i][j] == 'R')
				{
					for(int k=0; k<4; k++)
					{
						x = i; y = j;
						rCt = 0;
						while(Inside(x, y))
						{
							if(mp1[x][y] == 'R') rCt ++;
							else break;
							x = x + dx[k];
							y = y + dy[k];
						}
						if(rCt>=K)
						{
							//cout << i << " " << j << " " << k << endl;
							hasRed = true;
						}
					}
				}
				if(mp1[i][j] == 'B')
				{
					for(int k=0; k<4; k++)
					{
						x = i; y = j;
						bCt = 0;
						while(Inside(x, y))
						{
							if(mp1[x][y] == 'B') bCt ++;
							else break;
							x = x + dx[k];
							y = y + dy[k];
						}
						if(bCt>=K) hasBlue = true;
					}
				}
			}
		}


		cout << "Case #" << cas++ << ": ";
		if(hasRed && !hasBlue) cout << "Red\n";
		else if(hasBlue && !hasRed) cout <<"Blue\n";
		else if(hasRed && hasBlue) cout << "Both\n";
		else cout << "Neither\n";
	}
	return 0;
}