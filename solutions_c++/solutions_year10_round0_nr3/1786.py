#include <stdio.h>
#include <string.h>

int s[1005];
int tt[1005];
int map[1005];
int m[1005];

struct node
{
    long long p;
    int k;
}x[1005];

int main()
{
	freopen("C:\\Users\\QEver\\Desktop\\C-large.in","r",stdin);
	freopen("C:\\Users\\QEver\\Desktop\\C-large.out","w",stdout);
    int t,i,o,r,k,n,j,q,y;
    long long res,ans;
    scanf("%d",&t);
    for(o=1;o<=t;o++)
    {
        memset(x,0,sizeof(x));
        scanf("%d %d %d",&r,&k,&n);
        for(i=0;i<n;i++)
        {
            scanf("%d",&s[i]);
			tt[i]=s[i];
        }
		for(i=0;i<n;i++)
		{
			map[i]=i;
		}
        for(i=0;i<n;i++)
        {
            for(j=i+1;j!=i;j++)
            {
                if(j==n)j=0;
				if(j==i)break;
                if(tt[i]+s[j]<=k)
                {
                    tt[i]+=s[j];
                    map[i]=j;
                }
                else
                {
                    break;
                }
            }
        }
        res=0;
        q=0;
        y=1;
        while(x[q].k==0&&y<=r)
        {
            m[y]=q;
            x[q].k=y++;
            x[q].p=res;
            res+=tt[q];
            q=map[q]+1;
			while(q>=n)
			{
				q-=n;
			}
        }
        if(y==r+1)
        {
            printf("Case #%d: %lld\n",o,res);
        }
        else
        {
            int a,b,c;
            a=r-y+1;
            b=y-x[q].k;
            ans=res-x[q].p;
            c=a/b;
            res+=ans*c;
            a-=c*b;
            res+=x[m[x[q].k+a]].p-x[q].p;
            printf("Case #%d: %lld\n",o,res);
        }
    }
    return 0;
}
            
        
        
        
        
