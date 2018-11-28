#include<stdio.h>
int m[50][50],n,a[50];
void init()
{
	int i,j;
  char ctmp;
    scanf("%d",&n);
    for(i=1;i<=n;i++) 
        for(j=1;j<=n;j++) 
        {
            while(scanf("%c",&ctmp)) if(ctmp=='0'||ctmp=='1') break;
            m[i][j]=ctmp-'0';
        }
    for(i=1;i<=n;i++)
    {
        for(j=n;j>=1;j--) if(m[i][j]) break;
        a[i]=j;
	}
    //for(i=1;i<=n;i++) printf("%d\n",a[i]);
        
}

void work()
{
    int ans=0,i,j,k,tmp;
    for(i=1;i<=n;i++)
    {
	    for(j=i;j<=n;j++) if(a[j]<=i) break;
	    tmp=a[j];
	    for(k=j;k>i;k--) a[k]=a[k-1];
	    a[i]=tmp;
	    ans+=j-i;
	}
	printf("%d\n",ans);
}
int main()
{
  freopen("A-large.in","r",stdin);
  freopen("out.txt","w",stdout);
	int ncase,nc;
    scanf("%d",&ncase);
    for(nc=1;nc<=ncase;nc++)
    {
	    init();
	    printf("Case #%d: ",nc);
	    work();
	}
	return 0;
}
