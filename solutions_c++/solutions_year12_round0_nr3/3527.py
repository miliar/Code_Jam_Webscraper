#include<stdio.h>
int main()
{
	int t,i,j;
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		int a,b,s,m=0,n=1,c=0;
		scanf("%d%d",&a,&b);
		s=a;
		printf("Case #%d: ",i);
		while(s!=0){
			s/=10;
			m++;
		}
		for(int i=1;i<=m;i++)
			n*=10;
		for(j=a;j<=b;j++){
			int v=10;
			while(v<n){
				
				s=(j%v)*(n/v)+j/v;
				
				if((s>j&&s<=b)){
					c++;
//				printf("%d\n",j);
				}
				v*=10;
			}
		}
		printf("%d\n",c);
	}
	return 0;
}
