#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
typedef long long ll;
#define PB push_back
int main()
{
ifstream fin;
fin.open("C:\\data\\A-small-attempt0.in");
ofstream fout;
fout.open("C:\\data\\as.txt");
int t;
fin>>t;
ll a,b,c,d,x,y,m;
int n;
long long ret=0;
for(int cas=1;cas<=t;++cas)
{
ret=0;
  fin>>n>>a>>b>>c>>d>>x>>y>>m;
  vector<ll> X,Y;
  X.PB(x);Y.PB(y);
  for(int i=1;i<n;++i)
  {
    x=((a*x)%m+b%m)%m;
    y=((c*y)%m+d%m)%m;
    X.PB(x);Y.PB(y);         
   }
   for(int i=0;i<n;++i)
    for(int j=i+1;j<n;++j)
        for(int k=j+1;k<n;++k)
            {
                if((X[i]+X[j]+X[k])%3==0 && (Y[i]+Y[j]+Y[k])%3==0)
                    ret++;
            }
    fout<<"Case #"<<cas<<": "<<ret<<endl;
} 
fin.close();
fout.close();
return 0;    
}
