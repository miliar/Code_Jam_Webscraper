#include<stdio.h>
int n;
int R[200];
int P[200];
int next[200];
int ans;
int cnt;
void print()
{
    cnt++;
    printf("Case #%d: %d\n",cnt,ans);
}
void solve()
{
    int p,nowo,nowb,i,t;
    nowo=1;nowb=1;p=1;
    for (t=1;;t++)
    {
	if (R[p]==0)
	{
	    int nextb=nowb;
	    for (i=p+1;i<=n;i++)
		if (R[i]==1){nextb=P[i];break;}
	    if (nowb<nextb)nowb++;
	    else
		if (nowb>nextb)nowb--;
	    if (nowo==P[p]){p++;if (p>n){ans=t;break;}continue;}
	    if (nowo<P[p])nowo++;
	    else if (nowo>P[p])nowo--;
	}
	else
	{
	    int nexto=nowo;
	    for (i=p+1;i<=n;i++)
		if (R[i]==0){nexto=P[i];break;}
	    if (nowo<nexto)nowo++;
	    else if (nowo>nexto)nowo--;
	    if (nowb==P[p]){p++;if(p>n){ans=t;break;}continue;}
	    if (nowb<P[p])nowb++;
	    else if (nowb>P[p])nowb--;
	}
    }
}
void init()
{
    int i;
    scanf("%d",&n);
    for (i=1;i<=n;i++)
    {
	char c;
	int x;
	scanf(" %c %d",&c,&x);
	if (c=='O')R[i]=0;
	else R[i]=1;
	P[i]=x;
    }
}
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
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
