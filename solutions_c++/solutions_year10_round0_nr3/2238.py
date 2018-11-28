#include <iostream>
#include <fstream>


using namespace std;

int main()
{
    int t,n,i,j,k,r,g[1000],sum,m,temp[1000],p,q;
    ifstream s;
    ofstream o("output.txt");
    s.open("C-small-attempt0.in");
    s>>t;
    i=0;
    while(i<t)
    {
              s>>r>>k>>n;
              j=0;
              while(j<n)
              {
                        s>>g[j];
                        ++j;
                        }
                        sum=0;
                        j=0;
                        while(j<r)
                        {
                              m=0;
                              q=0;
                              while(m<n)
                              {
                                               sum=sum+g[m];
                                               q=q+g[m];
                                               if(q<=k)
                                               {
                                                         temp[m]=g[m];
                                                         ++m;
                                                         }
                                               else break;
                                               }
                                               p=m;
                                               if(m==n)break;
                                                         else
                                                         {
                                                             sum=sum-g[m];
                                                             while(p<n)
                                                             {
                                                                       g[p-m]=g[p];
                                                                       ++p;
                                                                       }
                                                                       p=0;
                                                                       while(p<m)
                                                                       {
                                                                                 g[n-m+p]=temp[p];
                                                                                 ++p;
                                                                                 }   
                                                             }
                                                             //cout<<j<<" "<<sum<<" "<<g[0]<<g[1]<<g[2]<<g[3]<<endl;
                                                             ++j;
                                  }
                                  if(m==n)o<<"Case #"<<i+1<<": "<<sum*r<<endl;
                                  else o<<"Case #"<<i+1<<": "<<sum<<endl;
                                  ++i;
                                                 
              }
              s.close();
              o.close();
              //system("pause");
              return 0;
    }
