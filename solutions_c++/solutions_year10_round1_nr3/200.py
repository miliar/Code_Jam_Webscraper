#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

long t,a1,a2,b1,b2;

bool ask(long i,long j){
	if(j>0 && i/j>1)return 1;
	if(j==0)return 1;
	return (i/j==1)^(ask(j,i%j));
}

int main(){
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	long h,i,j,k,ans;
	scanf("%ld",&t);
	for(h=1;h<=t;h++){
		ans=0;
		scanf("%ld%ld%ld%ld",&a1,&a2,&b1,&b2);
		for(i=a1;i<=a2;i++)
			for(j=b1;j<=b2;j++)
				ans+=ask(i,j);
		printf("Case #%ld: %ld\n",h,ans);
	}
	return 0;
}