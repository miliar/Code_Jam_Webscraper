#include<stdio.h>
int a,b,c,n;
int main(){
	int _;
	scanf("%d",&_);
	for(int x=1; x<=_; x++){
		scanf("%d",&n);
		a=0,b=0,c=100000001;
		for(int i=0,t; i<n; i++)
		{
			scanf("%d",&t);
			if(t<c)c=t;
			a+=t;
			b^=t;
		}
		printf("Case #%d: ",x);
		if(b)puts("NO");else
			printf("%d\n",a-c);
	}
	return 0;
}
