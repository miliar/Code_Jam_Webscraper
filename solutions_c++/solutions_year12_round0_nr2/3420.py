#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define FOR(i,v,n) for(int i=v;i<=n;i++)

int T;
int t[105];
int S,p,N;

int main()
{
  cin>>T;
  int counter=0;
  FOR(_t,1,T)
    {
      counter=0;
      cin>>N>>S>>p;
      FOR(n,0,(N-1))
	cin>>t[n];
      sort(t,t+N);
      int i=N-1;
      int lowt=p+2*(p-2);
      lowt = (lowt>=0?lowt:p);

      while(i>=0 && t[i]>=lowt)
	{
	  if(t[i]>lowt+1)
	    counter++;
	  else if(S-->0 || p<=1)
	    counter++;
	  i--;
	}
      cout<<"Case #"<<_t<<": "<<counter<<endl;
    }
  return 0;
}
