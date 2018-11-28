#include<cstdio>
#include<string.h>

int l,d,n;
char s[5005][20],tmp[1005];
bool ok[20][30];

int main(){
	scanf("%d%d%d",&l,&d,&n);
	gets(tmp);
	for (int i=1;i<=d;++i) gets(s[i]);
	for (int i=1;i<=n;++i){
		memset(ok,0,sizeof(ok));
		gets(tmp);
		
		int k=strlen(tmp),pos=0; bool ll=0;
		for (int j=0;j<k;++j){
			if (tmp[j]==')') ll=0,++pos;
			else if (tmp[j]=='(') ll=1;
			else {
				 ok[pos][tmp[j]-'a']=1;
				 if (ll==0) ++pos;
	 		}
		}
		
		//for (int j=0;j<26;++j) printf("%c %d\n",j+'a',ok[0][j]);
		
		int ans=0;
		for (int j=1;j<=d;++j){
			bool yes=1;
			for (int m=0;m<l;++m) yes&=ok[m][s[j][m]-'a'];
			if (yes) ++ans;
		}
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}
