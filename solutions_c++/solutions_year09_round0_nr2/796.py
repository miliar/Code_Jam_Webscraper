#include <iostream>
#include <vector>
#include <deque>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <functional>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <utility>
#include <memory>
#include <sstream>

using namespace std;

struct pos
{
	int x,y;
};

int sink[101][101],height[101][101],dir[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};

int main()
{
//	freopen("D:\\VC project\\ForTest\\Debug\\input.in","r",stdin);
//	freopen("D:\\VC project\\ForTest\\Debug\\out.txt","w",stdout);
	int x,h,w,no,i,j,cnt,ans,colorCnt;
	pos next,cur,minPos,path[10001];
	cin >> x;
	for(no = 1;no <= x;no++)
	{
		cin >> h >> w;
		for(i = 0;i < h;i++) for(j = 0;j < w;j++) scanf("%d",&height[i][j]);
		memset(sink,-1,sizeof(sink));
		colorCnt = -1;
		for(i = 0;i < h;i++) for(j = 0;j < w;j++)
		{
			if(sink[i][j] != -1) continue;
			cnt = 1,path[0].x = i,path[0].y = j,cur.x = i,cur.y = j;
			while(1)
			{
				minPos.x = cur.x,minPos.y = cur.y;
				for(int d = 0;d < 4;d++)
				{
					if((next.x = cur.x + dir[d][0]) >= 0 && next.x < h && (next.y = cur.y + dir[d][1]) >= 0 && next.y < w)
					{
						if(height[next.x][next.y] < height[minPos.x][minPos.y]) minPos.x = next.x,minPos.y = next.y;
					}
				}
				if(minPos.x == cur.x && minPos.y == cur.y) 
				{
					ans = ++colorCnt;
					for(int i1 = 0;i1 < cnt;i1++) sink[path[i1].x][path[i1].y] = ans;
					break;
				}
				cur.x = path[cnt].x = minPos.x,cur.y = path[cnt].y = minPos.y;
				if(sink[cur.x][cur.y] != -1)
				{
					ans = sink[cur.x][cur.y];
					for(int i1 = 0;i1 < cnt;i1++) sink[path[i1].x][path[i1].y] = ans;
					break;
				}
				cnt++;
			}
		}
		cout << "Case #" << no << ":" << endl;
		for(i = 0;i < h;i++) 
		{
			for(j = 0;j < w - 1;j++) printf("%c ",'a' + sink[i][j]);
			printf("%c\n",'a' + sink[i][w - 1]);
		}
	}
	return 0;
}