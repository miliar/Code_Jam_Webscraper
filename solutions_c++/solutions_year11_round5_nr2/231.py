#include <stdio.h>
#include <math.h>
#include <map>
#define inf 10000000
using namespace std;
int findmax(map<int,int> C)
{
  if(C.size()==0)
    return inf;
  //printf("%d\n",C.size());
  int top=(*C.begin()).first;
  //printf("top is %d\n",top);
  int optanswer=0;
  for(int i=1;;i++)
    {
      if(C.find(top+i-1)==C.end())
	break;
      map<int,int> Cnext=C;
      for(int j=top;j<=top+i-1;j++)
	{
	  Cnext[j]--;
	  if(Cnext[j]==0)
	    Cnext.erase(j);
	}
      optanswer=max(optanswer,min(i,findmax(Cnext)));

    }
  return optanswer;
}

int main()
{
  int T;
  scanf("%d",&T);
  for(int t=1;t<=T;t++)
    {
      int n;
      scanf("%d",&n);
      map<int,int> cts;
      for(int i=0;i<n;i++)
	{
	  int v;
	  scanf("%d",&v);
	  cts[v]++;
	}
      //printf("dsfs\n");
      int answer=findmax(cts);
      printf("Case #%d: %d\n",t,answer==inf?0:answer);
      
    }
}
