#include<iostream>

using namespace std;

long long t,n,a[1001],b[1001],cost,at,bt;
void swap()
{
  long long i,j;
  for(i=1;i<=n;i++)
    for(j=i;j<n;j++)
      {
	if(a[j]>a[j+1])
	  {
	    at = a[j+1];
	    bt = b[j+1];
	    a[j+1]= a[j];
	    b[j+1]= b[j];
	    a[j] = at;
	    b[j] = bt;
	  }
      }
  for(i=1;i<=n;i++)
    for(j=i;j<=n;j++)
      {
	if(b[i]>b[j])
	  {
	    //cout<<"\na[i],b[i]="<<a[i]<<","<<b[i];
	    //cout<<"\na[j],b[j]="<<a[j]<<","<<b[j];
	    cost++;
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
      cin>>n;
      for(i=1;i<=n;i++)
	{
	  cin>>a[i]>>b[i];
	}
      swap();
      cout<<"\nCase #"<<k<<": "<<cost;
      k++;
    }
  return 0;
}
