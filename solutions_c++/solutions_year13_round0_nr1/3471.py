#include<iostream>
#include<sstream>
#include<cstdio>
#include<climits>
#include<cstring>
#include<map>
#include<set>
#include<cstdio>
#include<cmath>
#include<vector>
#include <algorithm> 
using namespace std;
#define R return
#define FR(i,a,b) for(i=a;i<b;i++)
#define RFR(i,a,b) for(i=a;i>=b;i--)

typedef long long int ll;

int main()
{
int t,n,m,i,j,k;
cin>>t;
for(j=0;j<t;j++)
{  string arr[4];
   char win='D';
   for(i=0;i<4;i++)
   cin>>arr[i];
   /*for(i=0;i<4;i++)
   cout<<arr[i]<<"\n";*/
   char ch='D';
   int dot=0;
   for(i=0;i<4;i++)
   {  ch=arr[i][0];
      if(ch!='.')
      { if(ch=='T')
      ch=arr[i][1];
      if(ch!='.'){
      m=0;
      for(k=1;k<4;k++)
      { if(arr[i][k]==ch||arr[i][k]=='T')
         m++;
        else if(arr[i][k]=='.')
        dot++;
      }
      if(m==3)
      { win=ch; break ;};
      }
      }
   }
  // cout<<win<<" row\n";
   if(win=='D')
   { 
     for(i=0;i<4;i++)
     {  ch=arr[0][i];
      if(ch!='.')
      { if(ch=='T')
        ch=arr[1][i];
      if(ch!='.'){
      m=0;
      for(k=1;k<4;k++)
      { if(arr[k][i]==ch||arr[k][i]=='T')
         m++;
      }
      if(m==3)
      { win=ch; break ;};
      }
      }
    //  cout<<win<<" col\n";
      }
   }
   if(win=='D')  //left diagonal
   {  ch=arr[0][0];
      if(ch!='.')
      { if(ch=='T')
         ch=arr[1][1];
         if(ch!='.')
         {  m=0;
           for(i=1;i<4;i++)
          { if(arr[i][i]==ch||arr[i][i]=='T')
             m++;
          if(m==3)
          { win=ch; break ;};
          }
          }
      }
    //  cout<<win<<" left d\n";
   }
  
   if(win=='D')  //right diagonal
   {  ch=arr[0][3];
      if(ch!='.')
      {
         if(ch=='T')
          ch=arr[1][2];
         if(ch!='.')
         { m=0;
         for(i=1;i<4;i++)
         { if(arr[i][3-i]==ch||arr[i][3-i]=='T')
             m++;
         if(m==3)
         { win=ch; break ;};
         }
         }
      }
    // cout<<win<<" right d\n";
   }
   for(i=0;i<4;i++)
   { for(k=0;k<4;k++)
     if(arr[i][k]=='.')
     dot++;
   }
   if(win=='X'||win=='O')
   cout<<"Case #"<<j+1<<": "<<ch<<" won\n";
   else if(dot>0)
   cout<<"Case #"<<j+1<<": Game has not completed\n";
   else cout<<"Case #"<<j+1<<": Draw\n";
}
  // system("pause");
}




