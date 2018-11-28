#include<iostream>
#include<iomanip>
#include <fstream>
using namespace std;

int main()
{
    int t,n,i,j,k,m,p;
    int a[1001],index[1001];
    ifstream in;
    ofstream o("output1.txt");
    in.open("D-large1.in");
    in>>t;
    i=1;
    while(i<=t)
    {
               in>>n;
               for(j=1;j<=n;++j)in>>a[j];
               memset(index,0,sizeof(index));
               m=0;
               for(j=1;j<=n;++j)
               {
                                if(!index[j])
                                {
                                             index[j]=1;
                                             for(p=0,k=j;a[k]!=j;k=a[k],++p)index[k]=1;
                                             index[k]=1;
                                             if(p)m+=p+1;
                                             }
                                }
                                 o<<"Case #"<<i<<": "<<setiosflags(ios::fixed)<<setprecision(6) <<1.0*m<<endl;
                                 ++i;
               }
               return 0;
    }
