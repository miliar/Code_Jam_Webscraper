#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define FOR(i,v,n) for(int i=v;i<=n;i++)

int T;
char G[105];

char conv[30]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z', 't','n','w','j','p','f','m','a','q',0};

void parse(char *s)
{
  while(*s)
    {
      int i=0;
      while(conv[i])
	{
	  if(i==*s-'a')
	    {
	      *s=conv[i];
	      break;
	    }
	  ++i;
	}
      ++s;
    }
}

int main()
{
  cin>>T;
  gets(G);
  FOR(t,1,T)
    {
      gets(G);
      parse(G);
      cout<<"Case #"<<t<<": "<<G<<endl;
    }
  return 0;
}
