#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<queue>
#include<cstring>
using namespace std;
int main(void){
	freopen("C:\\C-large.in", "r", stdin);
	freopen("C:\\ans.out", "w", stdout);
	int cst;
	scanf("%d",&cst);
	int th;
	for(th=1;th<=cst;th++){
		int r,k,n;
		int i,j,t,w;
		scanf("%d%d%d",&r,&k,&n);
		int biglv[1001];
		for(i=0;i<n;i++) scanf("%d",biglv+i);
		int num[1001],id[1001];
		for(i=0;i<n;i++) num[i]=0;
		for(i=0;i<n;i++){
			j=0,w=0,t=i;
			if(biglv[i]>k) {
				num[i]=0;
				id[i]=i;
				continue;
			}
			int tmp=0;
			while(j<n&&w<=k){
				tmp=biglv[t++];
				w+=tmp;
				if(t==n) t=0;
				j++;
			}
			num[i]=w;
			if(w>k) num[i]=w-tmp;
			id[i]=t-1;
			if(id[i]<0) id[i]+=n;
		}
		i=0;
		__int64 ans=0;
		while(r--){
			ans+=(__int64)num[i];
			i=id[i];
		}
		printf("Case #%d: %I64d\n",th,ans);
	}
	return 0;
}