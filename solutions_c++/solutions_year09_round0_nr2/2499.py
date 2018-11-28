#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cstring>
#include <cfloat>
using namespace std;

typedef pair<int, int> node;

char alpha;
int visited[101][101];
int table[101][101];
char ans[101][101];
int dd[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};
int rev[4][2] = {{1,0},{0,1},{0,-1},{-1,0}};

int main(void){
    int ts, h, w;
    
    freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);

    scanf("%d",&ts);
	for(int tt=0;tt<ts;tt++){
		alpha = 'a';
		memset(ans,0,sizeof(ans));
		memset(table,0,sizeof(table));
		scanf("%d %d",&h,&w);

		for(int i=0;i<h;i++){
			for(int j=0;j<w;j++){
				scanf("%d",&table[i][j]);
			}
		}

		for(int i=0;i<h;i++){
			for(int j=0;j<w;j++){
				if(!ans[i][j]){
					memset(visited,0,sizeof(visited));
					queue<node> q;
					q.push(node(i,j));
					visited[i][j] = -1;

					while(!q.empty()){
						node top = q.front();
						q.pop();
						int m = table[top.first][top.second], mI=-1;
						for(int ii=0;ii<4;ii++){
							if(top.first+dd[ii][0] >= 0 && top.first+dd[ii][0] < h &&
								top.second+dd[ii][1] >= 0 && top.second+dd[ii][1] < w &&
								!visited[top.first+dd[ii][0]][top.second+dd[ii][1]]){
									if(m > table[top.first+dd[ii][0]][top.second+dd[ii][1]]){
										m = table[top.first+dd[ii][0]][top.second+dd[ii][1]];
										mI = ii;
									}
							}
						}
						if(mI == -1){
							node temp;
							temp.first = top.first;
							temp.second = top.second;
							while(visited[temp.first][temp.second] != -1){
								int fuck = visited[temp.first][temp.second];
								ans[temp.first][temp.second] = (int)alpha;
								temp.first += rev[ fuck ][0];
								temp.second += rev[ fuck ][1];
							}
							ans[temp.first][temp.second] = (int)alpha;
							visited[temp.first][temp.second] = 1;
							alpha += 1;
						}else if(mI != -1 && !ans[top.first+dd[mI][0]][top.second+dd[mI][1]]){
							node temp;
							temp.first = top.first+dd[mI][0];
							temp.second = top.second+dd[mI][1];
							visited[temp.first][temp.second] = mI;
							q.push(temp);
						}else if(mI != -1 && ans[top.first+dd[mI][0]][top.second+dd[mI][1]]){
							int haha = ans[top.first+dd[mI][0]][top.second+dd[mI][1]];
							node temp;
							temp.first = top.first;
							temp.second = top.second;
							while(visited[temp.first][temp.second] != -1){
								int fuck = visited[temp.first][temp.second];
								ans[temp.first][temp.second] = haha;
								temp.first += rev[ fuck ][0];
								temp.second += rev[ fuck ][1];
							}
							ans[temp.first][temp.second] = haha;
							visited[temp.first][temp.second] = 1;
						}
					}
				}
			}
		}
		printf("Case #%d:\n",tt+1);
		for(int i=0;i<h;i++){
			for(int j=0;j<w;j++){
				printf("%c ",(char)ans[i][j]);
			}
			puts("");
		}
	}
    return 0;
}