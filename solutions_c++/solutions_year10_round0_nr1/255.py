#include<iostream>
#include<string.h>
#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
    int  cas,n,k;
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&cas);
    int t=0;
    while (cas--)
    {
        
          scanf("%d%d",&n,&k);
            int tt=(1<<n)-1; 
          if (k%(tt+1)==tt)
          printf("Case #%d: ON\n",++t);
          else
          printf("Case #%d: OFF\n",++t);
    }
}
          
