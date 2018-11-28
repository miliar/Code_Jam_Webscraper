#include <iostream>
#include<cstring>
#include <cstdio>
#include <vector>
using namespace std;

int map[110][110];
int nmap[110][110];
char ans[110][110];
bool mark[110][110];
int dir[][2] = {-1, 0, 0, -1, 0, 1, 1, 0};
struct Point
{
	int x, y;
};
int R, C;
vector<Point> drain;
vector<int> alt;

bool ok(int x, int y)
{
	if(x < 0 || x >= R) return false;
	if(y < 0 || y >= C) return false;
	return true;
}

void getDrain()
{
	for(int i = 0; i < R; i++)
	{
		for(int j = 0; j < C; j++)
		{
			bool isok = true;
			int tmp = map[i][j];
			for(int k = 0; k < 4; k++)
			{
				int x = i + dir[k][0];
				int y = j + dir[k][1];
				if(!ok(x, y)) continue;
				if(map[x][y] < tmp) {
					isok = false;
					break;
				}
			}
			if(isok) 
			{
				Point p;
				p.x = i;
				p.y = j;
				drain.push_back(p);
				nmap[i][j] = drain.size()-1000000;
			}
		}
	}
}

int search(int r, int c)
{
	int x, y;
	mark[r][c] = true;
	if(nmap[r][c] < 0)
	{
		return nmap[r][c];
	}
	int tmp = map[r][c];
	int tx, ty;
	tx = -1;
	ty = -1;
	for(int i = 0; i < 4; i++)
	{
		x = r + dir[i][0];
		y = c + dir[i][1];
		if(!ok(x, y)) continue;
		//if(mark[x][y]) continue;
		if(map[x][y] < tmp)	
		{
			tmp = map[x][y];
			tx = x;
			ty = y;
		}
	}
	if(tx == -1 || ty == -1) 
	{
		cout<<"error"<<endl;
	}
	mark[tx][ty] = true;
	nmap[r][c] = search(tx, ty);
	return nmap[r][c];
}

void getAns(int r, int c, char ch)
{
	ans[r][c] = ch;
	mark[r][c] = true;
	int x, y;
	for(int i = 0; i < 4; i++)
	{
		x = r + dir[i][0];
		y = c + dir[i][1];
		if(!ok(x, y)) continue;
		if(mark[x][y]) continue;
		if(nmap[r][c] == nmap[x][y]) getAns(x, y, ch);
	}
}

int main()
{
	int tcase = 1;
	int N, i, j;
	//while(cin>>N)
	freopen("blin.txt", "r", stdin);
	freopen("blout.txt", "w", stdout);
	scanf("%d", &N);
	{
		
		for(int tcase = 1; tcase <= N; tcase++)
		{
			drain.clear();
			scanf("%d%d", &R, &C);
			memset(nmap, 0, sizeof(nmap));
			for( i = 0; i < R; i++)
			{
				for( j = 0; j < C; j++)
				{
					scanf("%d", &map[i][j]);
				}
			}
			getDrain();
			/*for( i = 0; i < drain.size(); i++)
			{
				cout<<drain[i].x<<" "<<drain[i].y<<endl;
			}*/
			memset(mark, false, sizeof(mark));
			char ch = 'a'-1;
			for(i = 0; i < R; i++)
			{
				for(j = 0; j < C; j++)
				{
					if(mark[i][j]) continue;
					mark[i][j] = true;
					nmap[i][j] = search(i, j);
				}
			}
/*
			for(i = 0; i < R; i++)
			{
				for(j = 0; j < C; j++)
				{
					cout<<nmap[i][j]<<" ";
				}
				cout<<endl;
			}*/
			memset(ans, 0, sizeof(ans));
			memset(mark, false, sizeof(mark));
			for( i = 0; i < R; i++)
			{
				for( j = 0; j < C; j++)
				{
					if(mark[i][j]) continue;
					ch++;
					getAns(i, j, ch);
				}
			}
			cout<<"Case #"<<tcase<<":"<<endl;
			for( i = 0; i < R; i++)
			{
				for( j = 0; j < C; j++)
				{
					if(!j) printf("%c", ans[i][j]);
					else printf(" %c", ans[i][j]);
				}
				printf("\n");
			}
		}
	}
	return 0;
}
