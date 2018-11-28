#include <iostream>
#include <fstream>


using namespace std;

int main()
{
    int t,n,i,j,k;
    long long sum,a[29]={1,2,4,8,16,32,64,128,256,512,
    1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,
    1048576,2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456};
    ifstream s;
    ofstream o("output.txt");
    s.open("A-large.in");
    s>>t;
    i=0;
    while(i<t)
    {
              s>>n>>k;
              sum=0;
              j=0;
              while(j<n)
              {
                        sum=sum+a[j];
                        ++j;
                        }
                        if(k<sum)
                        {
                                 o<<"Case #"<<i+1<<": OFF"<<endl;
                                 ++i;
                                 continue;
                                 }
                                 else
                                 {
                                     k=k-sum;
                                     k=k%a[n];
                                     if(k==0)
                                     {
                                             o<<"Case #"<<i+1<<": ON"<<endl;
                                             ++i;
                                             continue;       
                                             }
                                             else
                                             {
                                                 o<<"Case #"<<i+1<<": OFF"<<endl;
                                                 ++i;
                                                 continue;
                                                 }
                                     }                              
              }
              s.close();
              o.close();
              //system("pause");
              return 0;
    }
