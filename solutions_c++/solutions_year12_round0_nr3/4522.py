#include <iostream>
#include <cstdio>

using namespace std;
int main(){
	int n,a,b,i,j,k,ans,m,num,num2,r,m2,num3;
	scanf("%d",&n);
	for(i=1;i<=n;i++){
		ans=0;
		scanf("%d %d",&a,&b);
		m=a;
		num=1;
		while(m>0){
			m/=10;
			if(m==0){break;}
			num*=10;
		}
		num2=num;
		for(j=a;j<=b;j++){
			num=num2;
			for(k=10;k<=j;k*=10){
				m=j/num+(j%num)*k;
				num/=10;
				if(m>=a&&j>m&&m<=b){
					num3=num2;
					for(r=10;r<=m;r*=10){
						m2=m/num3+(m%num3)*r;
						num3/=10;
						if(m2==j){ans++;break;}
					}
				}
			}
		}
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}
