#include <iostream>

using namespace std;

int N,maxr=0,maxb=0,T,a[1000][1000],last[1000];

void Check()
{
     int sum;
     for (int i=1;i<=N;i++)
     {
         sum=0;
         for (int j=1;j<=N+1;j++)
             if (j==1) sum=1;
             else if (a[i][j]!=a[i][j-1]) 
                  {
                     if (a[i][j-1]==1) maxr>?=sum;
                     if (a[i][j-1]==2) maxb>?=sum;
                     sum=1;
                  }
                  else sum++;
     }
     for (int j=1;j<=N;j++)
     {
         sum=0;
         for (int i=1;i<=N+1;i++)
             if (i==1) sum=1;
             else if (a[i][j]!=a[i-1][j]) 
                  {
                     if (a[i-1][j]==1) maxr>?=sum;
                     if (a[i-1][j]==2) maxb>?=sum;
                     sum=1;
                  }
                  else sum++;
     }
     for (int i=1;i<=N;i++)
     {
         sum=0;
         for (int j=0;j<=i;j++)
             if (j==0) sum=1;
             else if (a[i-j][j+1]!=a[i-j+1][j]) 
                  {
                     if (a[i-j+1][j]==1) maxr>?=sum;
                     if (a[i-j+1][j]==2) maxb>?=sum;
                     sum=1;
                  }
                  else sum++;
     }
     for (int j=1;j<=N;j++)
     {
         sum=0;
         for (int i=0;i<=N-j+1;i++)
             if (i==0) sum=1;
             else if (a[N-i][i+j]!=a[N-i+1][i+j-1]) 
                  {
                     if (a[N-i+1][i+j-1]==1) maxr>?=sum;
                     if (a[N-i+1][i+j-1]==2) maxb>?=sum;
                     sum=1;
                  }
                  else sum++;
     }    
     for (int i=1;i<=N;i++)
     {
         sum=0;
         for (int j=0;j<=N-i+1;j++)
             if (j==0) sum=1;
             else if (a[i+j][j+1]!=a[i+j-1][j]) 
                  {
                     if (a[i+j-1][j]==1) maxr>?=sum;
                     if (a[i+j-1][j]==2) maxb>?=sum;
                     sum=1;
                  }
                  else sum++;
     }
     for (int j=1;j<=N;j++)
     {
         sum=0;
         for (int i=0;i<=N-j+1;i++)
             if (i==0) sum=1;
             else if (a[i+1][i+j]!=a[i][i+j-1]) 
                  {
                     if (a[i][i+j-1]==1) maxr>?=sum;
                     if (a[i][i+j-1]==2) maxb>?=sum;
                     sum=1;
                  }
                  else sum++;
     }              
}

void Gravity()
{
     for (int j=1;j<=N;j++)
     {
         for (int i=N;i>=1;i--)
             if (a[i][j]) a[N-last[j]++][j]=a[i][j];
         for (int i=1;i<=N-last[j];i++) a[i][j]=0;
     }
}

int main()
{
    freopen("Rotate.in","r",stdin);
    freopen("Rotate.out","w",stdout);
    cin>>T;
    for (int t=1;t<=T;t++)
    {
        int K;
        memset(a,0,sizeof(a));
        memset(last,0,sizeof(last));
        maxr=0;maxb=0;
        scanf("%d%d",&N,&K);
        for (int i=1;i<=N;i++)
            for (int j=1;j<=N;j++)
            {
                char ch;
                scanf("\n%c",&ch);
                if (ch=='.') a[j][N+1-i]=0;
                if (ch=='R') a[j][N+1-i]=1;
                if (ch=='B') a[j][N+1-i]=2;
            }
        Gravity();
        Check();
        //cout<<maxb<<" "<<maxr<<endl;
        if (maxr>=K)
           if (maxb>=K) cout<<"Case #"<<t<<": Both\n";
           else cout<<"Case #"<<t<<": Red\n";
        else if (maxb>=K) cout<<"Case #"<<t<<": Blue\n";
             else cout<<"Case #"<<t<<": Neither\n";
    }
    return 0;
}
