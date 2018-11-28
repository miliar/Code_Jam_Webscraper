#include <iostream>
#include <vector>
using namespace std;

int h,w;
char grid[128][128];
int alt[128][128];
int sink[128][128];

int dx[] = {0,-1,1,0};
int dy[] = {-1,0,0,1};

int dfs(int x,int y){
	if(sink[y][x] != -1)
		return sink[y][x];
	int i,minH=1<<27,i2=-1;
	for(i=0;i<4;i++){
		int ny,nx;
		ny=y+dy[i];nx=x+dx[i];
		if(ny<0 || nx<0 || ny>=h || nx>=w)continue;
		if(alt[ny][nx]>=alt[y][x])continue;
		if(minH>alt[ny][nx])minH=alt[ny][nx],i2=i;
	}
	if(i2<0){
		return sink[y][x]=y*w+x;
	}
	return sink[y][x] = dfs(x+dx[i2],y+dy[i2]);
}

int main(){
	int cas,casIdx =0;
	cin >> cas;
	while(cas--){
		casIdx++;
		cin >> h >> w;
		int i,j;
		for(i=0;i<h;i++)for(j=0;j<w;j++)
			cin >> alt[i][j];
		memset(grid,'Z',sizeof grid);
		memset(sink,-1,sizeof sink);
		int cur=0;
		vector<int> list[128][128];
		for(i=0;i<h;i++)for(j=0;j<w;j++)
			list[i][j].clear();
		for(i=0;i<h;i++)for(j=0;j<w;j++)
			//if(dfs(j,i) != i*w+j)
				list[dfs(j,i)/w][dfs(j,i)%w].push_back(i*w+j);
		for(i=0;i<h;i++)for(j=0;j<w;j++)
			if(grid[i][j] == 'Z'){
				int k;
				for(k=0;k<list[dfs(j,i)/w][dfs(j,i)%w].size();k++)
					{
						int cy,cx;
						cy = list[dfs(j,i)/w][dfs(j,i)%w][k]/w;
						cx = list[dfs(j,i)/w][dfs(j,i)%w][k]%w;
						grid[cy][cx] = 'a' + cur;
					}
				cur++;
			}
		cout << "Case #" << casIdx << ":" << endl;
		for(i=0;i<h;i++){
			for(j=0;j<w-1;j++)
				cout << grid[i][j] << " ";
			cout << grid[i][j] << endl;
		}
	}
	return 0;
}
