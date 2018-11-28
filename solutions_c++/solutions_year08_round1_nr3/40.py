#include<stdio.h>
#include<memory.h>

int nn[2][2]={
    {6,-4},
    {1,0}
};

int N;

int st[2]={28,6};

void mul(int a[2][2],int b[2][2],int cc[2][2])
{
     int i,j,k;
     int c[2][2];
     for(i=0;i<2;i++)
       for(j=0;j<2;j++)
       {
          c[i][j]=0;
          for(k=0;k<2;k++)
            c[i][j]+=a[i][k]*b[k][j];
       }
     for(i=0;i<2;i++)
        for(j=0;j<2;j++)
           cc[i][j]=(c[i][j]%1000+1000)%1000;
}

void solve()
{
     int aa[2][2],bb[2][2],cc[2][2];
     bool f[32];
     int tt=N-2;
     int ii=0,i;
     while(tt)
       f[ii++]=tt&1,tt>>=1;
     memset(aa,0,sizeof(aa));
     aa[0][0]=aa[1][1]=1;
     for(i=ii-1;i>=0;i--)
     {
        mul(aa,aa,aa);
        if(f[i])
           mul(aa,nn,aa);
     }
     if(N==2)
        printf("028\n");
     else
        printf("%03d\n",((aa[0][0]*st[0]+aa[0][1]*st[1]-1)%1000+1000)%1000);
}

int main()
{
    int T,i;
    //freopen("C.in","r",stdin);
    //freopen("C.txt","w",stdout);
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
       scanf("%d",&N);
       printf("Case #%d: ",i);
       solve();
    }
    return 0;
}

           
     
