#include<stdio.h>
#include<string.h>
int a[110][110],top;
int dx[]={-1,0,0,1},dy[]={0,-1,1,0};
struct node{
	int x,y;
	node*next;
}edge[40010],*list[110][110];
char res[110][110],now;
void dfs(int x,int y) {
	for (node*p=list[x][y];p;p=p->next) 
		if (res[p->x][p->y]==0) {
		res[p->x][p->y]=now;
		dfs(p->x,p->y);
	}
}
int main()
{
	int nn,n,m;
	freopen("B-large.in","r",stdin);
	freopen("b-large.out","w",stdout);
	scanf("%d",&nn);
	for (int ii=1;ii<=nn;ii++) {
		scanf("%d%d",&n,&m);
		memset(a,0x7f,sizeof(a));
		memset(res,0,sizeof(res));
		top=0;
		memset(list,0,sizeof(list));
		for (int i=1;i<=n;i++) for (int j=1;j<=m;j++) scanf("%d",a[i]+j);
		for (int i=1;i<=n;i++) for (int j=1;j<=m;j++) {
			int ans=0x7f7f7f7f,sit;
			for (int k=0;k<4;k++) if (ans>a[i+dx[k]][j+dy[k]]) {
				sit=k;
				ans=a[i+dx[k]][j+dy[k]];
			}
			if (ans!=0x7f7f7f7f&&a[i+dx[sit]][j+dy[sit]]<a[i][j]) {
				edge[++top].x=i+dx[sit];
				edge[top].y=j+dy[sit];
				edge[top].next=list[i][j];
				list[i][j]=edge+top;
				
				edge[++top].x=i;
				edge[top].y=j;
				edge[top].next=list[i+dx[sit]][j+dy[sit]];
				list[i+dx[sit]][j+dy[sit]]=edge+top;
			}
		}
		now='a';
		for (int i=1;i<=n;i++) for (int j=1;j<=m;j++) if (res[i][j]==0) {
			res[i][j]=now;
			dfs(i,j);
			now++;
		}
		printf("Case #%d:\n",ii);
		for (int i=1;i<=n;i++) {
			for (int j=1;j<m;j++) printf("%c ",res[i][j]);
			printf("%c\n",res[i][m]);
		}
	}
}
