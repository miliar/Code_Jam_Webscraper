#include <stdio.h>
#include <ctype.h>
#include <iostream>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <stdlib.h>
#include <time.h>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <assert.h>

//#define M_PI 3.141592653589793238462643
#define eps 1e-8
#define inf ((int)1e9)
#define pb push_back
#define mp make_pair

using namespace std;

vector <int> P[26];
char s[1200];
int len, res, D[40][2];
bool A[50][50];

void add (char c, int d)
{
  P[(int)(c-'a')].pb(26+d);
}

int main()
{
  int tst, cnt, i, j, k, len, x, y;
  freopen(".in", "r", stdin);
  freopen(".out", "w", stdout);
  add('o',0);
  add('i',1);
  add('e',3);
  add('a',4);
  add('s',5);
  add('t',7);
  add('b',8);
  add('g',9);
  for (i=0; i<26; i++)
    P[i].pb(i);
  scanf("%d", &tst);
  for (cnt=1; cnt<=tst; cnt++)
  {
    memset(D,0,sizeof(D)), res=0;
    memset(A,0,sizeof(A));
    scanf("%d ", &k), gets(s), len=strlen(s);
    //puts(s);
    for (i=0; i<len-1; i++)
    {
      x=(int)(s[i]-'a'), y=(int)(s[i+1]-'a');
      for (j=0; j<(int)P[x].size(); j++)
        for (k=0; k<(int)P[y].size(); k++)
          if (!A[P[x][j]][P[y][k]])
            A[P[x][j]][P[y][k]]=1, D[P[x][j]][0]++, D[P[y][k]][1]++;
    }
    //for (i=12; i<=26; i++)
    //  cerr<<"!!!   "<<D[i][0]<<" "<<D[i][1]<<endl;
    //cerr<<endl;
    for (i=0; i<36; i++)
      res+=max(0,D[i][0]-D[i][1]);
    if (res==0)
      res=1;
    for (i=0; i<36; i++)
      res+=D[i][0];
    printf("Case #%d: %d\n", cnt, res);
  }
  return 0;
}
