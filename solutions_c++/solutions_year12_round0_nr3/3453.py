#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <stdlib.h>
using namespace std;

#define FOR(i,v,n) for(int i=v;i<=n;i++)

int T;
int A,B;
int processed[10000000];
int power[]={1,10,100,1000,10000,100000,1000000,10000000,100000000};

int process(int n,int len)
{
  processed[n]=1;
  int newn;
  int div,mul;
  int counter=0;
  int dig=n%10,okay=0;
  newn=n/10;
  
  while(newn)
    {
      if(dig!=newn%10)
	okay=1;
      newn/=10;
    }
  
  if(!okay)
    return 0;
  mul=10;
  div=power[len-1];
  FOR(l,1,len-1)
    {
      newn=(n%div)*mul + n/div;

      if(newn<=B && newn>n && n%div>=div/10)
	{
	  counter++;
	  processed[newn]=1;
	  //cout<<'('<<n<<','<<newn<<")\n";
	}
      div/=10;
      mul*=10;
    }
  return (counter*(counter+1))/2;
}

int main()
{
  cin>>T;
  int counter;
  char buff[20];
  FOR(_t,1,T)
    {
      cin>>A>>B;
      counter=0;
      memset(processed,0,sizeof(processed));
      sprintf(buff,"%d",A);
      int len=strlen(buff);
      FOR(i,A,B-1)
	if(!processed[i])
	  counter+=process(i,len);
      cout<<"Case #"<<_t<<": "<<counter<<endl;
    }
  return 0;
}
