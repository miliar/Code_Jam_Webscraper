#include<iostream>
#define fr(i,a,b) for(i=a;i<=b;++i)
using namespace std;
const int maxn=102;
int h[maxn][maxn],i,j,ca,ti,n,m;
bool g[maxn][maxn][4];
char ans[maxn][maxn],now;
void dfs(int a,int b,char c){
	if(ans[a][b])
		return;
	ans[a][b]=c;
	if(g[a][b][0])
		dfs(a-1,b,c);
	if(g[a][b][1])
		dfs(a,b-1,c);
	if(g[a][b][2])
		dfs(a,b+1,c);
	if(g[a][b][3])
		dfs(a+1,b,c);
}
void build(int a,int b){
	int mi=1<<30;
	if(a>1&&h[a-1][b]<mi)
		mi=h[a-1][b];
	if(b>1&&h[a][b-1]<mi)
		mi=h[a][b-1];
	if(b<m&&h[a][b+1]<mi)
		mi=h[a][b+1];
	if(a<n&&h[a+1][b]<mi)
		mi=h[a+1][b];
	if(mi>=h[a][b])
		return;
	if(a>1&&h[a-1][b]==mi){
		g[a][b][0]=g[a-1][b][3]=true;
		return;
	}
	if(b>1&&h[a][b-1]==mi){
		g[a][b][1]=g[a][b-1][2]=true;
		return;
	}
	if(b<m&&h[a][b+1]==mi){
		g[a][b][2]=g[a][b+1][1]=true;
		return;
	}
	if(a<n&&h[a+1][b]==mi)
		g[a][b][3]=g[a+1][b][0]=true;
}
int main(){
	freopen("b2.in","r",stdin);
	freopen("b2.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		cin>>n>>m;
		fr(i,1,n)
			fr(j,1,m)
				cin>>h[i][j];
		memset(g,0,sizeof(g));
		fr(i,1,n)
			fr(j,1,m)
				build(i,j);
		memset(ans,0,sizeof(ans));
		now='a';
		fr(i,1,n)
			fr(j,1,m)
				if(!ans[i][j])
					dfs(i,j,now++);
		cout<<"Case #"<<ti<<":"<<endl;
		fr(i,1,n){
			fr(j,1,m-1)
				cout<<ans[i][j]<<" ";
			cout<<ans[i][m]<<endl;
		}
	}
}
