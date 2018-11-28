#include<stdio.h>
#include<math.h>

int gcd(int x,int y){
	if(y==0)return x;
	if(x==0)return y;
	int r=x%y;
	while(r){
		x=y;
		y=r;
		r=x%y;
	}
	return y;
}

int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int t,n,i,j,a,c,b,ans;
	scanf("%d",&t);
	for(i=1;i<=t;++i){
		scanf("%d",&n);
		if(n==2){
			scanf("%d%d",&a,&b);
			ans=abs(a-b);
		}
		else{
			scanf("%d%d%d",&a,&b,&c);
			int x=gcd(abs(a-b),abs(a-c));
			ans=gcd(x,abs(b-c));
		}
		if( ans==1 )ans=0;
		else if( a%ans==0)ans=0;
		else ans=ans-(a%ans);
		printf("Case #%d: %d\n",i,ans );
	}
	return 0;
}

