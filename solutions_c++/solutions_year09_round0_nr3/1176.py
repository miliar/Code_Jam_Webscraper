#include <cstdio>
#include <cstring>

char l[2000];
int n,m;
int pd[2000][21];

char s[]="welcome to code jam";

int calc(int a, int b) {
	if (a==n && b==m) return 1;
	if (a==n) return 0;
	if (pd[a][b]!=-1) return pd[a][b];
	
	int res=0;
	if (l[a]==s[b]) res=calc(a+1,b+1);
	res=(res+calc(a+1,b))%10000;
	
	return (pd[a][b]=res);
}

int main() {
	int nt;
	m=strlen(s);
	
	scanf(" %d",&nt);
	for (int ct=1; ct<=nt; ct++) {
		scanf(" %[^\n]",l);
		n=strlen(l);
		memset(pd,-1,sizeof(pd));
		
		printf("Case #%d: %04d\n",ct,calc(0,0));
	}
	
	return 0;
}
