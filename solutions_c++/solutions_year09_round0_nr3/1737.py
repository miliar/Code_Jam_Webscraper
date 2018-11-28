#include<cstdio>
#include<iostream>
using namespace std;

const int MOD=10000;

int a[600][20];
char tar[30];
char s[600];
int tl;

void out(int x)
{
	int p=1000;
	while (p!=1 && p>x) {
		printf("0");
		p/=10;
	}
	printf("%d\n",x);
}

int main()
{
	freopen("C-large.in","rt",stdin);
	freopen("C-large.out","wt",stdout);
	strcpy(tar," welcome to code jam");
	tl=strlen(tar);
	int T, tt=0;
	scanf("%d\n",&T);
	while (tt<T) {
		memset(a,0,sizeof(a));
		a[0][0]=1;
		gets(s);
//		printf("%s\n",s);
		int len=strlen(s);
		for(int i=0;i<len;++i) {
			for(int j=0;j<tl;++j) a[i+1][j]=a[i][j];
			for(int j=1;j<tl;++j)
				if (s[i]==tar[j]) a[i+1][j]+=a[i][j-1];
			for(int j=0;j<tl;++j) a[i+1][j]%=MOD;
		}
		printf("Case #%d: ",++tt);
		out(a[len][tl-1]);
	}
	return 0;
}