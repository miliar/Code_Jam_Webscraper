#include<cstdio>
const int N=100;
const int dx[4]={-1,0,0,1};
const int dy[4]={0,-1,1,0};
int g[N][N],mark[N][N],f[N*N],n,m,test;
int findfa(int x){
	return f[x]==-1?x:(f[x]=findfa(f[x]));
}
void merge(int x,int y){
	int a=findfa(x),b=findfa(y);
	if (a!=b)
		f[a]=b;
	return;
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&test);
	for (int testnum=1;testnum<=test;testnum++){
		printf("Case #%d:\n",testnum);
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++){
				scanf("%d",&g[i][j]);
				mark[i][j]=-1;
				f[i*m+j]=-1;
			}
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++){
				int fa=-1,fah;
				for (int k=0;k<4;k++){
					int x=i+dx[k],y=j+dy[k];
					if (x>=0 && x<n && y>=0 && y<m && g[x][y]<g[i][j] && (fa==-1 || fah>g[x][y]))
						fa=x*m+y,fah=g[x][y];
				}
				if (fa!=-1)merge(fa,i*m+j);
			}
		int countnum=0;
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++){
				int k=findfa(i*m+j);
				if (mark[k/m][k%m]==-1)
					mark[k/m][k%m]=countnum++;
				mark[i][j]=mark[k/m][k%m];
			}
		for (int i=0;i<n;i++){
			for (int j=0;j<m-1;j++)
				printf("%c ",mark[i][j]+'a');
			printf("%c\n",mark[i][m-1]+'a');
		}
	}
	return 0;
}
