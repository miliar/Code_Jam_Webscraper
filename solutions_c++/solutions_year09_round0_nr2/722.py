#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <fstream>
#include <cassert>
#include <memory.h>

using namespace std;


int t,h,w;
int a[111][111];

int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};
char ans[111][111];
int was[111][111];

int main()
{
	freopen("nut.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for (int i=0;i<t;i++)
	{
		scanf("%d%d",&h,&w);
		for (int j=0;j<h;j++)
			for (int g=0;g<w;g++)
				scanf("%d",a[j]+g);
		memset(was,0,sizeof(was));
		int kot=1;
		for (int j=0;j<h;j++)
			for (int g=0;g<w;g++)
				if (!was[j][g])
				{
					queue< int > q;
					q.push(j*1000+g);
					was[j][g]=kot++;
					int rx=j;
					int ry=g;
					for (;1;)
					{
						int zx,zy,vol=10000000;
						for (int d=0;d<4;d++)
						{
							int nx=rx+dx[d];
							int ny=ry+dy[d];
							if (nx<h&&nx>=0&&ny<w&&ny>=0&&a[nx][ny]<a[rx][ry]&&a[nx][ny]<vol)
							{
								zx=nx;
								zy=ny;
								vol=a[nx][ny];
							}
						}
						if (vol==10000000)
						{
							break;
						}
						else
						{
							if (was[zx][zy])
							{
								for (;!q.empty();)
								{
									rx=q.front()/1000;
									ry=q.front()%1000;
									was[rx][ry]=was[zx][zy];
									q.pop();
								}
								break;
							}
							else
							{
								was[zx][zy]=was[rx][ry];
								rx=zx;
								ry=zy;
								q.push(zx*1000+zy);
							}
						}
					}
				}
		map< int , char > mp;
		char ee='a';
		for (int f=0;f<h;f++)
			for (int j=0;j<w;j++)
			{
				if (mp.find(was[f][j])==mp.end())
					mp[was[f][j]]=ee++;
				ans[f][j]=mp[was[f][j]];
			}
		printf("Case #%d:\n",i+1);
		for (int j=0;j<h;j++,printf("\n"))
			for (int f=0;f<w;f++)
				printf("%c ",ans[j][f]);
	}
	return 0;
}