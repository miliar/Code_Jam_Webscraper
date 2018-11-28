#include<stdio.h>
int n,m,i,j,k,l,t,tt;
int a[50000],b[5000][2],bo[50000],c[50000],tr[5000][10];

int min(int o,int p)
{
    if (o<p) {return o;} else {return p;}
}

void work(int o)
{
    if (o<(1<<n))
    {
       work(o*2);
       work(o*2+1);
       int i,j,k,l;
       c[o]=min(c[o*2],c[o*2+1]);
       for (i=0;i<=c[o];i++)
       {
           if (tr[o*2][i]!=-1) {k=tr[o*2][i];}
           if (tr[o*2+1][i]!=-1) {l=tr[o*2+1][i];}
           tr[o][i]=k+l+a[o];
           if ((i!=c[o]))
           {
                      if (tr[o*2][i+1]!=-1) {
                      k=tr[o*2][i+1];   
                      for (j=i+2;j<=c[o*2];j++)
                      {
                          k=min(k,tr[o*2][j]);
                      }
                      }
                      if (tr[o*2+1][i+1]!=-1) {
                      l=tr[o*2+1][i+1];   
                      for (j=i+2;j<=c[o*2+1];j++)
                      {
                          l=min(l,tr[1+o*2][j]);
                      }
                      }
                      if ((k+l<tr[o][i])||(tr[o][i]==-1)) {tr[o][i]=k+l;}
           }
       }
    } else {for (int i=0;i<=c[o];i++)tr[o][i]=0;} 
}

int main()
{
    freopen("B-large(2).in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d",&tt);
    for (t=1;t<=tt;t++)
    {
        scanf("%d",&n);
        for (i=1;i<=5000;i++) {c[i]=100;}
        for (i=1;i<=5000;i++) for (j=0;j<=10;j++) {tr[i][j]=-1;}
        for (i=1;i<=(1<<n);i++) {scanf("%d",&b[i][0]);c[(1<<(n))-1+i]=b[i][0];}
        for (i=n;i>=1;i--)
        for (j=1;j<=(1<<(i-1));j++) {scanf("%d",&a[(1<<(i-1))-1+j]);}
        work(1);
        
        int ans;ans=tr[1][0];
        for (i=1;i<=c[1];i++) {if ((tr[1][i]<ans)&&(tr[1][i]!=-1)) {ans=tr[1][i];}} 
        printf("Case #%d: %d\n",t,ans);
        
    }
    return 0;
}
