#include<cstdio>
#include<cstring>
int r,c,n;
int map[105][105];
int mark[105][105],mk;
int dir[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};
int hasho[30];
int dfs(int rr,int cc) {
	int i,min=map[rr][cc],dd;
	if(mark[rr][cc])return mark[rr][cc];
	for(i=0;i<4;i++)
		if(rr+dir[i][0]>=0 && rr+dir[i][0]<r && cc+dir[i][1]>=0 && cc+dir[i][1]<c && map[rr+dir[i][0]][cc+dir[i][1]]<min) {
			min=map[rr+dir[i][0]][cc+dir[i][1]];
			dd=i;
		}
	if(min!=map[rr][cc])
		return mark[rr][cc]=dfs(rr+dir[dd][0],cc+dir[dd][1]);
	else
		return mark[rr][cc]=++mk;
}
int main() {
	//freopen("jam22.in","r",stdin);
	//freopen("jam22.out","w",stdout);
	scanf("%d",&n);
	int i,j,k,sst;
	for(i=0;i<n;i++) {
		scanf("%d %d",&r,&c);
		for(j=0;j<r;j++)
			for(k=0;k<c;k++) {
				scanf("%d",&map[j][k]);
				mark[j][k]=0;
			}
		mk=0;
		for(j=0;j<r;j++)
			for(k=0;k<c;k++) {
				if(!mark[j][k])
					dfs(j,k);
		}
		sst='a';
		for(j=0;j<26;j++) hasho[j]=0;
		for(j=0;j<r;j++)
			for(k=0;k<c;k++)
				if(!hasho[mark[j][k]])
					hasho[mark[j][k]]=sst++;
		printf("Case #%d:\n",i+1);
		for(j=0;j<r;j++,printf("\n"))
			for(k=0;k<c;k++)
				printf("%c ",hasho[mark[j][k]]);
			
	}
}
