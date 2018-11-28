#include<iostream>
#include<string.h>
#include<algorithm>
#include<stdio.h>
#include<cmath>
using namespace std;
int a[200][2],b[200][2];
int n,m;
int main()
{
    int i,j,k,num,p=0;
    int cs;
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&cs);
    while (cs--)
    {
          scanf("%d",&num);
          char ch;
          int pos1=1,pos2=1,time1=0,time2=0;
          for (n=m=0,i=1;i<=num;i++)
          {
               cin>>ch;
               cin>>k;
               if (ch=='O')
               {
                  time1=max(time1+abs(k-pos1)+1,time2+1);
                  pos1=k;
               }
               else
               {
                  time2=max(time2+abs(k-pos2)+1,time1+1);
                  pos2=k;
               }
          }
          printf("Case #%d: ",++p); 
          cout<<max(time1,time2)<<endl;
    }
}
    
