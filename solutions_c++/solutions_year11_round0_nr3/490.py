#include <stdio.h>
int c[1010];
int min(int a,int b){return a<b?a:b;}
int main(int argc, const char *argv[])
{
	int times;
	scanf("%d",&times);
	for(int tm=1;tm<=times;tm++){
		int n;
		scanf("%d",&n);
		int top=0,sum=0,xorsum=0,m=0x11111111;
		for(int i=0;i<n;i++){
			scanf("%d",&c[i]);
			sum+=c[i];
			xorsum^=c[i];
			m=min(m,c[i]);
		}
		printf("Case #%d: ",tm);
		if(xorsum){
			printf("NO\n");
		} else {
			printf("%d\n",sum-m);
		}
	}
	return 0;
}
