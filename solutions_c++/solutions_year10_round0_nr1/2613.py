#include<iostream>

using namespace std;
long long val(long long n)
{
  if(n == 1)
    return 1;
  else
    return 2*val(n-1)+1;
}
int chk(long long n,long long k)
{
  long long m;
  if(n == 1)
    {
      if(k%2 == 0)
	return 0;
      else 
	return 1;
    }
  else
    {
      m = val(n);
      if(k == m)
	return 1;
      else if(k > m)
	{
	  if((k-m)%(m+1) == 0)
	    return 1;
	  else
	    return 0;
	}
      else
	return 0;
    }
}

int main()
{
  long long t,n,k,cnt,ch;
  cin>>t;
  cnt = 0;
  while(cnt<t)
    {
      cnt++;
      cin>>n>>k;
      ch = chk(n,k);
      if(ch == 1)
	cout<<"\nCase #"<<cnt<<": ON";
      else
	cout<<"\nCase #"<<cnt<<": OFF";
    }
  return 0;
}
