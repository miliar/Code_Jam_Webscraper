#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int c[20];

int lsum;
int rsum;
int lnum;
int n;
int maxx = -1;
void foo(int i, int lsum, int rsum, int lxor,int rxor)
{
  //cout<<"come here "<<i<<" "<<n<<endl;
  if(i==n)
  {
    
    if(lsum!=0&&rsum!=0 && lxor == rxor)
      maxx =maxx>rsum?maxx:rsum;
    return;
  }
  foo(i+1,lsum+c[i],rsum,lxor^c[i],rxor);
  foo(i+1,lsum,rsum+c[i],lxor,rxor^c[i]);
}


int main()
{
  freopen("in.txt","r",stdin);
  int T;
  
  cin>>T;
  for(int idx=1;idx<=T;++idx)
  {
    cin>>n;
    for(int i=0;i<n;++i)
    {
      cin>>c[i];
    }
    maxx=-1;
    foo(0,0,0,0,0);
    cout<<"Case #"<<idx<<": ";
    if(maxx==-1)
      cout<<"NO"<<endl;
    else cout<<maxx<<endl;
  }
}
