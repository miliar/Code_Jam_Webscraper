#include<stdio.h>
#include<map>
#include<vector>
#include<iostream>
#include<algorithm>

using namespace std;

#define mod 1000000007
  
char a[10][10];
           
int dig2(int i,char ch)
{
    for(int j=1;j<4;j++)
       {
          if(a[j][3-j]==ch||a[j][3-j]=='T')
           {}
          else
            {return 0;}                     
      }
     
     return 1;
}
           
int dig1(int i,char ch)
{
    for(int j=1;j<4;j++)
       {
          if(a[j][j]==ch||a[j][j]=='T')
           {}
          else
            {return 0;}                     
      }
     
     return 1;
}
           
int side(int i,char ch)
{
    for(int j=1;j<4;j++)
       {
          if(a[i][j]==ch||a[i][j]=='T')
           {}
          else
            {return 0;}                     
      }
     
     return 1;
}


int down(int i,char ch)
{
    for(int j=1;j<4;j++)
       {
          if(a[j][i]==ch||a[j][i]=='T')
           {}
          else
            {return 0;}                     
      }
     
     return 1;
}


int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int t,n=1;
    cin>>t;
 while(t--)
 {
    int i,j;
    for(i=0;i<4;i++)
     scanf("\n%s",a[i]);  
    
      
      int rs=0;
      char ch;
      
        for(i=0;i<4;i++)
        {
            ch=a[0][i];
            if(ch!='.')
            rs=down(i,ch);
            if(rs)
            break;
            ch=a[i][0];
            if(ch!='.')
            rs=side(i,ch);
            if(rs)
            break;
        }
        if(rs)
        {cout<<"Case #"<<n<<": "<<ch<<" won"<<"\n"; n++;
         continue;
        }
      
      ch=a[0][0];
      if(ch!='.')
      rs=dig1(1,ch);
        if(rs)
        {cout<<"Case #"<<n<<": "<<ch<<" won"<<"\n"; n++;
         continue;
        }
      
      ch=a[0][3];
      if(ch!='.')      
      rs=dig2(1,ch);
        if(rs)
        {cout<<"Case #"<<n<<": "<<ch<<" won"<<"\n"; n++;
         continue;
        }
        
    int flag=0;
    for(i=0;i<4;i++)
        for(j=0;j<4;j++)
         {if(a[i][j]=='.') {flag=1;break; }
          }
          
      if(flag==1)
      {cout<<"Case #"<<n<<": "<<"Game has not completed"<<"\n";n++;}
      else
      {cout<<"Case #"<<n<<": "<<"Draw"<<"\n";n++;}            
    
      

}
//cin>>i;
return 0;    
}
