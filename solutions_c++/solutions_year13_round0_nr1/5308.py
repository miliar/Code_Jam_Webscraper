#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
 int t,n;
 //scanf("%d",&t);
 ifstream fin;
 ofstream fout;
 fin.open("input11.txt");
 fout.open("output11.txt");
 fin>>t;
 n=t;
 string st;
// getline(cin,st);
// fin>>st;
 while(t--)
 {
  char ch[4][4];
  int g=0;
  for(int i=0;i<4;i++)
  {// getline(cin,st);
  fin>>st;
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
  { char p=ch[i][0];
    f=-1;

    if(p=='.')
     {f=-1;
      //g=1;
     }
     else{//int ll;
    for(int j=1;j<4;j++)
    { //fout<<"j "<<j<<" "<<p<<endl;
      //cin>>ll; 
    if(j!=3)
      {
       if(p=='T' && ch[i][j]=='X')
       { p='X';
       }
       else if(p=='T' && ch[i][j]=='O')
           { p='O';
           }
       else if(ch[i][j]=='.')
          {  f=-1;
      //       g=1;
            break;
          }
       else if(ch[i][j]!=p && ch[i][j]!='T')
        { f=-1;
          //g=1;
          break; 
        }
        //fout<<"p "<<p<<endl;
      }
      else { //fout<<"p "<<p<<endl; 
      if(ch[i][j]=='T')
              { fout<<"Case #"<<(n-t)<<": "<<p<<" won"<<endl;
                f=1;
                break;
              }
              else if(ch[i][j]==p)
                 {fout<<"Case #"<<(n-t)<<": "<<p<<" won"<<endl;;
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
  
       }
     
 if(f!=1)
 {
  f=-1;
  int ac[4];
 
  for(int j=0;j<4;j++)
  { char p=ch[0][j];
    f=-1;
    if(p=='.')
     {f=-1;
      //g=1;
     }
     else{
    for(int i=1;i<4;i++)
    { if(i!=3)
      {
       if(p=='T' && ch[i][j]=='X')
       { p='X';
       }
       else if(p=='T' && ch[i][j]=='O')
           { p='O';
           }
       else if(ch[i][j]=='.')
          {  f=-1;
  
            break;
          }
       else if(ch[i][j]!=p && ch[i][j]!='T')
        { f=-1;
          break; 
        }
      }
      else { if(ch[i][j]=='T')
              { fout<<"Case #"<<(n-t)<<": "<<p<<" won"<<endl;
                f=1;
                break;
              }
              else if(ch[i][j]==p)
                 {fout<<"Case #"<<(n-t)<<": "<<p<<" won"<<endl;;
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
   
       }
    
 }
 if(f!=1)
 { char p=ch[0][0];
   f=-1;
   int d[2];
  for(int i=1;i<4;i++)
  { if(i==3)
      {
       if(ch[i][i]=='T' || ch[i][i]==p)
     {fout<<"Case #"<<(n-t)<<": "<<p<<" won"<<endl;
       f=1;
       break;
     }
      }
  else if(p=='T' && ch[i][i]=='X')
     p='X';
     else if(p=='T' && ch[i][i]=='O')
     p='O';
     else if(ch[i][i]!=p && ch[i][i]!='T')
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
    p=ch[0][3];
    if(f!=1)
    for(int i=3;i>=0;i--)
	{ if(i==0)
     {
      if(ch[4-i-1][i]=='T' || ch[4-i-1][i]==p)
     {fout<<"Case #"<<(n-t)<<": "<<p<<" won"<<endl;
       f=1;
       break;
     }
     }
	else if(p=='T' && ch[4-i-1][i]=='X')
     p='X';
     else if(p=='T' && ch[4-i-1][i]=='O')
     p='O';
     else if(ch[4-i-1][i]!=p && ch[4-i-1][i]!='T')
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
 fout<<"Case #"<<(n-t)<<": "<<"Game has not completed"<<endl;
 else
 fout<<"Case #"<<(n-t)<<": "<<"Draw"<<endl;
  }     
 
 }
 fout.close();
 return 0;
}
