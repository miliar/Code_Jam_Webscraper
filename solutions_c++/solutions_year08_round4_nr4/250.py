#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int k;
string data;

int calc(int p[])
{ string t(data.size(),' ');
  int i,j;
  for(i=0;i<t.size();i+=k)
    for(j=0;j<k;++j) t[j+i]=data[p[j]+i];
  int res=1;
  for(i=1;i<t.size();++i) if(t[i]!=t[i-1]) ++res;
  return res;
}
int main()
{
  int ci,cn,i;
  cin>>cn;
  for(ci=1;ci<=cn;++ci)
  {
    cin>>k>>data;
    int p[5],rv=data.size();
    for(i=0;i<k;++i) p[i]=i;
    do
    { int r=calc(p);
      if(rv>r) rv=r;
    }while(next_permutation(p,p+k));
    cout<<"Case #"<<ci<<": "<<rv<<endl;
  }
}
