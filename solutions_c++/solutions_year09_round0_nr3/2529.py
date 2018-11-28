#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

int main(){
	freopen("in","rt",stdin);
	freopen("out","wt",stdout);
	int n;
	char s[1024];
	char q[20]="welcome to code jam";
	int ans[20];
	scanf("%d", &n);
	gets(s);
	int l;
	for (int i=0; i<n; ++i){
		gets(s);
		memset(ans,0,sizeof(ans));
		l=strlen(s);
		for (int j=0; j<l; ++j){
			if (s[j]=='w') ans[0]=(ans[0]+1)%10000;
			for (int u=1; u<19; ++u){
				if (s[j]==q[u]) ans[u]=(ans[u]+ans[u-1])%10000;
			}
		}
		printf("Case #%d: ", i+1);
		if (ans[18]<1000) printf("0");
		if (ans[18]<100) printf("0");
		if (ans[18]<10) printf("0");
		printf("%d\n", ans[18]);	
	}
	return 0;
}