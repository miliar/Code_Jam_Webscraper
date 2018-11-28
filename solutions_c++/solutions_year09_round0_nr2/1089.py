#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
int map[102][102];
char ans[102][102];
int h,w;
int dx[4]={-1,0,0,1};
int dy[4]={0,-1,1,0};
bool _link(int x1,int y1,int x2,int y2){
	bool r=false;
	int min_a=map[x1][y1];
	for(int i=0;i<4;++i){
		int x=x1+dx[i];
		int y=y1+dy[i];
		if(map[x][y]<min_a){
			min_a=map[x][y];
			if(x==x2 && y==y2)
				r=true;
			else
				r=false;
		}
	}
	return r;
}
bool link(int x1,int y1,int x2,int y2){
	if(map[x1][y1]>10000 || map[x2][y2]>10000)
		return false;
	return _link(x1,y1,x2,y2) || _link(x2,y2,x1,y1);
}
void dfs(int x,int y,char z){
	ans[x][y]=z;
	for(int i=0;i<4;++i){
		int xx=x+dx[i];
		int yy=y+dy[i];
		if(ans[xx][yy]==0 && link(x,y,xx,yy))
			dfs(xx,yy,z);
	}
}
int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;++i){
		cout<<"Case #"<<i<<":"<<endl;
		cin>>h>>w;
		memset(map,1,sizeof(map));
		memset(ans,0,sizeof(ans));
		for(int i=1;i<=h;++i)
			for(int j=1;j<=w;++j)
				cin>>map[i][j];
		char top='a';
		for(int i=1;i<=h;++i)
			for(int j=1;j<=w;++j){
				if(ans[i][j]==0)
					dfs(i,j,top++);
				cout<<ans[i][j]<<(j==w?'\n':' ');
			}
	}
	return 0;
}
