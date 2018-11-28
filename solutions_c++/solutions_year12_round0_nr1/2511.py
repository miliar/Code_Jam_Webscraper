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
#define foreach(x...) _foreach(x)

typedef long long int huge;

const int inf = 0x3f3f3f3f;
const huge hugeinf = 0x3f3f3f3f3f3f3f3fll;//dois L's
const double eps = 1e-9;
char mapa[265];

string ent[3] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi", 
                 "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", 
                 "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
string ret[3] = {"our language is impossible to understand",
                 "there are twenty six factorial possibilities", 
                 "so it is okay if you want to just give up"};
char s[55555];

int main ()
{
  memset(mapa,0,sizeof(mapa));
  for(int i=0;i<3;i++){
    for(int j=0;j<ent[i].size();j++){
      mapa[ent[i][j]] = ret[i][j];
      //   printf("%s\n",ent[i]);
    }
  }
  mapa['q'] = 'z';
  mapa['z'] = 'q';
  for(int i='a';i<='z';i++){
    //printf("%c %c\n",i,mapa[i]?mapa[i]:'-');
    for(int j=i+1;j<='z';j++)
      if(mapa[i]==mapa[j])printf("fuuu\n");
  }
  if(mapa[' ']!=' ')printf("fuuu2\n");

  int tt;
  scanf("%d ",&tt);

  for(int pp=1;pp<=tt;pp++)
    {
      gets(s);
      for(int i=0;s[i];i++)
        s[i]=mapa[s[i]];
      printf("Case #%d: ",pp);
      printf("%s\n",s);
    }
  return 0;
}
