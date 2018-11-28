#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    int t,n,i,c,sum,mi,k;
    ifstream s;
    ofstream o("output2.txt");
    s.open("C-small-attempt0.in");
    s>>t;
    i=0;
    while(i<t)
    {
              s>>n;
              sum=0;
              k=0;
              mi=10000000;
              while(n--)
              {
                        s>>c;
                        sum+=c;
                        k^=c;
                        if(c<mi)mi=c;
                        }
              if(k==0)o<<"Case #"<<i+1<<": "<<sum-mi<<endl; 
              else o<<"Case #"<<i+1<<": NO"<<endl;  
              ++i;                                 
              }
              s.close();
              o.close();
              //system("pause");
              return 0;
    }
