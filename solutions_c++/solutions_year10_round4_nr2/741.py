#include<cstdio>
const int N=10;
int a[1<<N],b[1<<N];
int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int i,j,k,p,q,t,tt=1;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&p);
		for(i=0;i<(1<<p);i++){
			scanf("%d",&a[i]);
			a[i]=p-a[i];
		}
		for(i=p-1;i>=0;i--)
			for(j=0;j<(1<<i);j++)
				scanf("%d",&b[j]);
		q=0;
		for(i=p;i>0;i--)
			for(j=0;j<(1<<(p-i));j++){
				for(k=j*(1<<i);k<(j+1)*(1<<i);k++)
					if(a[k]>0){
						q++;
						for(;k<(j+1)*(1<<i);k++)
							if(a[k]>0)a[k]--;
					}
			}
				
		printf("Case #%d: %d\n",tt++,q);
	}
	return 0;
}
