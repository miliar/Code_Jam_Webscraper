#include <iostream>
#include <cstdio>

using namespace std;

int g[2040];

int main()
{
	__int64 sum=0;
	freopen("C-small-attempt2.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T,H;
	int R,k,n,i,vl;
	scanf("%d",&T);
	for(H=1;H<=T;H++){
		scanf("%d%d%d",&R,&k,&n);
		for(i=1;i<=n;i++){
			scanf("%d",&g[i]);
			g[n+i-1]=g[i];
		}
		sum=0;
		for(i=1;i<=n;i++)sum+=g[i];
		if(sum<=k){sum*=R;printf("Case #%d: %I64d\n",H,sum);continue;}
		
		vl=0;
		int kol=0,j=1;
		sum=0;
		for(i=1;i<=R;i++){
			kol=0;
			while((kol+g[j])<=k){
				kol+=g[j];
				j++;
				if(j>n)j=1;
			}
			sum+=kol;
			kol=0;
		}
		printf("Case #%d: %I64d\n",H,sum);
	}
	return 0;
}
