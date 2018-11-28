#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
using namespace std;
#define ll long long
#define ull unsigned long long
#define mp(X,Y) make_pair(X,Y)
#define pb(X) push_back(X)
#define sz(X) (int)X.size()
#define clr(X) memset(X,0,sizeof(X))
#define klr(X) memset(X,-1,sizeof(X))
#define pii pair<int,int>

	int adj[110][110];
	double wp[110];
	double owp[110];
	double oowp[110];

	
int main(){
	int casos;
	scanf("%d",&casos);

	for(int caso=1;caso<=casos;caso++){
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				char c;
				scanf(" %c",&c);
				if(c=='0')adj[i][j]=0;
				else if (c=='1')adj[i][j]=1;
				else adj[i][j]=-1;
				//printf("%d ",adj[i][j]);
			}
			//printf("\n");
		}
		for(int i=0;i<n;i++){
			wp[i]=0.0;
			int q=0;
			for(int j=0;j<n;j++)
				if(adj[i][j]!=-1){
				//	printf("adj[%d][%d]=%d\n",i,j,adj[i][j]);
					if(adj[i][j]==1)wp[i]+=1;
					q++;
				}
		//	printf("antes wp[i]:%.5f q:%d\n",wp[i],q);
			wp[i]/=q;
			//printf("wp[%d] = %.5f\n",i,wp[i]);
		}
		for(int i=0;i<n;i++){
			owp[i]=0;
			int q2=0;
			for(int j=0;j<n;j++){
				if(adj[i][j]==-1)continue;
				q2++;
				double ewp =0.0;
				int q=0;
				for(int k=0;k<n;k++){
					if(k!=i){
						if(adj[j][k]!=-1)q++;
						if(adj[j][k]==1)
						ewp+=1.0;
					}
				}
				ewp/=q;
				owp[i]+=ewp;
			}
			owp[i]/=q2;
		//	printf("owp[%d] = %.5f\n",i,owp[i]);
		}
		for(int i=0;i<n;i++){
			oowp[i]=0;
			int q2=0;
			for(int j=0;j<n;j++){
				if(adj[i][j]==-1)continue;
				oowp[i]+=owp[j];
				q2++;
			}
			oowp[i]/=q2;
			//printf("oowp[%d] = %.5f\n",i,oowp[i]);
		}
		printf("Case #%d:\n",caso);
		for(int i=0;i<n;i++){
			printf("%.12f\n",0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
		}
	}	
	return 0;
}

