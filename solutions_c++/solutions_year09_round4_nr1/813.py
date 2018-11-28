#include <iostream>
#include <cstdio>
using namespace std;

int a[100],s,x;
int main()
{
  int T,c;
  cin>>T;
  for(c=1;c<=T;c++)
    {
      int i,j,n;
      char ch;
      cin>>n;
      for(i=0;i<n;i++)
	{
	  a[i]=0;
	  for(j=0;j<n;j++)
	    {
	      cin>>ch;
	      if(ch-'0')
		a[i]=j;
	    }
	}
      s=0;
      for(i=0;i<n;i++)
	{
	  if(a[i]>i)
	    {
	      j=i+1;
	      while(a[j]>i)
		j++;
	      for(;j>i;j--)
		{
		  x=a[j];
		  a[j]=a[j-1];
		  a[j-1]=x;
		  s++;
		}
	    }
	}
      cout<<"Case #"<<c<<": "<<s<<"\n";
    }
}


