#include <stdio.h>
#include <string.h>
#include <math.h>
typedef long long LL;
char s[100];
char st[100];
int n;
int dfs(int dep,LL v){
	if (dep==n){
		LL tmp=(LL)sqrt((double)v);
		if (tmp*tmp==v){
			for (int i=0;i<dep;i++)
				if (s[i]=='?') printf("%c",st[i]);else printf("%c",s[i]);
			printf("\n");
			return 1;
		}
		if ((tmp+1)*(tmp+1)==v){
			for (int i=0;i<dep;i++)
				if (s[i]=='?') printf("%c",st[i]);else printf("%c",s[i]);
			printf("\n");
			
			return 1;
		}
		return 0;
	}
	if (s[dep]=='?'){
		st[dep]='0';
		if (dfs(dep+1,v<<1)) return 1;
		st[dep]='1';
		return dfs(dep+1,(v<<1)+1);
	}else
	if (s[dep]=='0') return dfs(dep+1,v<<1);else return dfs(dep+1,(v<<1)+1);
}
int main(){
	int i,j,k;
	int tn,cp;
	for (scanf("%d",&tn),cp=1;cp<=tn;cp++){
		scanf("%s",s);
		n=strlen(s);
		printf("Case #%d: ",cp);
		dfs(0,0);
	}
	return 0;
}