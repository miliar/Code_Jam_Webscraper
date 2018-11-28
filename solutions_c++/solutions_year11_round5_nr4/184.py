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
vector<char> saida;
void printa(huge ret)
{
  saida.clear();
      while(ret>0)
	{
	  saida.push_back(ret&1?'1':'0');
	  ret>>=1;
	}
      reverse(all(saida));
}
void printamsm(huge ret)
{
  printa(ret);
  for(int i=0;i<(int)saida.size();i++)
    printf("%c",saida[i]);
  printf("\n");

}
int main()
{
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      huge alvo=0,alvo2=0;
      char ent[111];
      scanf(" %s",ent);
      for(int i=0;ent[i];i++)
	{
	  alvo<<=1;				
	  alvo2<<=1;
	  if(ent[i]=='1')alvo++;		
	  else if(ent[i]=='0')alvo2++;
	}
      huge ret=0;
      for(ret=1;;ret--)
	{
	  if(ret*ret>alvo*2)break;
	  huge tmp=(ret*ret);
	  tmp = alvo^tmp;
	  huge tmp2 = alvo2^(ret*ret);
	  //printa(ret*ret);
	  // printa(tmp);
	  //printa(alvo);
	  //printf("ddd\n");
	  if(((tmp&alvo)==0) && ((tmp2&alvo)==alvo))
	    {
	      huge m = ret*ret;
	      printa(m);
	      bool ok = true;
	      for(int i=0;ok && ent[i];i++)
		if(ent[i]!='?' && ent[i]!=saida[i])ok=false;
	      if(ok)break;
	    }
	}
      ret*=ret;
      printf("Case #%d: ",pp);
      printamsm(ret);
    }
  return 0;
}
