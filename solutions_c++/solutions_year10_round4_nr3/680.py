#include<iostream>
using namespace std;
bool A[120][120],B[120][120];
int cnt=0,a,b,c,d,NUM;
void Solve()
{
     int Time=0;
     memset(A,false,sizeof(A));
     int n;
     scanf("%d",&n);
     NUM=0;
     for (int i=0;i<n;++i)
     {
         scanf("%d %d %d %d",&a,&b,&c,&d);
         for (int i=a;i<=c;++i)
         for (int j=b;j<=d;++j)
         {
              if (!A[i][j]) ++NUM;
              A[i][j]=true;
         }
         
     }
     while (NUM>0)
     {
           memset(B,false,sizeof(B));
           for (int i=1;i<=100;++i)
           for (int j=1;j<=100;++j)
           if ( A[i][j] && (A[i-1][j] || A[i][j-1]) )
           B[i][j]=true; else
           if ( !A[i][j] && (A[i-1][j] && A[i][j-1]) )
           B[i][j]=true;
           
           memset(A,false,sizeof(A));           
           NUM=0;
           for (int i=1;i<=100;++i)
           for (int j=1;j<=100;++j)
           {
                      A[i][j]=B[i][j];
                      if (A[i][j]) ++NUM;
           }
           ++Time;
     }
     printf("Case #%d: %d\n",++cnt,Time);
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C_Ans.txt","w",stdout);
    int T;
    scanf("%d",&T);

    while (T--) Solve();
    return 0;
}
