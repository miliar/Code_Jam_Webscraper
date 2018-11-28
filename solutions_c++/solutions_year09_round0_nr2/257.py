#include<iostream>
#include<algorithm>
#define fo(i,u,d) for(int i=u;i<=d;i++)
using namespace std;
const int cc[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
int fa[10010],map[110][110],t1=1,tt,id[10010];
int n,m;

int find(int x){
	if (fa[x]!=x)
		fa[x]=find(fa[x]);
	return fa[x];
}

int main(){
	freopen("bl.in","r",stdin);
	freopen("b.out","w",stdout);
	for(scanf("%d",&tt);t1<=tt;t1++){
		scanf("%d%d",&n,&m);
		fo(i,0,n+1)fo(j,0,m+1)map[i][j]=10000000;
		fo(i,1,n)
			fo(j,1,m)
				scanf("%d",&map[i][j]);
		fo(i,1,n*m)fa[i]=i,id[i]=0;
		fo(i,1,n)
			fo(j,1,m){
				int t=0;
				fo(k,1,3)
					if (map[i+cc[k][0]][j+cc[k][1]]<map[i+cc[t][0]][j+cc[t][1]])
						t=k;
				if (map[i+cc[t][0]][j+cc[t][1]]<map[i][j])
					fa[find((i-1)*m+j)]=find((i+cc[t][0]-1)*m+j+cc[t][1]);
			}
		int now=0;
		fo(i,1,n)
			fo(j,1,m){
				if (id[find((i-1)*m+j)]==0)
		 			id[fa[(i-1)*m+j]]=++now;
		 		map[i][j]=id[fa[(i-1)*m+j]];
			}
		printf("Case #%d:\n",t1);
		fo(i,1,n){
			fo(j,1,m-1)
				printf("%c ",map[i][j]+96);
			printf("%c\n",map[i][m]+96);
		}		
	}
	return 0;
}
				
		
