#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <string>
#include <list>
#include <stack>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <utility>
#include <list>
#define INF 0x3fffffff


typedef long long ll;
#define PII pair<int, int>
#define PLL pair<ll, ll>
#define PDD pair<double, double>
#define PIL pair<int, ll>
#define PLI pair<ll, int>
#define PID pair<int, double>
#define PDI pair<double, int>
#define PLD pair<ll, double>
#define PDL pair<double, ll>

#define PQ(x) priority_queue< x >  //highest first
#define PQR(x) priority_queue< x , vector< x > , greater < x > > //lowest first
#define V(x) vector< x > 
#define L(x) list< x > 
#define MP make_pair
#define PB push_back
#define IT(x) for (typeof((x).begin()) it = (x).begin() ; it != (x).end() ; it++)
#define IT2(x) for (typeof((x).begin()) it2 = (x).begin() ; it2 != (x).end() ; it2++)
#define FOR(i, a, b) for (int i = (a) ; i< (b) ; i++)

using namespace std;

int gi() {  int t;  scanf("%i ", &t); return t; }
ll gll() {  ll t;  scanf("%lli ", &t); return t; }
double gd() {  double t;  scanf("%lf ", &t); return t; }


#define MAXD 5005
#define MAXL 18
int words[MAXD][MAXL];
int tmpw[MAXL];

int n,d,l;

bool match(int j)
{
  FOR(i,0,l)
    if ( (tmpw[i] & words[j][i]) == 0)
      return false;
  return true;
}

void testc(int t)
{
  int sum=0;

  FOR(i,0,l)
    {
      tmpw[i] = 0;
      char c = getchar();

      if (c!='(')
        tmpw[i] = (1<<(c-'a'));
      else
        while(1)
          {
            c = getchar();
            if (c==')') break;

            tmpw[i] |= (1<<(c-'a'));
          }
    }
  scanf(" ");
  
  FOR(i,0,d)
    if (match(i))
      sum++;

  printf("Case #%i: %i\n",t,sum);
}


int main()
{
  scanf("%i %i %i ", &l, &d, &n);
  
  memset(words, 0, sizeof(words));

  char tmp[ MAXL ];
  FOR(i,0,d)
    {
      gets(tmp);
      FOR(j,0,l)
        words[i][j] = (1<<(tmp[j])-'a');

      
    }

  FOR(i,0,n)
    testc(i+1);
  return 0;
}
