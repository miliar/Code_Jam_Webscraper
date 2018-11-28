#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
    FILE *fp = fopen("outputC.txt","w");
 int n;
 int t,cnt;
 scanf("%d",&t);
 for(cnt=1;cnt<=t;cnt++)
 {
 scanf("%d",&n);
 int i;
 int small = 1000000;
 long int sum = 0;
 int exor;
 exor=0;
 for(i=0;i<n;i++)
 {
                 int x;
                 scanf("%d",&x);
                 
                 if(small>x)
                  small = x;
                  
                 sum += x;
                 
                 exor=exor^x;
                 
    
}

if(exor==0)
 fprintf(fp,"Case #%d: %d\n",cnt,sum-small);
else
 fprintf(fp,"Case #%d: NO\n",cnt);
}
 
 return 0;
}
