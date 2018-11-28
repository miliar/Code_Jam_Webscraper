#include <iostream>
#include<algorithm>
#include<string>
#include<math.h>
#define N 1000
#include <fstream>


using namespace std;

int main()
{
    int  t,n,i,j,k,r,a[N],b[N];
    ifstream s;
    ofstream o("output1.txt");
    s.open("A-large.in");
    s>>t;
    i=0;
    while(i<t)
    {
              s>>n;
              j=0;
              while(j<n)
              {
                        s>>a[j]>>b[j];
                        ++j;
                        }
              j=0;
              r=0;
              while(j<n)
              {
                        k=j+1;
                        while(k<n)
                        {
                            if((a[j]<a[k]&&b[j]>b[k])||(a[j]>a[k])&&b[j]<b[k])
                            {
                                                    ++r;
                                                    ++k;
                                                    }
                             else ++k;      
                                  }
                                  ++j;
                        }          
              o<<"Case #"<<i+1<<": "<<r<<endl;  
              ++i;                                 
              }
              s.close();
              o.close();
              system("pause");
              return 0;
    }
