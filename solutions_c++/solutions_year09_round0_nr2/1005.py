#include<stdio.h>

int alt[110][110];
int val[110][110];
int h,w;
int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};
int k;

int calc(int i, int j)
{
    if(val[i][j]!=-1)
        return val[i][j];
    int min=alt[i][j],dd=-1;
    for(int d=0;d<4;d++)
    {
        int ni=i+dx[d],nj=j+dy[d];
        if(ni>=h || ni<0 || nj>=w || nj<0)
            continue;
        if(alt[ni][nj]<min)
        {
            min=alt[ni][nj];
            dd=d;
        }
    }
    if(dd==-1)
    {
        val[i][j]=k;
        k++;
    }
    else
        val[i][j]=calc(i+dx[dd],j+dy[dd]);
    return val[i][j];
}

int main()
{
    //freopen("B1.in","r",stdin);
    //freopen("B1.out","w",stdout);
    freopen("B2.in","r",stdin);
    freopen("B2.out","w",stdout);

    int t,i,j;
    scanf("%d",&t);
    for(int cs=1;cs<=t;cs++)
    {
        scanf("%d%d",&h,&w);
        for(i=0;i<h;i++)
        {
            for(j=0;j<w;j++)
            {
                scanf("%d",&alt[i][j]);
                val[i][j]=-1;
            }
        }
        k=0;
        for(i=0;i<h;i++)
        {
            for(j=0;j<w;j++)
            {
                calc(i,j);                
            }
        }

        printf("Case #%d:\n",cs);
        for(i=0;i<h;i++)
        {
            for(j=0;j<w;j++)
            {
                if(j)
                    printf(" ");
                printf("%c",'a'+val[i][j]);
            }
            puts("");
        }
    }
    return 0;
}
