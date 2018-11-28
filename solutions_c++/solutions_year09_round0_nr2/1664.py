#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <set>
#include <limits>
#include <map>
#include <cmath>
#include <numeric>
using namespace std;

#define pb push_back
#define REP(i,n) for(int i=0; i<(n); ++i)   
#define ALL(X) (X).begin(),(X).end()
#define present(c,x) ((c).find(x) != (c).end())
typedef long long ll;
template<class T>inline int sz(T& x){return (int)x.size();}
int stoi(string a){int len=sz(a);if(len==1)return a[0]-'0';return a[len-1]-'0'+10*stoi(a.substr(0,len-1));}
template<class T>inline string tostring(T& i){ostringstream oss; oss << i; return oss.str();}
template <class T> void make_unique(T& v){sort(ALL(v)); v.resize(unique(ALL(v)) - v.begin());}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int test; scanf("%d",&test);
	int table[101][101];
	int map[101][101];
	for(int tt=1;tt<=test;tt++)
	{
		int h,w; scanf("%d %d",&h, &w);
		memset(table,-1,sizeof(table));
		int area = 0;
		table[0][0] = area;
		for(int i=0;i<h;i++)
			for(int j=0;j<w;j++)
				scanf("%d",&map[i][j]);
		int dx[4] = {0,1,-1,0};
		int dy[4] = {1,0,0,-1};
		//0 1 2 3
		for(int y=0;y<h;y++)
		{
			for(int x=0;x<w;x++)
			{
				int lx = -1,ly = -1,llow = map[y][x];
				for(int k=0;k<4;k++)
				{
					int gx = x + dx[k];
					int gy = y + dy[k];
					if(gx < 0 || gx >= w) continue;
					if(gy < 0 || gy >= h) continue;
					if(llow >= map[gy][gx] && map[y][x] > map[gy][gx]){
						llow = map[gy][gx];
						lx = gx;
						ly = gy;
					}
				}
				if(lx == -1 && ly == -1)
				{
					if(table[y][x] == -1)table[y][x] = ++area;
					continue;
				}
				if(table[y][x] == -1 && table[ly][lx] == -1)
				{
					table[ly][lx] = table[y][x] = ++area;
				}
				else if(table[y][x] != -1 && table[ly][lx] == -1)
				{
					table[ly][lx] = table[y][x];
				}
				else if(table[y][x] == -1 && table[ly][lx] != -1)
				{
					table[y][x] = table[ly][lx];
				}
				else if(table[y][x] != -1 && table[ly][lx] != -1)
				{
					deque<pair<int,int> > q;
					int tar;
					int ori;
					if(table[y][x] < table[ly][lx])
					{
						tar = table[y][x];
						ori = table[ly][lx];
						q.push_back(make_pair(ly,lx));
					}
					else
					{
						tar = table[ly][lx];
						ori = table[y][x];
						q.push_back(make_pair(y,x));
					}
					while(!q.empty())
					{
						pair<int,int> res = q.front(); q.pop_front();
						table[res.first][res.second] = tar;
						for(int k=0;k<4;k++)
						{
							int gy = res.first + dx[k];
							int gx = res.second + dy[k];
							if(gx < 0 || gx >= w) continue;
							if(gy < 0 || gy >= h) continue;
							if(table[gy][gx] == ori)
							{
								q.push_back(make_pair(gy,gx));
							}
						}
					}
				}
			}
		}
		int res = 0;
		int up = 27;
		for(int i=0;i<h;i++)
			for(int j=0;j<w;j++)
			{
				if(table[i][j] > res + 1)
				{
					res++;
					up++;
					int ori = table[i][j];
					for(int y=0;y<h;y++)
						for(int x=0;x<w;x++)
						{
							if(table[y][x] == res)
								table[y][x] = up;
							else if(table[y][x] == ori)
								table[y][x] = res;
						}
				}
			}
		printf("Case #%d:\n",tt);
		for(int y=0;y<h;y++)
		{
			for(int x=0;x<w;x++)
			{
				printf("%c",table[y][x]+ 97);
				if(x != w-1) printf(" ");
			}
			printf("\n");
		}
	}
	return 0;
} 