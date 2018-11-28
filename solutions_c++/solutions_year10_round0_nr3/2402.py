#include <stdio.h>
#include <memory>

unsigned __int64 a[1001];

int main()
{
	//freopen("z:\\a.out","w",stdout);
	//freopen("z:\\0.in","r",stdin);
	unsigned __int64 sum,c,i,r,k,k1,j,n,x,y,z;
	int sign;
	scanf("%I64u",&c);
	for(i=1;i<=c;++i){
		scanf("%I64u%I64u%I64u",&r,&k,&n);
		for(j=0;j<n;++j){
			scanf("%I64u",&a[j]);
		}
		sum=0;
		y=z=0;
		for(j=1;j<=r;++j){
			k1=0;sign=0;
			for(;;){
				if(z==y&&sign==0){
					sign=1;
				}
				else if(z==y&&sign==1){
					break;
				}
				if(k1+a[z]>k) break;
				//k1+a[x]<=k	
				k1+=a[z];
				z=(++z)%n;
			}
			sum+=k1;
			y=z;
		}
		printf("Case #%I64u: %I64u\n",i,sum);
	}
	
	return 0;
}