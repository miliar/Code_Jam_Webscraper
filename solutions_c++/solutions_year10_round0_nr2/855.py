#include<iostream>
using namespace std;

int gcd(int a,int b);

int main()
{
    int t,i;
    
    cin>>t;
    
    for(i=0;i<t;i++)
    {
      int n,j,temp,k;
      cin>>n;
      
      int a[n],min,max;
      
      for(j=0;j<n;j++)
	cin>>a[j];
      
      
      for(j=0;j<n-1;j++)
      {
	for(k=0;k<n-j-1;k++)
	{
	  if(a[k+1]<a[k])
	  {
	    temp=a[k];
	    a[k]=a[k+1];
	    a[k+1]=temp;
	  }
	}
      }
      int diff[n-1];
      
      for(j=0;j<n-1;j++)
	diff[j]=a[j+1]-a[j];
      
      int gd=gcd(diff[0],diff[0]);
      
      for(j=1;j<n-1;j++)
	gd=gcd(gd,diff[j]);
      
      int tem=gd;     
      
      for(;tem<a[0];tem+=gd);
      
      cout<<"Case #"<<i+1<<": "<<(tem-a[0])<<"\n";
      
    }
    return 0;
}

int gcd (int a,int b)
{
  if(b==0)
    return a;
  else
    return gcd(b,a%b);
}
