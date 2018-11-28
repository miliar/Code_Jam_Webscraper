#include<stdio.h>
#include<algorithm>

using namespace std;

int r[33][33];
int an,n;
int a[122][122],as[122];

void dfs(int nn,int aan)
{
    int i,j;
    if(aan>=an)return ;
    for(i=1;i<=aan;i++)
    {
        bool ok=1;
        for(j=1;j<=as[i];j++)if(!r[nn][a[i][j]])
        {ok=0;break;}
        if(ok)
        {
            if(nn==n)
            {
                an=min(an,aan);
            }
            else
            {
                a[i][++as[i]]=nn;
                dfs(nn+1,aan);
                as[i]--;
            }
        }
    }
    if(nn==n)
    {
        an=min(an,aan+1);
    }
    else
    {
        as[aan+1]=1;
        a[aan+1][as[aan+1]]=nn;
        dfs(nn+1,aan+1);
    }
    
    
}

int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    int k,cases,ii,i,j,p[122][33],jj;
    scanf("%d",&cases);
    for(ii=1;ii<=cases;ii++)
    {
        scanf("%d%d",&n,&k);
        for(i=1;i<=n;i++)for(j=1;j<=k;j++)scanf("%d",&p[i][j]);
    
    
    for(i=1;i<=n;i++)for(j=1;j<=n;j++)
    {
        r[i][j]=1;
        for(jj=1;jj<k;jj++)
        {
            if(p[i][jj]>=p[j][jj] && p[i][jj+1]<=p[j][jj+1])r[i][j]=0;
            if(p[i][jj]<=p[j][jj] && p[i][jj+1]>=p[j][jj+1])r[i][j]=0;
        }
        //fprintf(stderr,"r[%d][%d]=%d\n",i,j,r[i][j]);
    }
    
    an=n;
    
    dfs(1,0);
    printf("Case #%d: %d\n",ii,an);
    
    }
    fputs("END",stderr);
    while(1);
    return 0;
}
