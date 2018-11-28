#include <cstdio>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <functional>
#include <vector>

using namespace std;
int n,m;
int M[101][26];
int E[101][101];
int u[101][101];
int c[101];



int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,Q,i,j,ans;
	scanf("%d",&Q);
	for(T=1;T<=Q;T++){
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				scanf("%d",&M[i][j]);
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				E[i][j]=0;
		for(i=0;i<n;i++)
			for(j=i+1;j<n;j++){
				int e=0;
				for(int k=0;k<m;k++)
					if(M[i][0]-M[j][0]>0 && M[i][k]-M[j][k]<0 ||
						M[i][0]-M[j][0]<0 && M[i][k]-M[j][k]>0 || M[i][k]-M[j][k]==0)
						e=1;
				if(e)E[i][j]=E[j][i]=1;
			}
		ans=0;
		for(int b=0;b<(1<<n);b++){
			int z=1;
			for(i=0;i<n;i++)
				for(j=i+1;j<n;j++)
					if((b&(1<<i))>0 && (b&(1<<j))>0 && E[i][j]==0)z=0;
			if(z){
				z=0;
				for(i=0;i<n;i++)if(b&(1<<i))z++;
				if(ans<z)ans=z;
			}
		}
		printf("Case #%d: %d\n",T,ans);
	}
	return 0;
}
