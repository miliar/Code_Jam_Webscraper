#include<cstdio>
#include<cstring>
int N;
const char *s="welcome to code jam";
int ans[1000][22];

char inpS[1000];

int main(){
	int i,j,k;
	int l,l0;
	scanf("%d",&N);
	gets(inpS);
	for (i=1;i<=N;i++){
		memset(ans,0,sizeof(ans));
		gets(inpS);
		l=strlen(inpS);
		l0=strlen(s);
		for (j=0;j<l;j++)
			if (inpS[j]==s[0])
				ans[j][0] = 1;
		for (j=1;j<=l0;j++){
			int qt=0;
			for (k=0;k<=l;k++){
				qt=(qt+ans[k][j-1])%10000;
				if (s[j]==inpS[k])
					ans[k][j] = qt;
			}
		}
		printf("Case #%d: %04d\n", i, ans[l][l0]);
	}
	return 0;
}
