

#include <iostream>
#include <string>
#include <cassert>
#include <queue>
using namespace std;

const int MX = 105;
const int MX2=MX*2;

int walls[MX2][MX2];
bool inner[MX2][MX2];
int visited[MX2][MX2];

const int nDir[][2]={
	{1,0},
	{0,1},
	{-1,0},
	{0,-1}
};

const int xdi[][2]={
	{-1,0},
	{0,-1},
	{1,0},
	{0,1}
};

void floodfill(int r,int c,int col)
{
	queue<pair<int,int> > que;
	visited[r][c] = col;
	que.push(make_pair(r,c));
	while(que.size()){
		pair<int,int> now = que.front();
		que.pop();
		for(int k=0;k<4;++k){
			if( (1<<k)& walls[now.first][now.second] )
				continue;
			pair<int,int> nx(now.first+xdi[k][0],now.second+xdi[k][1]);
			if( nx.first < 0 || nx.second >= MX2 || visited[nx.first][nx.second] >= 0 )
				continue;
			visited[nx.first][nx.second] = col;
			que.push(nx);
		}
	}
}

int main()
{
	int n;
	cin>>n;
	for(int tc=1;tc<=n;++tc)
	{
		int L;
		cin>>L;
		int nr=MX,nc=MX;
		int nk=0;
		memset(walls,0,sizeof walls);
		for(int i=0;i<MX2;++i){
			walls[0][i] |= 1;
			walls[MX2-1][i] |= (1<<2);
			walls[i][0] |= (1<<1);
			walls[i][MX2-1] |= (1<<3);
		}

		for(int k=0;k<L;++k){
			string s;
			int t;
			cin>>s>>t;
			const int sz = (int)s.size();
			for(int p=0;p<t;++p){
				for(int q=0;q<sz;++q){
					const char ch = s[q];
					switch(ch)
					{
					case 'F':
						do{
							switch(nk)
							{
							case 0:
								walls[nr][nc]   |= (1<<1);
								walls[nr][nc-1] |= (1<<3);
								break;
							case 1:
								walls[nr][nc]  |= 1;
								walls[nr-1][nc]|= (1<<2);
								break;
							case 2:
								walls[nr-1][nc] |= (1<<1);
								walls[nr-1][nc-1]|=(1<<3);
								break;
							case 3:
								walls[nr][nc-1]   |= 1;
								walls[nr-1][nc-1] |= (1<<2);
								break;
							default:
								assert(0);
								break;
							}
							nr+=nDir[nk][0];
							nc+=nDir[nk][1];
						}while(0);
						break;
					case 'R':
						nk=(nk+1)%4;
						break;
					case 'L':
						nk=(nk+3)%4;
						break;
					}
				}
			}//~

			queue<pair<int,int> > que;
			memset(visited,-1,sizeof visited);
			int color = 0;
			if( visited[MX][MX] < 0 ){
				floodfill(MX,MX,color);
				++color;
			}
			if( visited[MX-1][MX] < 0 ){
				floodfill(MX-1,MX,color);
				++color;
			}
			if( visited[MX][MX-1] < 0 ){
				floodfill(MX,MX-1,color);
				++color;
			}
			if( visited[MX-1][MX-1] < 0){
				floodfill(MX-1,MX-1,color);
				++color;
			}
			//~
		}//~ end k
		const int bdColor = visited[0][0];
		int ans = 0;
		for(int i=0;i<MX2;++i){
			for(int j=0;j<MX2;++j){
				if( bdColor == visited[i][j] )
				{
					bool ok = false;
					bool upper = false;
					int xr=i,xc=j;
					while(!upper && xr<MX2-1 ){
						if( walls[xr][xc]&(1<<2) ){
							upper = true;
							break;
						}
						++xr;
					}
					if( upper ){
						bool lower = false;
						int xr = i,xc = j;
						while(!lower&&xr>0){
							if( walls[xr][xc]&1 ){
								lower = true;
								break;
							}
							--xr;
						}
						if(lower){
							++ans;
							ok=true;
						}
					}

					if(!ok)
					{
						bool left = false;
						int xr=i,xc=j;
						while(!left && xc>0 ){
							if( walls[xr][xc]&(1<<1) ){
								left = true;
								break;
							}
							--xc;
						}
						if( left )
						{
							bool right = false;
							int xr=i,xc=j;
							while(!right&& xc<MX2-1 ){
								if(walls[xr][xc]&(1<<3)){
									right = true;
									break;
								}
								++xc;
							}
							if(right){
								++ans;
							}
						}
					}
				}
			}
		}//~
		cout<<"Case #"<<tc<<": ";
		cout<<ans<<endl;
	}
}