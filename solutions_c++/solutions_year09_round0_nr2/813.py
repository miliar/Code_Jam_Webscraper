#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;

const int maxn= 200;

struct node {
	int xmin,ymin;
}g[maxn][maxn];

int h[maxn][maxn];
int n,m;
const int inf=1000000;
const int dx[]={-1,0,0,1};
const int dy[]={0,-1,1,0};

int mk[maxn][maxn];
char ans[maxn*maxn];
int parent[maxn*maxn],rank[maxn*maxn];
int find_set(int x){
	if( parent[x]!=x )parent[x]=find_set( parent[x]);
	return parent[x];
}
void union_set(int x,int y){
	x=find_set(x);y=find_set(y);
	if(x==y)return ;
	if( rank[x]<rank[y] )parent[x]=y;
	else {
		parent[y]=x;
		if(rank[x]==rank[y])rank[x]++;
	}
}

int ok(int x,int y){
	return (x>=1&&x<=n && y>=1 && y<=m );
}
void bfs(int x,int y){
	int i,j,k;
	queue<int>que;
	int nx,ny;
	que.push(x);que.push(y);
	while( !que.empty() ){
		int cx=que.front();que.pop();
		int cy=que.front();que.pop();
		if( mk[cx][cy] )continue ;
		mk[cx][cy]=1;
		int td,th=inf;
		for(i=0;i<4;i++){
			nx=cx+dx[i];
			ny=cy+dy[i];
			if( ok(nx,ny) && h[nx][ny]<h[cx][cy]){
				if( h[nx][ny]< th ){
					th=h[nx][ny];td=i;
				}
			}
		}

		if( th==inf )continue ;//bottom
		nx=cx+dx[ td ];
		ny=cy+dy[ td ];
		union_set(nx*m+ny,cx*m+cy);

		que.push(nx);que.push(ny);
		
	}
}

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int i,j,k,T;
	int nx,ny;
	scanf("%d",&T);
	for(int ca=1;ca<=T;ca++){
		printf("Case #%d:\n",ca);
		scanf("%d%d",&n,&m);
		memset(mk,0,sizeof(mk));
	
		for(i=1;i<=n;i++)for(j=1;j<=m;j++){
			scanf("%d",&h[i][j]);
			g[i][j].xmin = n+1;
			g[i][j].ymin = m+1;

			parent[i*m+j]=i*m+j;
			rank[i*m+j]=0;
		}

		for(i=1;i<=n;i++)for(j=1;j<=m;j++){
			int td,th=inf;
			for(k=0;k<4;k++){
				nx=i+dx[k];ny=j+dy[k];
				if( ok(nx,ny) ){
					if(h[nx][ny]>h[i][j] )break;					
				}
			}

			if( k<4 )continue ;//not the highest
			
			//cout<<i<<" "<<j<<endl;
			bfs(i,j);

			
			
		}

		for(i=1;i<=n;i++)for(j=1;j<=m;j++)bfs(i,j);

		memset(ans,0,sizeof(ans));
		char ch='a';
		for(i=1;i<=n;i++){
			for(j=1;j<=m;j++){
				k=find_set(i*m+j);
				if( ans[k]==0 )ans[k]=ch++;
			}
		}
		for(i=1;i<=n;i++){
			for(j=1;j<m;j++)printf("%c ",ans[ find_set(i*m+j) ]);
			printf("%c\n",ans[ find_set(i*m+j) ]);
		}

	}
}
