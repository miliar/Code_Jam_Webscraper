#include<cstdio>
#include<cstring>
const int N=501;
const char s2[19]={'w','e','l','c','o','m','e',' ','t','o',' ','c','o','d','e',' ','j','a','m'};
const int modo=10000;
char s1[N];
int f[N][20];
int test;
int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&test);gets(s1);
	for (int testnum=1;testnum<=test;testnum++){
		gets(s1);
		int n=strlen(s1);
		f[0][0]=1;
		for (int i=1;i<=n;i++){
			f[i][0]=1;
			for (int j=1;j<=19;j++)
				if (s1[i-1]==s2[j-1])
					f[i][j]=(f[i-1][j-1]+f[i-1][j])%modo;
				else
					f[i][j]=f[i-1][j];
		}
		printf("Case #%d: %04d\n",testnum,f[n][19]);
	}
	return 0;
}
