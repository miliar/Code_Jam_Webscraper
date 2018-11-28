#include<iostream>
#include<fstream>
#include<vector>
#include<string>
using namespace std;
ifstream fin("in.txt");
ofstream fout("out.txt");

int main()
{
    int T;
    fin>>T;
    for(int tt=0;tt<T;tt++)
    {
       unsigned int n,sum=0,vmin=10000000,xr=0,a;
       fin>>n;
       for(int i=0;i<n;i++)
       {
          fin>>a;
          sum+=a;
          xr^=a;
          vmin=min(vmin,a);
       }
       fout<<"Case #"<<tt+1<<": ";
       if(xr!=0) fout<<"NO"<<endl;
         else fout<<sum-vmin<<endl;
    }
}
