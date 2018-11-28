#include <cstdio>
#include <queue>
#include <string>
#include <set>
using namespace std;
int dx[] = {-1,0,1,0};
int dy[] = {0,1,0,-1};
int a[301][301];
int now=0;
set<pair<pair<int,int>,pair<int,int>>> s;
bool go(int nowx, int nowy){
	memset(a,0,sizeof(a));
	a[nowx][nowy]=1;
		queue<pair<int,int>>q;
		q.push(make_pair(nowx,nowy));
		while(!q.empty()){
			pair<int,int> temp = q.front();
			int x=temp.first;
			int y=temp.second;
			if(x<=10 || y<=10 || x>=270 || y>=270)
				return false;
			q.pop();
			if(s.find(make_pair(make_pair(x,y),make_pair(x-1,y)))==s.end() && a[x][y-1]==0){
				a[x][y-1] = 1;
				q.push(make_pair(x,y-1));
			}
			if(s.find(make_pair(make_pair(x-1,y),make_pair(x-1,y+1)))==s.end() && a[x-1][y]==0){
				a[x-1][y] = 1;
				q.push(make_pair(x-1,y));
			}
			if(s.find(make_pair(make_pair(x-1,y+1),make_pair(x,y+1)))==s.end() && a[x][y+1]==0){
				a[x][y+1] = 1;
				q.push(make_pair(x,y+1));
			}
			if(s.find(make_pair(make_pair(x,y),make_pair(x,y+1)))==s.end() && a[x+1][y]==0){
				a[x+1][y] = 1;
				q.push(make_pair(x+1,y));
			}
		}
		return true;
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d\n",&t);
	for(int tc=1; tc<=t; tc++){
		string x = "";
		int n;
		scanf("%d\n",&n);
		for(int i=1; i<=n; i++){
			char t1[100];
			int t2;
			scanf("%s %d ",t1,&t2);
			for(int j=1; j<=t2; j++)
				x += t1;
		}
		now=0;
		int nowx,nowy;
		nowx=150;
		nowy=150;
		s.clear();
		int minx,maxx,miny,maxy;
		minx=maxx=miny=maxy=nowx;
		for(int i=0; i<x.size(); i++){
			if(x[i]=='R'){
				now++;
				if(now==4)
					now=0;
			}
			else if(x[i]=='L'){
				now--;
				if(now==-1)
					now=3;
			}
			else{
				s.insert(make_pair(make_pair(nowx,nowy),make_pair(nowx+dx[now],nowy+dy[now])));
				s.insert(make_pair(make_pair(nowx+dx[now],nowy+dy[now]),make_pair(nowx,nowy)));
				nowx+=dx[now];
				nowy+=dy[now];
				minx=min(minx,nowx);
				maxx=max(maxx,nowx);
				miny=min(miny,nowy);
				maxy=max(maxy,nowy);
			}
		}
		memset(a,0,sizeof(a));
		if(!go(150,150))
			if(!go(151,150))
				if(!go(150,149))
					go(151,149);
		
		int cnt=0;
		for(int i=minx; i<=maxx; i++){
			for(int j=miny; j<=maxy; j++){
				if(a[i][j]==1)
					continue;
				bool ok = false;
				bool ok2 = false;
				nowx=i;
				nowy=j;
				while(nowx>=0){
					if(a[nowx][nowy]==1){
						ok=true;
						break;
					}
					nowx--;
				}
				nowx=i;
				while(nowx<=300){
					if(a[nowx][nowy]==1){
						ok2=true;
						break;
					}
					nowx++;
				}
				if(ok && ok2){
					cnt++;
				}
				else{
					bool ok3 = false;
					bool ok4 = false;
					nowx=i;nowy=j;
					while(nowy>=0){
						if(a[nowx][nowy]==1){
							ok3=true;
							break;
						}
						nowy--;
					}
					nowy=j;
					while(nowy<=300){
						if(a[nowx][nowy]==1){
							ok4=true;
							break;
						}
						nowy++;
					}
					if(ok3 && ok4)
						cnt++;
				}
			}
		}
		printf("Case #%d: %d\n",tc,cnt);
	}
	return 0;
}