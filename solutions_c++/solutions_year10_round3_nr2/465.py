#include<iostream>

using namespace std;

long long t,l,p,c,cost,val,ctr;
void swap()
{
  long long ct;
  if(p%l == 0)
    val = p/l;
  else
    {
      val = p/l;
      val++;
    }
  ctr = 0;
  ct = 1;
  //cout<<"\n val = "<<val;
  while(ct<val)
    {
      ct *= c;
      ctr++;
    }
    //cout<<"\nCtr = "<<ctr;
    while(ctr>1)
      {
	cost++;
	if(ctr%2 == 0)
	  ctr /=2;
	else
	  {
	    ctr /=2;
	    ctr++;
	  }
      }
    
}
int main()
{
  long long k,i,j;
  cin>>t;
  k = 1;
  while(k<=t)
    {
      cost = 0;
      cin>>l>>p>>c;
      swap();
      cout<<"\nCase #"<<k<<": "<<cost;
      k++;
    }
  return 0;
}
