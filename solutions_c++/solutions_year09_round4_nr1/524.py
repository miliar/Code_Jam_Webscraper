#include <stdio.h>

char inp[50][50];

int ps[50];

int pos[50];

bool avl[50];

int main()
{
    freopen("A2.in","r",stdin);
    freopen("A2.out","w",stdout);
    int t,i,j,k;
    scanf("%d",&t);
    for(int cs=1;cs<=t;cs++)
    {
        int n;
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            pos[i]=0;
            avl[i]=0;
            scanf("%s",inp[i]);
            for(j=0;j<n;j++)
            {
                inp[i][j]-='0';
                if(inp[i][j])
                    pos[i]=j;
            }
        }

        for(i=0;i<n;i++)
        {
            while(pos[i]<n && avl[pos[i]])
                pos[i]++;
            avl[pos[i]]=1;
            ps[i]=pos[i];
            
        }
        int ans=0;
        for(i=0;i<n;i++)
        {
            for(j=i;j<n;j++)
                if(pos[j]==i)
                    break; 
            ans+=j-i;
            for(k=j-1;k>=i;k--)
                pos[k+1]=pos[k];
        }

        printf("Case #%d: %d\n",cs,ans);


    }
    return 0;
}