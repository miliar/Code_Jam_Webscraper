#include<stdio.h>
using namespace std;
int t,n,l,h,gcd;
int player[100];
int main(){
	scanf("%d",&t);
	for(int I=1;I<=t;++I){
		scanf("%d%d%d",&n,&l,&h);
		for(int i=0;i<n;++i)
			scanf("%d",&player[i]);
			
		
		int i=l;
		for(;i<=h;++i){
			int j=0;
			for(;j<n;++j)
				if(i%player[j] !=0 && player[j]%i != 0)
					break;
				if(j==n) break;
		}
		if(i<=h) printf("Case #%d: %d\n",I,i);
		else printf("Case #%d: NO\n",I);
		
	}
	return 0;
}
