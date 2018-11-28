#include<iostream>
#include<fstream>
using namespace std;
ifstream fin("in.txt");
ofstream fout("out.txt");

int main()
{
    int T;
    fin>>T;
    for(int tt=0;tt<T;tt++)
    {
       int n,a;
       fin>>n;
       double ans=n;
       for(int i=1;i<=n;i++)
       {
          fin>>a;
          if(a==i) ans--;
       }
       fout<<"Case #"<<tt+1<<": "<<ans<<endl;
    }
}
