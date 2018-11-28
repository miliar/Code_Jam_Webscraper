//1792

#include<iostream>
using namespace std;
int main(void)
{
	
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
  long int n,k,t,s,j=1;
  cin>>t;
  while(t--)
  {
	  s=1;
	  cin>>n>>k;
	  for(int i=0;i<n;i++)
	  {
		  s*=2;
	  }
	  if(k%s==s-1)
	  {
		  cout <<"Case #"<<j++<<": ON"<<endl;
	  }
	  else
		  cout <<"Case #"<<j++<<": OFF"<<endl;
  }
  return 0;
}