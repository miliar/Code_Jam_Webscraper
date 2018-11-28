#include<stdio.h>
#include<string.h>
bool s[110][110],falg;
char str[110][110];
int a[110][110],h,w;
int op[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
void dfs(int x,int y,int c){
	int b[4][3],i,j,n,m,min,x1,y1;
	for(j=i=0;i<4;++i){
		x1=x+op[i][0];
		y1=y+op[i][1];
		if(x1>=0&&x1<h&&y1>=0&&y1<w){
			b[j][0]=a[x1][y1];
			b[j][1]=x1;
			b[j++][2]=y1;
		}
	}
	m=j;
	for(min=2147483647,i=0;i<m;++i){
		if(b[i][0]<min){min=b[i][0];j=i;}
	}
	x1=b[j][1];
	y1=b[j][2];
	if(min<a[x][y]){
		if(s[x1][y1])falg=false;
		else {
			dfs(x1,y1,c);
			s[x1][y1]=true;
		}
	}
	if(falg)str[x][y]=c;
	else str[x][y]=str[x1][y1];
}
int main(){
	int t,i,j,k,x;
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	scanf("%d",&t);
	for(k=1;k<=t;++k){
		scanf("%d%d",&h,&w);
		for(i=0;i<h;++i)
			for(j=0;j<w;++j)
				scanf("%d",&a[i][j]);
		memset(s,false,sizeof(s));
		for(x='a',i=0;i<h;++i){
			for(j=0;j<w;++j){
				if(!s[i][j]){
					falg=true;
					s[i][j]=true;
					dfs(i,j,x);
					if(falg)++x;
				}
			}
		}
		printf("Case #%d:\n",k);
		for(i=0;i<h;++i){
			printf("%c",str[i][0]);
			for(j=1;j<w;++j)
				printf(" %c",str[i][j]);
			printf("\n");
		}
	}
	return 0;
}