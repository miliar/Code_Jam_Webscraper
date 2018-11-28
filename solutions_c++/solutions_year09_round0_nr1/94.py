#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<list>
#include<deque>
#include<queue>
#include<stack>
#include<functional>
#include<sstream>
#include<iostream>
#include<ctime>
#include<algorithm>
using namespace std;

#define DEBUG(x...) printf(x)
#define allv(v) (v).begin(),(v).end()
#define rall(v) (v).begin(),(v).rend()
#define _foreach(it,b,e) for(__typeof__(b); it!=(e);++it)
#define foreach(x...)

typedef long long int huge;

const int inf = 0x3f3f3f3f;
const huge hugeinf = 0x3f3f3f3f3f3f3f3fll;//dois L's
const double eps = 1e-9;

int l,d,n;
char dict[5555][20];
char pode[20][30];
char pal[1000];
void solve(char *s)
{
  int flag=0;
  int i=0;
  int pos=0;
  while(s[i]!=0)
    {
      if(s[i]=='(')
	flag=1;
      else if(s[i]==')')
	{
	  flag=0;
	  pos++;
	}
      else if(flag)
	pode[pos][s[i]-'a']++;
      else
	pode[pos++][s[i]-'a']++;
      i++;
    }
}
int main ()
{
  scanf("%d %d %d",&l,&d,&n);
  
  for(int i=0;i<d;i++)
    {
      scanf(" %s",dict[i]);
      
    }
  for(int i=1;i<=n;i++)
    {
      int ret=0;
      scanf(" %s",pal);
      memset(pode,0,sizeof(pode));
      solve(pal);
      //printf("%s\n",pal);
      /* for(int j=0;j<l;j++)
	for(int k=0;k<26;k++)
	if(pode[j][k])printf(" %d %d ",j,k);*/
      for(int j=0;j<d;j++)
	{
	  int ok=1;
	  for(int k=0;k<l;k++)
	    if(!pode[k][dict[j][k]-'a'])
	      {
		ok=0;
		break;
	      }
	  if(ok)ret++;     
	}
      printf("Case #%d: %d\n",i,ret);
    }
  return 0;
}
