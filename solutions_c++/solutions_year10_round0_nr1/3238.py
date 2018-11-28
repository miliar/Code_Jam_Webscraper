#include <stdio.h>

int main(void){

	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);

	int T = 0;
	scanf("%d",&T);
	
	long n=0,k=0,m=1;
	for(int i=0;i<T;i++){	
		scanf("%d %d",&n,&k);
		m = 0;
		for(int j=0;j<n;j++,m=(m<<1)+1);
		printf("Case #%d: %s\n",i+1,(k&m) == m && m >0? "ON" : "OFF");
	}
}
