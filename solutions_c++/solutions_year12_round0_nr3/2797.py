#include<fstream>
#include<map>
#include<algorithm>
#include<string>
#include<sstream>
#include<iostream>
using namespace std;
ifstream fin("C.in");
ofstream fout("C.out");
int A,B;
long long recycle(int n)
{
    long long ret=0;
    map<int,bool> gn;
    gn.clear();
    int x=n,div=10,mod=10;
    while(n/div)
    {
        div*=10;
    }
    div=div/mod;
    while(n/mod)
    {
       x=(n%mod)*div;
       x+=n/mod;
       if(x>n&&x<=B&&!gn[x])
       {
          gn[x]=1;
          ret++;
       }
       mod*=10;
       div/=10;
    }
    return ret;
}
int main()
{
    int T;
    fin>>T;
    for(int c=1;c<=T;c++)
    {
         fin>>A>>B;
         long long res=0;
         for(int i=A;i<B;i++)
         {
              res+=recycle(i);
         }
         fout<<"Case #"<<c<<": "<<res<<endl;
    }
    return 0;
}
