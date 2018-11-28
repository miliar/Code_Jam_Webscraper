#include<iostream>
#include<cstdio>
#include<string>
//#include<conio.h>
using namespace std;
int main()
{
    int d[31]={0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10};
    int s[31]={0,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10,10,10};
    int t,n,sr,i,p,x,z=0,m=0;
    scanf("%d",&t);
    while(t--)
    {
              z++;
              scanf("%d",&n);
              scanf("%d",&sr);
              scanf("%d",&p);
              int a[n];
              for(i=0;i<n;i++)
              scanf("%d",&a[i]);
              for(i=0;i<31;i++)
              {
                              if(d[i]==p)
                              {
                                         x=i;
                                         break;
                              }
              }
              for(i=0;i<n;i++)
              {
                              if(a[i]>=x)
                              m++;
                              else if(s[a[i]]>=p && sr>0)
                              {
                                   m++;
                                   sr--;
                              }
              }
              cout<<"Case #"<<z<<": "<<m<<endl;
              m=0;
    }
    //getch();
    return 0;
}
              
