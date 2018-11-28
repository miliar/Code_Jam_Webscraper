#include <iostream>
using namespace std;

char text[20]="welcome to code jam";

int f[502][20],n,l,i,j,k,res;
char s[504];

int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d\n",&n);
	for (int t=1;t<=n;++t){
		gets(s);l=strlen(s);memmove(s+1,s,502);
		memset(f,0,sizeof f);res=0;
		for (i=1;i<=l;++i){
			if (s[i]=='w')f[i][1]=1;
			for (j=2;j<20;++j)if (s[i]==text[j-1])
				for (k=1;k<i;++k)if (s[k]==text[j-2])
					f[i][j]=(f[i][j]+f[k][j-1])%10000;
			res=(res+f[i][19])%10000;
		};
		printf("Case #%d: ",t);
		if (res<1000)cout<<0;
		if (res<100)cout<<0;
		if (res<10)cout<<0;
		cout<<res<<endl;
	};
};