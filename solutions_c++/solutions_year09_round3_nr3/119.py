#include<stdio.h>
#include<cstring>
#include<algorithm>

using namespace std;

#define EEE 2020202020
int p,q,a[102],an[102][102],w[102],sum[102][102];
bool ud[102][102];

int aa(int l,int r)
{
    //fprintf(stderr,"aa %d %d  sum %d\n",l,r,sum[l][r]);
    if(ud[l][r])return an[l][r];
    if(l==r)return 0;
    int i,tan;
    tan=EEE;
    for(i=l;i<r;i++)
    {
        tan=min(tan,sum[l][r]-1+aa(l,i)+aa(i+1,r));
    }
    ud[l][r]=1;
    an[l][r]=tan;
    //fprintf(stderr,"an[%d][%d]=%d\n",l,r,an[l][r]);
    return tan;
}

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int cases,ii,i,j,jj;
    scanf("%d",&cases);
    for(ii=1;ii<=cases;ii++)
    {
        scanf("%d%d",&p,&q);
        for(i=1;i<=q;i++)scanf("%d",&a[i]);
        a[0]=0;
        a[++q]=p+1;
        for(i=1;i<=q;i++)w[i]=a[i]-a[i-1];
        for(i=1;i<=q;i++)for(j=i;j<=q;j++)
        {
            sum[i][j]=a[j]-a[i-1]-1;
            //for(jj=i;jj<=j;jj++)sum[i][j]+=w[jj];
        }
        memset(ud,0,sizeof(ud));
        printf("Case #%d: %d\n",ii,aa(1,q));
    }
    fputs("END\n",stderr);
    while(1);
    return 0;
}
