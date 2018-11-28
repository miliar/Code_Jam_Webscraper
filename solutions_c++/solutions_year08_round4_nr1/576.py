#include <stdio.h>

const int inf=0x3fffffff;
int g[10001],c[10001],l[10001];
int m,v;

int dp(int root,int d)
{
	int l0,r0,l1,r1,ret=inf;
    if (root*2>m) return (l[root]==d)?0:-1;
    l0=dp(root<<1,0);
    l1=dp(root<<1,1);
    r0=dp((root<<1)+1,0);
    r1=dp((root<<1)+1,1);
    if (g[root]==0) {
        if (d==0 && l0!=-1 && r0!=-1 && l0+r0<ret) ret=l0+r0;  
        if (d==1 && l0!=-1 && r1!=-1 && l0+r1<ret) ret=l0+r1;
        if (d==1 && l1!=-1 && r0!=-1 && l1+r0<ret) ret=l1+r0;
        if (d==1 && l1!=-1 && r1!=-1 && l1+r1<ret) ret=l1+r1;
		if (c[root]==1) {
		    if (d==0 && l0!=-1 && r0!=-1 && l0+r0+1<ret) ret=l0+r0+1;  
		    if (d==0 && l0!=-1 && r1!=-1 && l0+r1+1<ret) ret=l0+r1+1;
		    if (d==0 && l1!=-1 && r0!=-1 && l1+r0+1<ret) ret=l1+r0+1;
		    if (d==1 && l1!=-1 && r1!=-1 && l1+r1+1<ret) ret=l1+r1+1;
		}
    } else {
        if (d==0 && l0!=-1 && r0!=-1 && l0+r0<ret) ret=l0+r0;  
        if (d==0 && l0!=-1 && r1!=-1 && l0+r1<ret) ret=l0+r1;
        if (d==0 && l1!=-1 && r0!=-1 && l1+r0<ret) ret=l1+r0;
        if (d==1 && l1!=-1 && r1!=-1 && l1+r1<ret) ret=l1+r1;
		if (c[root]==1) {
	        if (d==0 && l0!=-1 && r0!=-1 && l0+r0+1<ret) ret=l0+r0+1;  
	        if (d==1 && l0!=-1 && r1!=-1 && l0+r1+1<ret) ret=l0+r1+1;
	        if (d==1 && l1!=-1 && r0!=-1 && l1+r0+1<ret) ret=l1+r0+1;
	        if (d==1 && l1!=-1 && r1!=-1 && l1+r1+1<ret) ret=l1+r1+1;
		}
    }
	return (ret==inf)?-1:ret;
}

int main()
{
    int cs,ct,i;
    scanf("%d",&cs);
	for (ct=1;ct<=cs;ct++) {
        scanf("%d%d", &m,&v);
        for (i=1;i<=(m-1)/2;i++)
            scanf("%d%d",&g[i],&c[i]);
        for (i=(m+1)/2;i<=m;++i)
            scanf("%d",&l[i]);
        printf("Case #%d: ",ct);
		int ans=dp(1,v);
        if (ans==-1) printf("IMPOSSIBLE\n");
		else printf("%d\n",ans);
    }
    return 0;
}
