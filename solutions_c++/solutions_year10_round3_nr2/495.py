#include<iostream>
#include<vector>
#include<map>
#include<cmath>
#include<stdio.h>
#include<algorithm>
#include<string>
#include<stack>
#include<queue>

using namespace std;

int main()
{
     int t,i,j,l,p,c,count,pl;
     cin>>t;
     for(i=1;i<=t;i++)
     {
          cin>>l>>p>>c;
          count=0;
          if(p%l==0) pl=p/l;
          else pl=p/l+1;
          while(c<pl)
          {
               count++;
               c*=c;
          }
          cout<<"Case #"<<i<<": ";
          cout<<count;
          cout<<"\n";
     }
     //system("pause");
     return 0;
}
