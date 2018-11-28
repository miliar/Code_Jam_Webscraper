#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int merg[27][27],x[27][27];
int a,b,c,d,e,f,g,h,i,j,k,m,n,testcase;
char w[3],ch,s[102];
int z[102];
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&testcase);
	for (f=1;f<=testcase;f++){
		scanf("%d",&n);
		memset(merg,0,sizeof(merg));
		memset(x,0,sizeof(x));
		for (i=1;i<=n;i++) {
			scanf("%s",&w);
			merg[w[0]-64][w[1]-64]=w[2]-64;
			merg[w[1]-64][w[0]-64]=w[2]-64;
			}
		scanf("%d",&m);
		for (i=1;i<=m;i++){
			scanf("%s",&w);
			g=w[0]-64;h=w[1]-64;
			x[g][h]=1;x[h][g]=1;
			}
		scanf("%d%c",&d,&ch);
		for (i=0;i<d;i++) scanf("%c",&s[i]);
		s[d]='\0';
		c=0;
		for (i=0;i<strlen(s);i++){
			c++;z[c]=s[i]-64;
			if (c>1){
				if (merg[z[c]][z[c-1]]){
					c--;z[c]=merg[z[c]][z[c+1]];}else
				for (j=1;j<=c-1;j++) if (x[z[c]][z[j]]){
					c=0;break;}
				}
			}
		printf("Case #%d: [",f);
		for (i=1;i<=c;i++){
			if (i>1) printf(", ");
			printf("%c",z[i]+64);
			}
		printf("]\n");
		}
	return 0;
}
