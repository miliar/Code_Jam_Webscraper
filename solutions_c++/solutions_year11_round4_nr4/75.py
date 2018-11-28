#include<iostream>
#include<stdio.h>
#include<vector>
#include<string.h>
#define fr(i,a,b) for(i=a;i<=b;++i)
using namespace std;
const int maxn=1002;
int i,j,k,a,b,n,m,ans,ti,ca,g[maxn][maxn],f[maxn][maxn];
vector<int> d[maxn];
int cal(int a,int b){
	if(f[a][b]>=0)
		return f[a][b];
	if(b==1){
//		cout<<a<<" "<<b<<" "<<d[a].size()<<endl;
		return f[a][b]=d[a].size();
	}
	int c,i;
	bool u[500];
	fr(c,0,n-1)
		if(g[b][c]==1&&g[b][1]==g[b][c]+g[c][1]){
			memset(u,0,sizeof(u));
			u[b]=true;
			u[c]=true;
			fr(i,0,(int)d[b].size()-1)
				u[d[b][i]]=true;
			if(c!=1)
				fr(i,0,(int)d[c].size()-1)
					u[d[c][i]]=true;
			int tmp=cal(b,c)-1;
			fr(i,0,(int)d[a].size()-1)
				if(!u[d[a][i]]){
					tmp++;
//					cout<<a<<" "<<d[a][i]<<endl;
				}
			if(f[a][b]<tmp)
				f[a][b]=tmp;
		}
//	cout<<a<<" "<<b<<" "<<f[a][b]<<endl;
	return f[a][b];
}
int main(){
	freopen("d2.in","r",stdin);
	freopen("d2.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		cin>>n>>m;
		fr(i,0,n-1)
			fr(j,0,n-1)
				g[i][j]=(i==j?0:1000000000);
		fr(i,0,n-1)
			d[i].clear();
		while(m--){
			scanf("%d,%d",&a,&b);
			g[a][b]=g[b][a]=1;
			d[a].push_back(b);
			d[b].push_back(a);
		}
		fr(k,0,n-1)
			fr(i,0,n-1)
				fr(j,0,n-1)
					g[i][j]=min(g[i][j],g[i][k]+g[k][j]);
		memset(f,255,sizeof(f));
		ans=0;
		fr(i,0,n-1)
			if(g[0][i]==1&&g[i][1]==g[0][1]-1)
				ans=max(ans,cal(0,i));
		cout<<"Case #"<<ti<<": "<<g[0][1]-1<<" "<<ans<<endl;
	}
}