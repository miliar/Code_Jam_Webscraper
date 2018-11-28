#include<stdio.h>
#define MAXN 10005
int list[MAXN];
int main()
{
	int i,j,k,t,ca=1,n,l,f;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C1.txt","w",stdout);
	scanf("%d",&t);
	while(t--){
		scanf("%d%d%d",&n,&l,&f);
		for(i=0;i<n;i++)
			scanf("%d",&list[i]);
		for(k=l;k<=f;k++){
			for(i=0;i<n;i++){
				if(k%list[i]==0||list[i]%k==0);
				else
					break;
			}
			if(i==n){
				printf("Case #%d: %d\n",ca++,k);
				break;
			}
		}
		if(k>f){
			printf("Case #%d: NO\n",ca++);
		}
	}
	return 0;
}