#include<iostream>
//#include<conio.h>
#include<cstring>
#include<cstdlib>
#include<map>
using namespace std;
main()
{
int t,te=0;
cin>>t;
while(++te<=t)
 {
            int a,b,ta,tb,i,j;
            scanf("%d%d",&a,&b);
            if(a==b)
            {if(te!=t)
  cout<<"Case #"<<te<<": "<<0<<"\n";
  else            
  cout<<"Case #"<<te<<": "<<0; 
            
            
            continue;}
              ta=a;
              tb=b;
              int l=0,pairs=0;
              while(ta>0){++l;ta/=10;}
              for(i=a;i<b;i++)
              {int posi[6],ti=i,pos,tl=l;
                 while(tl>0){posi[tl]=ti%10;ti/=10;--tl;}
                 int mod=1;for(j=1;j<l;j++)mod*=10;
                 int sum=i;
                 
                              for(j=1;j<l;j++)
                {
                    sum%=mod;
                    sum*=10;sum+=posi[j];//cout<<"\nsum"<<sum;
                    if(sum>i&&sum<=b)++pairs;
                }
                              
                              
                              
                              
              }
             if(te!=t)
  cout<<"Case #"<<te<<": "<<pairs<<"\n";
  else            
  cout<<"Case #"<<te<<": "<<pairs; 
 }
      //getch();
}