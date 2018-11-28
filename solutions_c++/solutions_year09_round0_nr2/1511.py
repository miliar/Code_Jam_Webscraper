#include<string>
#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;

const int Max = 100;

struct pair1
{
	int x, y;
};

ifstream fin("qualround2.in");
ofstream fout("qualround2.out");

const int walk[4][2] = {{-1, 0},{0, -1},{0, 1},{1, 0}};

int T, H, W;
pair1 father[Max][Max];
int grid[Max][Max];
pair1 list[Max*Max], next[Max][Max];
char ans[Max][Max];

bool valid(int x, int y)
{
	if (x<0 || y<0 || x>=H || y>=W) return 0;
	return 1;
}

pair1 findfather(int x, int y)
{
	pair1 k;
	k.x = x;
	k.y = y;
	if (father[x][y].x == -1) return k;
	pair1 t = findfather(father[x][y].x, father[x][y].y);
	father[x][y].x = t.x;
	father[x][y].y = t.y;
	return t;
}

int main()
{
	fin>>T;
	for (int i=1;i<=T ;i++ )
	{
		fin>>H>>W;
		int max = 0;
		for (int a=0;a<H ;a++ )
		{
			for (int b =0;b<W ;b++ )
			{
				fin>>grid[a][b];
				father[a][b].x = father[a][b].y = -1;
				if (grid[a][b]>max)
				{
					 max = grid[a][b];
				}
			}
		}

		for (int k = 0;k<=max ;k++ )
		{
			list[k].x = list[k].y = -1;
		}
		for (int a=0;a<H ;a++ )
		{
			for (int b =0;b<W ;b++ )
			{
					int t= grid[a][b];
					next[a][b].x = list[t].x;
					next[a][b].y = list[t].y;
					list[t].x = a;
					list[t].y = b;
			}
		}

		for (int k=max;k>=0 ;k-- )
		{
			int x = list[k].x, y = list[k].y;
			while (x!=-1)
			{
				int na = -1, nb = -1, nc = 100000;
				for (int p=0;p<4 ;p++ )
				{
					int a = x + walk[p][0], b = y + walk[p][1];
					if (valid(a, b) && grid[a][b]<k && grid[a][b]<nc)
					{						
						na = a;
						nb = b;
						nc = grid[a][b];	
					}
				}
				if (na != -1)
				{
						pair1 n1 = findfather(na,nb);
						pair1 n2 = findfather(x,y);
						
						father[n2.x][n2.y].x = n1.x;
						father[n2.x][n2.y].y = n1.y;
				}

				int t= x;
				x = next[t][y].x;
				y = next[t][y].y;
			}
		}

		char limit = 'a';

		for (int a=0;a<H ;a++ )
		{
			for (int b =0;b<W ;b++ )
			{
				ans[a][b] = '0';
			}
		}
		fout<<"Case #"<<i<<":"<<endl;

		for (int a=0;a<H ;a++ )
		{
			for (int b =0;b<W ;b++ )
			{
				pair1 t = findfather(a, b);
				if (ans[t.x][t.y]=='0')
					ans[t.x][t.y] = limit++;

				fout<<ans[t.x][t.y]<<' ';
			}
			fout<<endl;
		}
	}


	return 0;
}
