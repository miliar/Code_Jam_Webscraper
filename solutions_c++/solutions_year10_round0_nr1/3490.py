#include <stdio.h>
#include <iostream>
using namespace std;


int main()
{
int tc;
long long n,k,mask,kk;
cin>>tc;
for(int i=1;i<=tc;++i)
{
  cin>>n>>k;
  mask= (1<<n)-1;
  kk= (k&mask);
  cout<<"Case #"<<i<<": ";
//  cout<<"kk=="<<kk<<" mask=="<<mask<<endl;
  if(kk==mask) {
	cout<<"ON\n";
  } else cout<<"OFF\n";

}

}
