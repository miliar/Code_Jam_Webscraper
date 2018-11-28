#include<stdio.h>
int f[101][300],a[101];
int n,m,i,j,k,l,t,tt,h;

int abs(int o)
{
    if (o>0) {return o;} else {return -o;}
}

int min(int o,int p)
{
    if (o<p) {return o;} else {return p;}
}

int main()
{
    freopen("B-small-attempt0(2).in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d",&tt);
    for (t=1;t<=tt;t++)
    {
        for (i=0;i<=100;i++) for (j=0;j<=256;j++) {f[i][j]=0;}
        scanf("%d%d%d%d",&k,&l,&m,&n);
        for (i=1;i<=n;i++) {scanf("%d",&a[i]);}
        for (i=0;i<=255;i++) {f[1][i]=abs(i-a[1]);}
        for (i=2;i<=n;i++)
         for (j=0;j<=255;j++)
         {
             f[i][j]=f[i-1][j]+k;
             for (h=0;h<=255;h++)
             {
                 if (abs(h-j)<=m) f[i][j]=min(f[i][j],f[i-1][h]+abs(j-a[i]));
                 if (m!=0) {
                 int kk,ll;
                 kk=abs(a[i]-j);
                 ll=abs(h-j)/m-1;
                 if ((abs(h-j)%m)!=0) {ll++;}
                 if (ll<0) {ll=0;}ll=ll*l;

                 f[i][j]=min(f[i][j],f[i-1][h]+kk+ll);}
             }
         }
         int ans=f[n][0];
         for (i=1;i<=255;i++) ans=min(ans,f[n][i]);
         printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
