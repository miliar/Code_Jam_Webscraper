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


char* sent = "welcome to code jam";
int slen = 19;
int sum[20];
char line[505];

void testc(int tc)
{
  memset(sum,0,sizeof(sum));
  
  gets(line);
  int llen=strlen(line);
  FOR(i,0,llen)
    for (int j=slen-1;j>=0;j--)
      if (sent[j] == line[i])
        {
          if (j>0)
            sum[j]+=sum[j-1];
          else
            sum[j]++;
          sum[j]%=10000;
        }
  
  printf("Case #%i: ",tc);

  int tot = sum[slen - 1];

  if (tot<1000) printf("0");
  if (tot<100) printf("0");
  if (tot<10) printf("0");
  printf("%i\n",tot);
  return;
}


int main()
{
  int tc;
  scanf("%i ", &tc);
  FOR(i,0,tc)
    testc(i+1);
  return 0;
}
