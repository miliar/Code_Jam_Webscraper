#include <stdio.h>
#include <iostream>
using namespace std;
int nn,tot;
int tprime[1000100];
bool prime[1000100];
__int64 n;

int find(int n)
{
  int m=0;
  prime[1]=false;
  for(int i=2;i<=n;i++) prime[i]=true;
  for(int i=2;i<=n;i++)
  {
    if (prime[i])tprime[++m]=i;
    int t=n/i;
    for(int j=1;tprime[j]<=t;j++)
    {
      prime[i*tprime[j]]=false;
      if (i%tprime[j]==0) break;
    }
  }
  return m;
}

__int64 findans(__int64 n)
{
	if(n==1)return 0;
	__int64 ans=1;
	for(int i=1;i<=nn;i++)
	{
		__int64 tt=tprime[i];
		while(tt<=n/tprime[i])
		{
			ans++;
			tt*=tprime[i];
		}
	}
	return ans;
}

int main(int argc, char *argv[])
{
	freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
	cin>>tot;
	nn=find(1000000);
	for(int t=1;t<=tot;t++)
	{
		cin>>n;
		cout<<"Case #"<<t<<": "<<findans(n)<<endl;
	}
	return 0;
}
