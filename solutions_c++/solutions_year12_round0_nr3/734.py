#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstdlib>
#include<cstring>
#define LOCAL
using namespace std;
int main()
{
#ifdef LOCAL
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
#endif
int T;int flag;
cin>>T;
for(int tm=1;tm<=T;tm++)
{ int a,b;int dig,cas;
  int m[10]; cas=0;

    cin>>a>>b;
dig=log10(a);
for(int n=a;n<b;n++)
{ memset(m,0,sizeof(m));
    m[0]=n;int th; 
for(int i=dig;i>=1;i--)
{ th=pow(10,dig); flag=1;
  m[dig-i+1]=10*(m[dig-i]%th)+m[dig-i]/th;
for(int j=0;j<dig-i;j++)
{if(m[dig-i+1]==m[j]) flag=0;}
if(m[dig-i+1]>n&&m[dig-i+1]<=b&&flag)cas++;

}

}

cout<<"Case #"<<tm<<": "<<cas<<endl;

}

return 0;
}

