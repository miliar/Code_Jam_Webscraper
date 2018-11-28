#include<cstdio>
#include<cstring>

int L,D,N,vis[5007];
char s[5007][20],c,t,ans;

int main()
{
	scanf("%d%d%d",&L,&D,&N);
	for (int i=0;i<D;++i) scanf("%s",s+i);
	for (int i=0;i<N;++i){
		memset(vis,0,sizeof(vis));ans=0;
		for (int j=0;j<L;++j){
			do c=getchar(); while (c<=' ');
			if (c=='('){
				t=getchar();
				while (t!=')'){
					for (int k=0;k<D;++k) if (s[k][j]==t) ++vis[k];
					t=getchar();
				}
			}else
				for (int k=0;k<D;++k) if (s[k][j]==c) ++vis[k];
		}
		for (int j=0;j<D;++j) if (vis[j]==L) ++ans;
		printf("Case #%d: %d\n",i+1,ans);
	}
	return 0;
}

