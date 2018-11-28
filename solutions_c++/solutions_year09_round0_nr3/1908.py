#include<stdio.h>
#include<string.h>

char a[20]="welcome to code jam";
char s[1000];
int f[1000][20];

int main(){
	int ca; scanf("%d",&ca); gets(s);
	for (int tt=1; tt<=ca; tt++){
		gets(s);
		int n=strlen(s);
		memset(f,0,sizeof(f));
		int ans=0;
		for (int i=0; i<n; i++){
			for (int j=0; j<19; j++){
				if (s[i]==a[j]){
					if (j==0) f[i][j]=1;
					else for (int k=0; k<i; k++) f[i][j]=(f[i][j]+f[k][j-1]);
				}
			}
			ans=(ans+f[i][18])%10000;
		}
		printf("Case #%d: %04d\n",tt,ans);
	}
	return 0;
}
