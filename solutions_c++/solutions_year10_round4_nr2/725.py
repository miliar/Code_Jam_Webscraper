#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

#define pb push_back
#define sz size()
#define MAXN 

void opens(){
	freopen("Bsmall.in","r",stdin);
	freopen("Bsmall.out","w",stdout);
}

void openb(){
	freopen("Blarge.in","r",stdin);
	freopen("Blarge.out","w",stdout);
}

int t,n,M[1030],coin[20][1030],sum;
int main(){
	opens();
	//openb();
	int xx=1;
	scanf("%d",&t);
	while (t--){
		scanf("%d",&n);
		for (int i=0;i<(1<<n);i++){
			scanf("%d",&M[i]);
		}
		sum=0;
		for (int i=n-1;i>=0;i--){
			for (int j=0;j<(1<<i);j++){
				scanf("%d",&coin[i][j]);
				sum+=coin[i][j];
			}
		}
		for (int i=1;i<=n;i++){
			for (int j=0;j<(1<<n);j++){
				if (j+(1<<i)-1>=(1<<n)) break;
				int mini=1000000000;
				for (int k=j;k<=j+(1<<i)-1;k++){
					mini=min(mini,M[k]);
				}
				if (mini){
					sum--;
					for (int k=j;k<=j+(1<<i)-1;k++){
						M[k]--;
					}
				}
				j+=(1<<i)-1;
			}
		}
		printf("Case #%d: %d\n",xx++,sum);
	}
	//system("pause");
	return 0;
}
