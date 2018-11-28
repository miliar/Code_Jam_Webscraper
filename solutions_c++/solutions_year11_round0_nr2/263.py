#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <functional>
#include <sstream>
#include <iostream>
#include <ctime>
#include <algorithm>
using namespace std;

#define DEBUG(x...) printf(x)
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define _foreach(it, b, e) for(__typeof__(b) it = (b); it != (e); ++it)
#define foreach(x...) _foreach(x)

typedef long long int huge;

const int inf = 0x3f3f3f3f;
const huge hugeinf = 0x3f3f3f3f3f3f3f3fll; // sao dois L's!!!
const double eps = 1e-9;

int opos[257][257];
char trans[257][257];
int pilha[5555];
int main()
{
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      memset(opos,0,sizeof(opos));
      memset(trans,0,sizeof(trans));
      int a,b,n,topo=0;
      scanf("%d",&a);
      for(int i=0;i<a;i++)
	{
	  char c1,c2,c3;
	  scanf(" %c %c %c",&c1,&c2,&c3);
	  trans[c1][c2]=trans[c2][c1]=c3;
	}
      scanf("%d",&b);
      for(int i=0;i<b;i++)
	{
	  char c1,c2;
	  scanf(" %c %c",&c1,&c2);
	  opos[c1][c2]=opos[c2][c1]=1;
	}
      scanf("%d",&n);
      for(int i=0;i<n;i++)
	{
	  char c;
	  scanf(" %c",&c);
	  while(topo && trans[pilha[topo-1]][c])
	    {
	      topo--;
	      c = trans[pilha[topo]][c];
	    }
	  pilha[topo++]=c;
       	  for(int j=0;j<topo-1;j++)
	    {
	      if(opos[c][pilha[j]])
		topo=0;
	    }
	  
	}
      printf("Case #%d: [",pp);
      for(int i=0;i<topo;i++)
	printf("%s%c",i?", ":"",pilha[i]);
      printf("]\n");
	
    }
  return 0;
}
