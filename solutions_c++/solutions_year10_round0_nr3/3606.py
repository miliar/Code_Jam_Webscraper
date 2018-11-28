#include<iostream>
#include<conio.h>
using namespace std;
int main()
{
    int t;
    int r,k,n,i=1,g=0,j;
    int A[1001];
    int B[1001];
    freopen("logfileshash.txt", "a+", stdout);
    int C[1001];
    scanf("%d",&t);
    while(i<=t)
    {
               int ct=0,ct1=1,cost=0;
               scanf("%d %d %d",&r,&k,&n);
      
               for(j=0;j<n;j++)
                       scanf("%d",&A[j]);
               while(ct1<=r)
               {
                            ct=0;j=0;
                            for(j=0;j<n&&ct+A[j]<=k;j++)
                            {
                                    ct+=A[j];
                                    B[j]=A[j];
                                    //A[j]=0;
                            }
                            
                            for(int l=0;l<n-j;l++)
                            {
                                    A[l]=A[l+j];
                                   
                            }
                            for(int l=0;l<j;l++)
                                     A[n-j+l]=B[l];
                            
                            
                            cost+=ct;
                            ct1++;
                            
                            
               }
               C[g]=cost;
               g++;
               i++;
    }
    for(int p=0;p<t;p++)
    {
             printf("Case #%d: %d\n",p+1,C[p]);
    }
  //  getch();
    return 1;
}
               
