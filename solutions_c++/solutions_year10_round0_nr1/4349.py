#include<iostream>
#include<conio.h>
#include<math.h>
using namespace std;
int main()
{
    int A[100000];
    freopen("logfile.txt", "a+", stdout);
    int t,n;
    long k;  
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
            scanf("%d",&n);
            scanf("%d",&k);
            int j=pow(2,n);
            if(((k+1)%j)==0)
                     A[i]=1;
            else
                     A[i]=0;                                                   
    }
    for(int i=0;i<t;i++)
    {
            if(A[i]==0)
                           printf("Case #%d: OFF\n",i+1);                  
            else
                           printf("Case #%d: ON\n",i+1);
    }     
   getch();      
    return 1;
}
