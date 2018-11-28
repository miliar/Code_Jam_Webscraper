#include<cstdio>
#include<string.h>
#include<cstdlib>
#define INF (1<<29)

int n;
char s[505];
char ans[25]="welcome to code jam";

int main(){
	scanf("%d",&n);
	gets(s);
	for (int t=1;t<=n;++t){
		int num[25];
		memset(num,0,sizeof(num));
		num[0]=1;
		gets(s);
		int k=strlen(s);
		for (int i=0;i<k;++i){
			for (int j=0;j<=18;++j){
				if (s[i]==ans[j]) num[j+1]+=num[j];
				if (num[j+1]>10000) num[j+1]%=10000;
			}
			//for (int j=0;j<=19;++j) printf("%d %d\n",j,num[j]);
		}
		
		num[19]%=10000;
		if (num[19]<10) printf("Case #%d: 000%d\n",t,num[19]);
		else if (num[19]<100) printf("Case #%d: 00%d\n",t,num[19]);
		else if (num[19]<1000) printf("Case #%d: 0%d\n",t,num[19]);
		else printf("Case #%d: %d\n",t,num[19]);
	}
	return 0;
}
