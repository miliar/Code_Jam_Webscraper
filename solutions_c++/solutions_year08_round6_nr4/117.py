#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<set>
#include<map>
using namespace std;
int n,m,cnt,a[12],L[12],R[12];
bool g1[10][10],g2[10][10],v1[10],v2[10],found;

//void dfs(int x,int y){
//	if(found)return;
//	for(int i=1;i<=m&&!found;i++)
//		if(!v2[i]&&g2[x][i]){
//			v2[i]=1;
//			for(int j=1;j<=n&&!found;j++)
//				if(!v1[j]&&g1[y][j]){
//					v1[j]=1;
//					cnt++;
//					if(cnt==m)found=1;
//					dfs(i,j);
//					cnt--;
//					v1[j]=0;
//				}
//			v2[i]=0;
//		}
//}


void dfs(int d){
	if(d==m+1){
		for(int i=1;i<=m;i++)
			for(int j=i+1;j<=m;j++)
				if(g2[i][j]&&!g1[a[i]][a[j]])return;
		found=1;
		return;
	}
	for(int i=R[0];i!=n+1&&!found;i=R[i]){
		R[L[i]]=R[i],L[R[i]]=L[i],a[d]=i;
		dfs(d+1);
		R[L[i]]=L[R[i]]=i;
	}
}
int main(){
	freopen("D-small-attempt2.in","r",stdin);
	freopen("out.txt","w",stdout);
	
	int Tn;
	scanf("%d",&Tn);
	for(int Cn=1;Cn<=Tn;Cn++){
		scanf("%d",&n);
		memset(g1,0,sizeof(g1));
		memset(g2,0,sizeof(g2));
		for(int i=0;i<n-1;i++){
			int a,b;
			scanf("%d%d",&a,&b);
			g1[a][b]=1,g1[b][a]=1;
		}
		scanf("%d",&m);
		for(int i=0;i<m-1;i++){
			int a,b;
			scanf("%d%d",&a,&b);
			g2[a][b]=1,g2[b][a]=1;
		}
		found=0;
		for(int i=0;i<=n;i++){
			L[i+1]=i,R[i]=i+1;
		}
		dfs(1);
		printf("Case #%d: ",Cn);
		if(found)puts("YES");
		else puts("NO");
	}
	return 0;
}

