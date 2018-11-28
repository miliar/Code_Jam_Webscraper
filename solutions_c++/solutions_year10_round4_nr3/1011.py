#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int table[101][101];
int dx[2] = {-1,0};
int dy[2] = {0,-1};

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int tests;
	scanf("%d",&tests);
	for(int t=1;t<=tests;++t)
	{
		memset(table,0,sizeof(table));
		printf("Case #%d: ",t);
		int n; scanf("%d",&n);
		for(int i=0;i<n;++i)
		{
			int x1,y1,x2,y2;
			scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
			--x1;
			--y1;
			--x2;
			--y2;
			for(int y=y1;y<=y2;++y)
			{
				for(int x=x1;x<=x2;++x)
				{
					table[y][x] = 1;
				}
			}
		}
		int cnt = 0;
		while(true){
			bool bFlag = false;
			vector<pair<int,int> > p;
			vector<pair<int,int> > po;
			for(int i=0;i<100;++i)
			{
				for(int j=0;j<100;++j)
				{
					int scnt = 0;
					for(int k=0;k<2;++k){
						int nx = j + dx[k];
						int ny = i + dy[k];
						if(nx < 0 || ny < 0){
							++scnt;
							continue;
						}
						if(table[ny][nx] == 0){
							++scnt;
						}
					}
					if(scnt == 0){
						if(table[i][j] == 0){
							p.push_back(make_pair(i,j));
							bFlag = true;
						}
					}
					if(scnt == 2){
						if(table[i][j] == 1){
							po.push_back(make_pair(i,j));
							bFlag = true;
						}
					}
				}
			}
			if(!bFlag){
				break;
			}
			++cnt;

			for(int m=0;m<p.size();++m)
			{
				table[p[m].first][p[m].second] = 1;
			}
			for(int pp=0;pp<po.size();++pp)
			{
				table[po[pp].first][po[pp].second] = 0;
			}
		}
		printf("%d\n",cnt);
	}
	return 0;
}