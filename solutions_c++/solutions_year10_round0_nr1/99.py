#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

long t,n,k;
bool q[40];

int main(){
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	long h,i,j;
	scanf("%ld",&t);
	for(h=1;h<=t;h++){
		scanf("%ld%ld",&n,&k);
		i=0;
		memset(q,0,sizeof(q));
		while(k>0){
			q[++i]=(k%2==1);
			k/=2;
		}
		for(j=1;j<=n;j++)
			if(q[j]==0)break;
		printf("Case #%ld: ",h);
		if(j==n+1)printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}