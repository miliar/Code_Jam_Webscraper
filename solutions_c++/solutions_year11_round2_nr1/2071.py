#include<iostream>
#include<cmath>
#include<string.h>
using namespace std;
int main()
{
  int t,c=1;
  cin>>t;
  while(t)
    {
      t--;
      int n;
      cin>>n;
      int a[n][n],i,j,k;
      for(i=0;i<n;i++)
	{
	  char inp[n+1];
	  cin>>inp;
	  for(j=0;j<n;j++)
	    {
	       if(inp[j]=='.')
		a[i][j]=-1;
		if(inp[j]=='0')
		a[i][j]=0;

		if(inp[j]=='1')
		a[i][j]=1;
	       	 
	    }
	}
      double rpi[n];
      double wp[n];
      double owp[n];
      double oowp[n];
      for(i=0;i<n;i++)
	{
	  double win=0,total=0;
	  for(j=0;j<n;j++)
	    {
	      if(a[i][j]!=-1)
		{
		  total++;
		  if(a[i][j]==1)win++;
		}
	    }
	wp[i]=(win/total);
	//cout<<r<<" ";
	}
	
      for(i=0;i<n;i++)
	{
	  double all=0;
	  double sum=0;
	  for(j=0;j<n;j++)
	    {
	       if(a[i][j]!=-1)
		{
		  all++;
		  double win=0,total=0;
		  for(k=0;k<n;k++)
		    {
		      if(k!=i)
			{
			  if(a[j][k]==0 || a[j][k]==1)
			    {
			      total++;
			      if(a[j][k]==1)win++;
			    }
			}
		    }
		  sum=sum+(win/total);
		}
	    }
	  owp[i]=sum/all;
	}
      for(i=0;i<n;i++)
	{
	  double all=0;
	  double sum=0;
	  for(j=0;j<n;j++)
	    {
	      if(a[i][j]!=-1)
		{
		  sum=sum+owp[j];
		  all++;
		}
	    }
	  oowp[i]=sum/all;
	}
      cout<<"Case #"<<c<<":\n";
      for(i=0;i<n;i++)
	{
	  double rpi=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
	  cout<<rpi<<"\n";
	}
      c++;
   }
}
