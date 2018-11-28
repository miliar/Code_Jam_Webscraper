#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int dp[110][110];
int can(int s,int p){
	if(s>=(3*p-4)&&s<=(3*p+4))
	return 1;
	return 0;
}

int f[110];
int main(){
	int t,ca=1;
//	freopen("B-large.in","r",stdin);
//	freopen("oo.txt","w",stdout);
	scanf("%d",&t);
	while(t--){
		int n,s,p;
		scanf("%d%d%d",&n,&s,&p);
		for(int i=1;i<=n;i++) scanf("%d",&f[i]);
		int a=0,b=0;
		for(int i=1;i<=n;i++){
			if(f[i]>=3*p-2) a++;
			else if(p>1&&f[i]>=(3*p-4)) b++;
		}
		if(b>s) b=s;
		printf("Case #%d: %d\n",ca++,a+b);
	}
	return 0;
}
