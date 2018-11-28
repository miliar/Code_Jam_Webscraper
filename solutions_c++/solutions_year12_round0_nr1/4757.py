#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
#include<stack>
#define SSD(x) (scanf("%d",&x))
#define SSL(x) (scanf("%lld",&x))
#define SSF(x) (scanf("%f",&x))
#define SSS(x) (scanf("%s",x))
#define ABS(x) (x>0?x:-x)
using namespace std;
#define MOD 1000000007
int main()
{
     int t,i,j;
     char s[]="yhesocvxduiglbkrztnwjpfmaq";
     freopen("A.in","r",stdin);
     freopen("output.txt","w+",stdout);
     char a[10000];
     scanf("%d\n",&t);
     for(int t1=1;t1<=t;t1++)
     {
         gets(a);
         int l=strlen(a);
         printf("Case #%d: ",t1);
         for(i=0;i<l;i++)
         {
             if(a[i]==' ') printf(" ");
             else
             {
                 printf("%c",s[a[i]-'a']);
             }
         }
         cout<<endl;
                 

     }
     return 0;
}

