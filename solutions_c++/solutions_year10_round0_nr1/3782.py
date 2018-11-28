#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<iostream>
using namespace std;
int main()
{   
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    
    int t;
    scanf("%d",&t);
    int n,k;
    int num=0;
    while(t--)
    {  
       scanf("%d%d",&n,&k);
       num++;
       int term=1<<n;
       k++;
       if(k%term==0)printf("Case #%d: ON\n",num);
       else printf("Case #%d: OFF\n",num);      
    }
   // system("pause");
    return 0;
}
