#include<stdio.h>
#include<string.h>
char s[5010][20],c;
bool mark[30],b[5010];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int l,d,n;
	scanf("%d%d%d",&l,&d,&n);
	char ts[10];
	gets(ts);
	for (int i=1;i<=d;i++) gets(s[i]);
	for (int i=1;i<=n;i++) {
		memset(b,0,sizeof(b));
		for (int j=1;j<=l;j++) {
			c=getchar();
			memset(mark,0,sizeof(mark));
			if (c!='(') mark[c-'a']=1;
			else
				while (((c=getchar())!=')')) mark[c-'a']=1;
			for (int k=1;k<=d;k++) if (mark[s[k][j-1]-'a']==0) b[k]=1;
		}
		gets(ts);
		int ans=0;
		for (int j=1;j<=d;j++) if (b[j]==0) ans++;
		printf("Case #%d: %d\n",i,ans);
	}
}
