#include<iostream>
#define fo(i,u,d) for(int i=u;i<=d;i++)
using namespace std;
int t1=1,tt,n,m,id;
int d[210][30],s,t;
int g[210][210],f[210][210],v[210];

void add(int x,int y){
	 g[x][++g[x][0]]=y;
	 g[y][++g[y][0]]=x;
	 f[x][y]=1;
	 f[y][x]=0;
}

bool dfs(int x){
	 if (x==t)
	 	return true;
	 v[x]=id;
	 fo(i,1,g[x][0])
	 	if ((f[x][g[x][i]])&&(v[g[x][i]]<id))
	 		if (dfs(g[x][i])){
				f[x][g[x][i]]=false;
				f[g[x][i]][x]=true;
				return true;
			}
	 return false;
}

int main(){
	freopen("cl.in","r",stdin);
	freopen("c.out","w",stdout);
	for(scanf("%d",&tt);t1<=tt;t1++){
		scanf("%d%d",&n,&m);
		s=n+n+1;t=s+1;	
		fo(i,1,t)v[i]=g[i][0]=0;
		fo(i,1,n)
			fo(j,1,m)
				scanf("%d",&d[i][j]);
		fo(i,1,n)
			fo(j,1,n){
				bool ok=true;
				fo(k,1,m)
					if (d[j][k]>=d[i][k]){
						ok=false;
						break;
					}
				if (ok)
					add(i,j+n);
			}
		fo(i,1,n){
			add(s,i);
			add(i+n,t);
		}
		id=1;
		while (dfs(s))
			id++;
		printf("Case #%d: %d\n",t1,n-(id-1));
	}
	return 0;
}
			
					
					
					
						
				
			
