#include<stdio.h>
#include<string.h>
int main(){
	int i,j,k,n,m,sum,t,a[30];
	char str1[510],str[30]="welcome to code jam";
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	scanf("%d",&n);getchar();
	for(t=1;t<=n;++t){
		gets(str1);
		memset(a,0,sizeof(a));
		m=strlen(str1);
		for(i=0;i<m;++i){
			for(j=0;j<=i&&j<19;++j){
				if(str1[i]=='w'){a[0]++;break;}
				if(str1[i]==str[j]){
					a[j]+=a[j-1];
					a[j]%=10000;
				}
			}
		}
		printf("Case #%d: %04d\n",t,a[18]);
	}
	return 0;
}