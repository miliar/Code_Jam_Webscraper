#include<iostream>

using namespace std;

long long c,n,k,b,t,test,x[100],v[100],f[100],tx,tv;
long long cost,chk;
/*
int check()
{
  long long i,j;
  for(j = n;j>=n-k+1;j--)
    {
      if(v[j]*t < b-x[j])
	{
	  //cout<<"\n j="<<j;
	  return -1;
	}
    }
  return 1;
}*/
void swap()
{
  long long i,c,chk,j,l,count=0;
  chk = 0;
  for(i=1;i<=n;i++)
    {
      if(v[i]*t>=b-x[i])
	chk++;
    }
  if(chk < k)
    {
      cost = -1;
      // return -1;
    }
  else
    {
      for(i=1;i<=n;i++)
	f[i] = 0;
      for(j=n;j>0;j--)
	{
	  //cout<<"\nt="<<t<<" v[j]="<<v[j]<<" b-x[j]="<<b-x[j];
	  if((v[j]*t) >=(b - x[j]))
	    {
	      f[j]=1; 
	      count++;
	      //cout<<"\n j ="<<j<<" count="<<count<<endl;
	      if(count == k)
		{
		  //cout<<"\nbreaking at j="<<j<<endl;
		  break;
		}
	    }
	}
      cost=0;
      for(c=j;c<=n;c++)
	for(i=n;i>=j;i--)
	  for(l=n-1;l>=j;l--)
	    {
	      if(f[i]==0 && f[i-1] == 1)
		{
		  f[i]=1;
		  f[i-1]=0;
		  //cout<<"\nthe nos are "<<i<<" "<<i-1<<endl; 
		  cost++;
		}
	    }
    }
}
	      
  
	      /*
void swap()
{
  long long c,j;
  chk = 0;
  cost = 0;
  for(c=1;c<=n;c++)
    {
      if(v[c]*t>=b-x[c])
	chk++;
    }
  if(chk < k)
    {
      cost = -1;
      // return -1;
    }
  else
    {
      // for(i = n;i>0;i--)
      //	for(j = i-1;j>0;j--)
      //	  {
      c = n;
      //cout<<"\n Check()"<<check();
      if(check() == 1)
	{
	  //cout<<"\nEntered";
	  cost =0;
	}
      else
	{
	  while(check() == -1)
	    {
	      j = c-1;
	      if(v[c]*t+x[c]<v[j]*t+x[j])
		{
		  tv=v[c];
		  tx=x[c];
		  v[c]=v[j];
		  x[c]=x[j];
		  v[j]=tv;
		  x[j]=tx;
		  //cout<<"\n i="<<c<<" and j ="<<j;
		  cost++;
		}
	      if(c == 1)
		c = n;
	      else
		c--;
	    }
	}
      // return cost;
    }
    }*/
int main()
{
  long long p,j,cos=0;
  cin>>test;
  p = 1;
  while(p <= test)
    {
      cost = 0;
      cin>>n>>k>>b>>t;
      for(j = 1;j<=n;j++)
	cin>>x[j];
      for(j = 1;j<=n;j++)
	cin>>v[j];
      cout<<"\nCase #"<<p<<": ";
      //cout<<"\n swap "<<swap();
      //cout<<cost;
      swap();
      //cout<<"\n cost ="<<cost;
      //cout<<"\n val "<<val;
      if(cost == -1)
	cout<<"IMPOSSIBLE";
      else
	cout<<cost;
      p++;
    }
  return 0;
}
