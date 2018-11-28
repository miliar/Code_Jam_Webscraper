#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int main()
{
int t,i,j,dot,x,o,tic,flag,count=1;
cin>>t;
string s;
while(t--)
{
          dot=0;
          char a[4][4];
          for(i=0;i<4;i++)
          { cin>>s;
          for(j=0;j<4;j++)
          {a[i][j]=s[j];
          if(a[i][j]=='.')
          dot=1;
          }
          }
          flag=0;
          for(i=0;i<4;i++)
          {
                  x=o=tic=0;        
                  for(j=0;j<4;j++)
                  {
                          if(a[i][j]=='X')
                          x++;
                          if(a[i][j]=='O')
                          o++;
                          if(a[i][j]=='T')
                          tic++;        
                                  }   
                   if((x==3 && tic==1) || x==4)
                   flag=1;    
                   else if((o==3 && tic==1) || o==4)
                   flag=2;
                          }
          if(flag==0)
          {
                 for(j=0;j<4;j++)
                 {
                  x=o=tic=0;        
                  for(i=0;i<4;i++)
                  {
                          if(a[i][j]=='X')
                          x++;
                          if(a[i][j]=='O')
                          o++;
                          if(a[i][j]=='T')
                          tic++;        
                                  }   
                   if((x==3 && tic==1) || x==4)
                   flag=1;    
                   else if((o==3 && tic==1) || o==4)
                   flag=2;
                          }    
                     }
          x=o=tic=0;
          if(flag==0)
          for(i=0;i<4;i++)
          {
                  if(a[i][i]=='X')
                  x++;
                  else if(a[i][i]=='O')
                  o++;
                  else if(a[i][i]=='T')
                  tic++;        
                          }   
           if((x==3 && tic==1) || x==4)
           flag=1;    
           else if((o==3 && tic==1) || o==4)
           flag=2; 
           x=o=tic=0;
           j=3;
           if(flag==0)
           for(i=0;i<4;i++)
           {
                    if(a[i][j]=='X')
                    x++;
                    else if(a[i][j]=='O')
                    o++; 
                    else if(a[i][j]=='T')
                    tic++;  
                    j--;    
                           }
            if((x==3 && tic==1) || x==4)
           flag=1;    
           else if((o==3 && tic==1) || o==4)
           flag=2;               
                                 
          if(flag==1)
          cout<<"Case #"<<count++<<": X won"<<endl;
          else if(flag==2)
          cout<<"Case #"<<count++<<": O won"<<endl;
          else if(dot==0)
          cout<<"Case #"<<count++<<": Draw"<<endl;
          else
          cout<<"Case #"<<count++<<": Game has not completed"<<endl;
          }
return 0;
}
