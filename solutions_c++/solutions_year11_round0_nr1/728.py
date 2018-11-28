#include <iostream>
#include<cmath>
#include <fstream>
using namespace std;

int main()
{
    char c;
    int t,ot,bt,op,bp,m,n,p,i;
    ifstream s;
    ofstream o("output1.txt");
    s.open("A-large.in");
    s>>t;
    i=0;
    while(i<t)
    {
              m=0;
              ot=0;
              bt=0;
              op=1;
              bp=1;
              s>>n;
              while(n--)
              {
                        s>>c>>p;
                        if(c=='O')
                        {
                                  if(m<ot+abs(p-op))m=ot+abs(p-op);
                                  ++m;
                                  ot=m;
                                  op=p;
                                  }
                                  else
                                  {
                                  if(m<bt+abs(p-bp))m=bt+abs(p-bp);
                                  ++m;
                                  bt=m;
                                  bp=p;
                                      }
                        }          
              o<<"Case #"<<i+1<<": "<<m<<endl;  
              ++i;                                 
              }
              s.close();
              o.close();
              //system("pause");
              return 0;
    }
