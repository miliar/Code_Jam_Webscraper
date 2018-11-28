#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#define FOR(a,b,c) for(int (a) = (b), _n = (c); (a) <= _n ; (a)++)
#define FORD(a,b,c) for(int (a) = (b), _n = (c) ; (a) >= _n ; (a)--)
#define FOR_N(a,b,c,n) for(int (a) = (b), _m = (n), _n = (c) ; (a) <= _n ; (a)+= _m )
#define FORD_N(a,b,c,n) for(int (a) = (b), _m = (n), _n = (c) ; (a) >= _n ; (a)-= _m)
#define EACH(v,it) for(__typeof(v.begin()) it = v.begin(); it != v.end() ; it++)
#define INF 200000000
#define MAX 1

using namespace std;

char str1[300] = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
char str2[300] = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";

int maps[300];

void init()
{
  int len = strlen(str1);
  memset(maps,-1,sizeof(maps));
  FOR(i,0,len-1)
  {
    maps[str1[i]] = str2[i];
  }
  maps['q'] = 'z';
  maps['z'] = 'q';
}

char data[2000];

int main()
{
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);
  int t;
  init();
  scanf("%d",&t);
  gets(data);
  FOR(ca,1,t)
  {
    gets(data);
    int len = strlen(data);
    FOR(i,0,len-1)
    {
      if(data[i] == ' ') continue;
      data[i] = maps[data[i]];
    }
    printf("Case #%d: %s\n",ca,data);
  }
  return 0;
}
