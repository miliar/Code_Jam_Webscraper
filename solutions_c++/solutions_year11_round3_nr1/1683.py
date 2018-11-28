#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    int t,i,r,c,j,k,m,n;
    char a[55][55];
    ifstream s;
    ofstream o("output1.txt");
    s.open("A-large.in");
    s>>t;
    i=1;
    while(i<=t)
    {
              s>>r>>c;
              for(j=1;j<=r;++j)
                 for(k=1;k<=c;++k)
                     s>>a[j][k];
              for(j=1;j<=r;++j)
                 for(k=1;k<=c;++k)
                 {
                                  if(a[j][k]=='#'&&a[j][k+1]=='#'&&a[j+1][k]=='#'&&a[j+1][k+1]=='#')
                                  {
                                                                                                    a[j][k]='/';
                                                                                                    a[j][k+1]='\\';
                                                                                                    a[j+1][k]='\\';
                                                                                                    a[j+1][k+1]='/';
                                                                                                    }
                                  }
              m=1;
              for(j=1;j<=r;++j)
              {
                 for(k=1;k<=c;++k)
                 {
                                  if(a[j][k]=='#')
                                  {
                                                  m=0;
                                                  break;
                                                  }
                                  }
                                  if(!m)break;
                                  }
              if(m)
              {
                   o<<"Case #"<<i<<":"<<endl;
                   for(j=1;j<=r;++j)
                   {
                                    for(k=1;k<=c;++k)
                                    {
                                                     o<<a[j][k];
                                                     }
                                                     o<<endl;
                                    }
                   }
                   else 
                   {
                        o<<"Case #"<<i<<":"<<endl;
                        o<<"Impossible"<<endl;
                        }
              ++i;                               
              }
              s.close();
              o.close();
              //system("pause");
              return 0;
    }
