#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <iterator>
#include <bitset>
#include <sstream>
#include <cmath>
#include <cstring>

using namespace std;

int p,n,a[4444],val[4444],opt[4444][11];

void dfs(int cur,int dep){
	if (dep==p){
		opt[cur][a[cur]]=0;
		//cout <<"#"<< cur <<" "<< a[cur] <<endl;
		//for (int i=0;i<=p;i++) cout << opt[cur][i] << " ";puts("");
		return;
	}
	dfs(cur*2,dep+1);
	dfs(cur*2+1,dep+1);
	for (int i=0;i<=p;i++)
		for (int j=0;j<=p;j++){
			int t=min(i,j);
			opt[cur][t]=min(opt[cur*2][i]+opt[cur*2+1][j]+val[cur],opt[cur][t]);
			if (t) opt[cur][t-1]=min(opt[cur*2][i]+opt[cur*2+1][j],opt[cur][t-1]);
		}
	//cout <<"#"<< cur <<endl;
	//for (int i=0;i<=p;i++) cout << opt[cur][i] << " ";puts("");
	return;
}

void work(){
	cin >> p;
	n=(1<<p);
	for (int i=n;i<2*n;i++) scanf("%d",&a[i]);
	for (int i=n-1;i>=1;i--) scanf("%d",&val[i]);
	for (int i=1;i<=p;i++){
		reverse(val+(1<<i),val+(1<<(i+1)));
	}
	memset(opt,0xf,sizeof(opt));
	dfs(1,0);
	int ans=2147480000;
	for (int i=0;i<=p;i++) ans=min(ans,opt[1][i]);
	cout << ans <<endl;
}

int main(){
	//freopen("test.in","r",stdin);
	//freopen("test.out","w",stdout);
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int t;cin >> t;
	for (int i=1;i<=t;i++){
		printf("Case #%d: ",i);
		work();
	}
	//system("pause");
	return 0;
}
