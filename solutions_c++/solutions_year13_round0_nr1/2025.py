#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
 int t,n;
 scanf("%d",&t);
 n=t;
 string st;
 getline(cin,st);
 while(t--)
 {
  char ch[4][4];
  int g=0;
  for(int i=0;i<4;i++)
  { getline(cin,st);
    for(int j=0;j<4;j++)
    {ch[i][j]=st[j];
      if(ch[i][j]=='.')
      g=1;
    }
  }
  char ch1[4][4];
  int f=-1;
  int ar[4];
  //for(int i=0;i<4;i++)
  //ar[i]=-2;
  //ch1[0][0]=ch[0][0];
  for(int i=0;i<4;i++)
  { char pre=ch[i][0];
    f=-1;

    if(pre=='.')
     {f=-1;
      //g=1;
     }
     else{//int ll;
    for(int j=1;j<4;j++)
    { //cout<<"j "<<j<<" "<<pre<<endl;
      //cin>>ll; 
    if(j!=3)
      {
       if(pre=='T' && ch[i][j]=='X')
       { pre='X';
       }
       else if(pre=='T' && ch[i][j]=='O')
           { pre='O';
           }
       else if(ch[i][j]=='.')
          {  f=-1;
      //       g=1;
            break;
          }
       else if(ch[i][j]!=pre && ch[i][j]!='T')
        { f=-1;
          //g=1;
          break; 
        }
        //cout<<"pre "<<pre<<endl;
      }
      else { //cout<<"pre "<<pre<<endl; 
      if(ch[i][j]=='T')
              { cout<<" Case #"<<(n-t)<<": "<<pre<<" won"<<endl;
                f=1;
                break;
              }
              else if(ch[i][j]==pre)
                 {cout<<"Case #"<<(n-t)<<": "<<pre<<" won"<<endl;;
                  f=1;
                  break;
                 }
              else if(ch[i][j]=='.')
               { f=-1;
    //           g=1;
                 break;
               }
              
           }
           
    }
     }
     if(f==1)
     break;
   /* if(i==3)
    {
   // cout<<f<<endl;
    if(f==-1)
     cout<<"Case #"<<(n-t)<<": "<<"Draw"<<endl;
    else if(f==0)
     cout<<"Case #"<<(n-t)<<": "<<"Game has not completed"<<endl;
   
    } */
       }
      /* cout<<"rows ";
       for(int k=0;k<4;k++)
       cout<<ar[k]<<" ";
       cout<<endl;
  */
 // char ch1[4][4];
 if(f!=1)
 {
  f=-1;
  int ac[4];
  //for(int i=0;i<4;i++)
  //ac[i]=-2;
  //ch1[0][0]=ch[0][0];
  for(int j=0;j<4;j++)
  { char pre=ch[0][j];
    f=-1;
    if(pre=='.')
     {f=-1;
      //g=1;
     }
     else{
    for(int i=1;i<4;i++)
    { if(i!=3)
      {
       if(pre=='T' && ch[i][j]=='X')
       { pre='X';
       }
       else if(pre=='T' && ch[i][j]=='O')
           { pre='O';
           }
       else if(ch[i][j]=='.')
          {  f=-1;
     //         g=1;
            break;
          }
       else if(ch[i][j]!=pre && ch[i][j]!='T')
        { f=-1;
          break; 
        }
      }
      else { if(ch[i][j]=='T')
              { cout<<"Case #"<<(n-t)<<": "<<pre<<" won"<<endl;
                f=1;
                break;
              }
              else if(ch[i][j]==pre)
                 {cout<<"Case #"<<(n-t)<<": "<<pre<<" won"<<endl;;
                  f=1;
                  break;
                 }
              else if(ch[i][j]=='.')
               { f=-1;
   //              g=1;
                 break;
               }
              
           }
           
    }
    if(f==1)
     break;
   
     }
     /* if(i==3)
    {
   // cout<<f<<endl;
    if(f==-1)
     cout<<"Case #"<<(n-t)<<": "<<"Draw"<<endl;
    else if(f==0)
     cout<<"Case #"<<(n-t)<<": "<<"Game has not completed"<<endl;
   
    } */
       }
    /*   cout<<"coloumns ";
       for(int i=0;i<4;i++)
       cout<<ac[i]<<" ";
       cout<<endl;*/
 }
 if(f!=1)
 { char pre=ch[0][0];
   f=-1;
   int d[2];
  for(int i=1;i<4;i++)
  { if(i==3)
      {
       if(ch[i][i]=='T' || ch[i][i]==pre)
     {cout<<"Case #"<<(n-t)<<": "<<pre<<" won"<<endl;
       f=1;
       break;
     }
      }
  else if(pre=='T' && ch[i][i]=='X')
     pre='X';
     else if(pre=='T' && ch[i][i]=='O')
     pre='O';
     else if(ch[i][i]!=pre && ch[i][i]!='T')
         {
           f=-1;
           break;
         }
     else if(ch[i][i]=='.')
     { f=-1;
       //g=1;
       break;
     }
     
     
  }
    d[0]=f;
    pre=ch[0][3];
    if(f!=1)
    for(int i=3;i>=0;i--)
	{ if(i==0)
     {
      if(ch[4-i-1][i]=='T' || ch[4-i-1][i]==pre)
     {cout<<"Case #"<<(n-t)<<": "<<pre<<" won"<<endl;
       f=1;
       break;
     }
     }
	else if(pre=='T' && ch[4-i-1][i]=='X')
     pre='X';
     else if(pre=='T' && ch[4-i-1][i]=='O')
     pre='O';
     else if(ch[4-i-1][i]!=pre && ch[4-i-1][i]!='T')
         {f=-1;
          break;
         }
     else if(ch[4-i-1][i]=='.')
     { f=-1;
      // g=1;
       break;
     }
     }	

    d[1]=f;   
 }
 if(f!=1)
 {
 if(g==1)
 cout<<"Case #"<<(n-t)<<": "<<"Game has not completed"<<endl;
 else
 cout<<"Case #"<<(n-t)<<": "<<"Draw"<<endl;
  }     
  /*
  for(int i=0;i<4;i++)
  {for(int j=0;j<4;j++)
  cout<<ch[i][j];
  cout<<endl;
  }*/
  //cout<<endl;
  getline(cin,st);
  //cin>>t;
 }
}
