#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<ctime>
#include<cassert>
using namespace std;
#define y1 fndjifhwdn
#define ws vfsdkofsjd
#define fs first
#define sc second
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pi;
const int inf=(int)1e9;
int a[1000][1000];
int b[1000][1000];
int obs[1000][1000];

int next[10000];
int head[10000];
int e[10000];
int s[10000];
int deg[10000];
int gd[10000];
int dp[10000];
int n,m,kl,x,y,ans,r;
vector<pi> v;
void add(int x,int y){
	kl++;
	next[kl]=head[x];
	head[x]=kl;
	e[kl]=y;
	s[kl]=x;
}
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	int tt;
    scanf("%d",&tt);
    for (int ti=0;ti<tt;ti++){
    	//cerr<<ti<<endl;
    	printf("Case #%d: ",ti+1);
    	kl=0;
    	memset(head,0,sizeof(head));
    	memset(next,0,sizeof(head));
    	memset(deg,0,sizeof(deg));
    	memset(gd,0,sizeof(gd));
    	memset(b,0,sizeof(b));
    	memset(dp,0,sizeof(dp));
    	memset(obs,0,sizeof(obs));
    	scanf("%d %d",&n,&m);
    	for (int i=0;i<n;i++)
			for (int j=0;j<n;j++) if (i!=j)
				a[i][j]=inf;
			else 
				a[i][j]=0;
    	for (int i=0;i<m;i++){
    		scanf("%d,%d ",&x,&y);
    		add(x,y);
    		add(y,x);
    		deg[x]++;
    		deg[y]++;
    		a[x][y]=1;
    		a[y][x]=1;
    	}
    	for (int k=0;k<n;k++)
    	for (int i=0;i<n;i++)
    	for (int j=0;j<n;j++)
    	if (a[i][j]>a[i][k]+a[k][j]){
    		a[i][j]=a[i][k]+a[k][j];
    	}
    	for (int i=0;i<n;i++)
	    	for (int j=0;j<n;j++)
			   	for (int k=0;k<n;k++)if (k!=i && k!=j){
	   				if (a[i][k]==1 && a[k][j]==1){
			   			obs[i][j]++;
	   				}
	   			}
    	for (int i=0;i<n;i++){
    		if (a[0][i]+a[i][1]==a[0][1]){
    			gd[i]=1;
    		//	cerr<<i<<endl;
    		} else
    			gd[i]=0;
    	}
    	v.clear();
		for (int i=1;i<=kl;i++){
			if (gd[s[i]]==1 && gd[e[i]]==1 && a[0][s[i]]+1==a[0][e[i]] && e[i]!=1){
				v.pb(mp(a[0][s[i]],i));
			//	cerr<<s[i]<<" "<<e[i]<<endl;
				b[s[i]][e[i]]=i;
			}
		}
	   //	cerr<<endl;
		sort(v.begin(),v.end());
		ans=0;
		for (int i=0;i<(int)v.size();i++){
			r=v[i].sc;
			if (s[r]==0){
				dp[r]=deg[0]+deg[e[r]]-obs[0][e[r]]-2;
			}
		//	cerr<<s[r]<<" "<<e[r]<<" "<<dp[r]<<endl;
			for (int j=0;j<n;j++) if (b[e[r]][j]!=0){
				dp[b[e[r]][j]]=max(dp[b[e[r]][j]],dp[r]+deg[j]-obs[e[r]][j]-2-obs[s[r]][j]+1);
			}
			if (a[0][e[r]]==a[0][1]-1){
				ans=max(ans,dp[r]);
			}
		}
    	printf("%d ",a[0][1]-1);
    	if (a[0][1]==1) printf("%d",deg[0]);
    			   else printf("%d",ans);
    	printf("\n");
    }
    return 0;
}









