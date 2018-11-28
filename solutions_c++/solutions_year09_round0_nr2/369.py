#include<all>
int a[110][110];
char ans[110][110];
int n,m;
int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};
int inside(int x,int y){
	return x>=0 && y>=0&& x<n&&y<m;
}
pair<int,int> dest(int x,int y){
	int ans=100000;
	for(int i=0; i<4; i++){
		if(inside(x+dx[i],y+dy[i])){
			if(a[x][y]>a[x+dx[i]][y+dy[i]])
				ans=min(ans,a[x+dx[i]][y+dy[i]]);
		}
	}
	if(ans==100000)
		return make_pair(x,y);
	for(int i=0; i<4; i++){
		if(inside(x+dx[i],y+dy[i]))
			if(ans==a[x+dx[i]][y+dy[i]]){
				return dest(x+dx[i],y+dy[i]);
			}
	}
	cerr<<"xxx";
	return make_pair(0,0);
}
int main(){
	int rr;
	cin >> rr;
	for(int kase=1; kase<=rr; kase++){
		memset(a,0,sizeof a);
		memset(ans,0,sizeof ans);
		cin >> n >> m;
		for(int i=0; i<n; i++){
			for(int j=0; j<m; j++){
				cin >> a[i][j];
			}
		}
		cout<<"Case #"<<kase<<":"<<endl;
		char now='a';
		for(int i=0; i<n; i++){
			for(int j=0; j<m; j++){
				pair<int,int> destij=dest(i,j);
				if(ans[destij.first][destij.second]==0){
					ans[destij.first][destij.second]=now;
					now++;
				}
				cout<<ans[destij.first][destij.second];
				if(j==m-1)
					cout<<endl;
				else
					cout<<" ";
			}
		}
	}
}

