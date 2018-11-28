#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <queue>
using namespace std;
int tc,ok,n;
char s[100];
int f(int x){
	ok=-1;
	for (int i=n-2;i>=x&&ok==-1;i--){
			int mx=20,u,v;
			for (int j=i+1;j<n;j++){
				//printf("%d %d\n",i+1,j+1);
				if (s[i]<s[j] && mx>s[j]-'0'){
					mx=s[j]-'0';
					u=i; v=j;
				}
			}
			if (mx!=20){
				char ccc=s[u];
				s[u]=s[v]; s[v]=ccc;
				ok=i;
				//printf(" SN\n");
			}
		}
	return ok;
}
int main(){
	scanf("%d",&tc);
	for (int c=1;c<=tc;c++){
		scanf("%s",s);
		n=strlen(s);int yoyo=0;
		int k=f(0);
		//printf(" M %s\n",s);
		if (k!=-1) sort(s+k+1,s+n);
		else yoyo=1;
		if (yoyo){
			int mn=100,u;
			for (int i=0;i<n;i++) if (mn>s[i]-'0' && s[i]!='0') mn=s[i]-'0',u=i;
			char cc=s[u]; s[u]=s[0]; s[0]=cc;
			sort(s+1,s+n);
			printf("Case #%d: %c0",c,s[0]);
			for (int i=1;i<n;i++){
				printf("%c",s[i]);
			}
			printf("\n");
		}
		else printf("Case #%d: %s\n",c,s);
	}
	return 0;
}
