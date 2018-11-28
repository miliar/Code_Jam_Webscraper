#include <stdio.h>
#include <string.h>
int map[11000];
int a[1000],b[1000];
int main()
{
    int T,i,n,ans,x,y,j;
	freopen("GCAJ.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
	    scanf("%d",&n);
	    ans=0;
	    memset(map,0,sizeof(map));
	    for(i=0;i<n;i++)
	    {
            scanf("%d%d",&a[i],&b[i]);
            map[a[i]]=b[i];
        }
        for(i=0;i<n;i++)
        {
            x=a[i]; y=b[i];
            for(j=1;j<11000;j++)
            {
                if(map[j])
                {
                    if(j<x && map[j]>y)
                    ans++;
                }
            }
        }
        printf("Case #%d: %d\n",t,ans);
    }
	return 0;
}
