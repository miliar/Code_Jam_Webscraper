#include <iostream>
const int maxn=1000;
int a[maxn][maxn],f[maxn][maxn],i,j,k,p,q,r,n,m,t,cc,maxs,ss,ans[maxn];
char x[500];
int max(int i,int j)
{
    if (i>j) return i;
        else return j;
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d\n",&t);
    for (cc=1;cc<=t;cc++)
    {
        scanf("%d %d\n",&n,&m);
        for (i=0;i<n;i++)
        {
            gets(x);
            for (j=0;j<m>>2;j++)
            {
                if ((x[j]>='0')&&(x[j]<='9')) p=x[j]-'0';
                                         else p=x[j]-'A'+10;
                for (k=0;k<4;k++) 
                {
                    a[i][(j<<2)+k]=(p&(1<<(3-k)))>>(3-k);
                    f[i][(j<<2)+k]=1;
                }
            }
        }
        maxs=1;
        for (i=n-2;i>=0;i--)
            for (j=m-2;j>=0;j--)
            {
                k=f[i+1][j+1];
                if (k>f[i+1][j]) k=f[i+1][j];
                if (k>f[i][j+1]) k=f[i][j+1];
                if (k>1)
                        if (a[i][j]==a[i+1][j+1]) k++;
                                             else k=1;
                else
                        if ((a[i][j]==a[i+1][j+1])&&(a[i][j]!=a[i+1][j])&&(a[i][j]!=a[i][j+1])) k++;
                                                                                           else k=1;
                f[i][j]=k;
                if (maxs<k) maxs=k;
            }
        ss=0;
        memset(ans,0,sizeof(ans));
        for (p=maxs;p>0;p--)
            for (i=0;i<n;i++)
                for (j=0;j<m;j++)
                    if (f[i][j]==p)
                    {
                                   ans[p]++;
                                   for (q=i;q<i+p;q++)
                                       for (r=j;r<j+p;r++) f[q][r]=0;
                                   for (q=max(0,i-p+1);q<i+p;q++)
                                       for (r=max(0,j-p+1);r<j+p;r++)
                                       if ((q<i)||(r<j))
                                       {
                                                        k=max(i-q,j-r);
                                                        if (f[q][r]>k) f[q][r]=k;
                                       }
                    }
        for (p=1;p<=maxs;p++) if (ans[p]) ss++;
        printf("Case #%d: %d\n",cc,ss);
        for (p=maxs;p>0;p--)
            if (ans[p])
            printf("%d %d\n",p,ans[p]);
    }
}
