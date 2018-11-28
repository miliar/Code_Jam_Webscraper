#include<stdio.h>
int c,d,n;
char C[200][10],D[200][10],S[200];
int cnt;
char ans[200];
void print()
{
    int i;
    ++cnt;
    printf("Case #%d: [",cnt);
    for(i=1;i<ans[0];i++)printf("%c, ",ans[i]);
    if (ans[0])printf("%c]\n",ans[ans[0]]);
    else printf("]\n");
}
void solve()
{
    int i,j,k;
    for (i=0;i<n;i++)
    {
	ans[++ans[0]]=S[i];
	if (ans[0]>1)
	{
		for (j=1;j<=c;j++)
	    	if (((ans[ans[0]]==C[j][0])&&(ans[ans[0]-1]==C[j][1]))||((ans[ans[0]-1]==C[j][0])&&(ans[ans[0]]==C[j][1]))){ans[0]--;ans[ans[0]]=C[j][2];}
		for (j=1;j<=d;j++)
		    for (k=1;k<ans[0];k++)if (((ans[ans[0]]==D[j][0])&&(ans[k]==D[j][1]))||((ans[ans[0]]==D[j][1])&&(ans[k]==D[j][0])))ans[0]=0;
	}
    }
}
void init()
{
    int i;
    scanf("%d",&c);
    for (i=1;i<=c;i++)scanf("%s",C[i]);
    scanf("%d",&d);
    for (i=1;i<=d;i++)scanf("%s",D[i]);
    scanf("%d",&n);
    scanf("%s",S);
    ans[0]=0;
}
int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int t;
    scanf("%d",&t);
    while (t--)
    {
    	init();
    	solve();
    	print();
    }
    return 0;
}
