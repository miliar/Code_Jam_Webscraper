#include<iostream>
#include<algorithm>
#include<functional>
#include<cmath>
#include<math.h>
#include<string.h>
#include<string>
# include<fstream>
using namespace std;
int main ()
{     int i,j,k,l,n,m,p,t,u,v,q,s,f,r;
      char a[4][4];
      string w;
       ifstream fin;
       ofstream fout;
       fin.open("Input.txt");
       fout.open("Output.txt");
       fin>>n;
     //  cout<<n;
       q=1;
       while(q<=n)
       {                f=0;
                        for(i=0; i<4; i++)
                         for(j=0; j<4; j++)
                         {
                          fin>>a[i][j];
                          if(a[i][j]=='.')
                          f=1;
                          }
                          u=0; v=0; 
                          for(i=0; i<4; i++)
                          { m=0; k=0; r=0;
                           for(j=0; j<4; j++)
                           {
                             if(a[j][i]=='X')
                              m++;
                              else if(a[j][i]=='O')
                              k++;
                              else if(a[j][i]=='T')
                              r++;
                           }
                            if(m==4||(m==3&&r==1))
                            {
                            u++;
                            break;
                            }
                            else if(k==4||(k==3&&r==1))
                            {
                            v++;
                            break;
                            }
                           }
                           for(i=0; i<4; i++)
                           { m=0; k=0; r=0;
                            for(j=0; j<4; j++)
                            {
                             if(a[i][j]=='X')
                              m++;
                              else if(a[i][j]=='O')
                              k++;
                              else if(a[i][j]=='T')
                              r++;
                            }
                            if(m==4||(m==3&&r==1))
                            {
                            u++;
                            break;
                            }
                            else if(k==4||(k==3&&r==1))
                            {
                            v++;
                            break;
                            }
                           }
                           m=0; k=0; r=0;
                          for(j=0; j<4; j++)
                            {
                             if(a[j][j]=='X')
                              m++;
                              else if(a[j][j]=='O')
                              k++;
                              else if(a[j][j]=='T')
                              r++;
                            }
                            if(m==4||(m==3&&r==1))
                            {
                            u++;
                            
                            }
                            else if(k==4||(k==3&&r==1))
                            {
                            v++;
                            
                            }
                            m=0; k=0; r=0;
                            p=3;
                          for(j=0; j<4; j++)
                            {
                             if(a[j][p]=='X')
                              m++;
                              else if(a[j][p]=='O')
                              k++;
                              else if(a[j][p]=='T')
                              r++;
                              p--;
                            }
                            if(m==4||(m==3&&r==1))
                            {
                            u++;
                           
                            }
                            else if(k==4||(k==3&&r==1))
                            {
                            v++;
                           
                            }
                           fout<<"Case #"<<q<<": "; 
                          if(u>v)
                          fout<<"X won\n";
                          else if(v>u)
                          fout<<"O won\n";
                          else if(u==v&&f==0)
                          fout<<"Draw\n";
                          else if(v==u&&f==1)
                          fout<<"Game has not completed\n";
                          
                          getline(fin,w);
                         // cout<<q;
                          q++;
         }  
       fin.close();
       fout.close();                     
                           
                           
//system("pause");
}
