#include <iostream>
using namespace std;

int l,d,n,i,j,k,x,cnt,last;
char st[5001][20],s[100000];
bool f[5001],flag;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d %d %d\n",&l,&d,&n);
	for (i=1;i<=d;++i)gets(st[i]);
	for (i=1;i<=n;++i){
		gets(s);
		int len=strlen(s);
		memset(f,true,sizeof f);
		last=-1;cnt=0;
		for (j=0;j<len;++j)
			if (s[j]=='(')last=j+1;
			else if (s[j]==')'){
				for (k=1;k<=d;++k){
					bool flag=false;
					for (x=last;x<j;++x)
						if (st[k][cnt]==s[x])flag=true;
					if (!flag)f[k]=false;
				};
				++cnt;last=-1;
			}
			else if (last==-1){
				for (k=1;k<=d;++k)
					if (st[k][cnt]!=s[j])f[k]=false;
				++cnt;last=-1;
			};
		cnt=0;
		for (j=1;j<=d;++j)cnt+=f[j];

		printf("Case #%i: %d\n",i,cnt);
	};
};