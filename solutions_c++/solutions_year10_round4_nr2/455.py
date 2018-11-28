#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <complex> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
using namespace std;

const int inf=1000000000;
int a[1<<20];
int opt[1<<12][12];
int main(){
	int T,cas=0;
	scanf("%d",&T);
	while(T--){
		int p;
		scanf("%d",&p);
		int n=1<<p;
		for(int i=0;i<n;i++)
			scanf("%d",a+n+i);
		for(int i=p-1;i>=0;i--){
			for(int j=0;j<1<<i;j++)
				scanf("%d",a+(1<<i)+j);
		}
		for(int i=0;i<n+n;i++)
			for(int j=0;j<=p;j++)
				opt[i][j]=inf;
		for(int i=0;i<n;i++)
			opt[n+i][a[n+i]]=0;
		for(int i=n-1;i>=1;i--){
			for(int l=0;l<=p;l++)
				for(int r=0;r<=p;r++){
					if(opt[i*2][l]==inf||opt[i*2+1][r]==inf)
						continue;
					opt[i][min(l,r)]=min(opt[i][min(l,r)],opt[i*2][l]+opt[i*2+1][r]+a[i]);
					if(l>=1&&r>=1)
						opt[i][min(l,r)-1]=min(opt[i][min(l,r)-1],opt[i*2][l]+opt[i*2+1][r]);
				}
		}
		int minv=inf;
		for(int i=0;i<=p;i++)
			minv=min(minv,opt[1][i]);
		printf("Case #%d: %d\n",++cas,minv);
	}
}
