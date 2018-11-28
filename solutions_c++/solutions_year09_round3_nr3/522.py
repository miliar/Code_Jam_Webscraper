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


int rel[200];
bool in[200];

void testc(int tc)
{
  printf("Case #%i: ", tc+1);
  int p,q;

  scanf("%i %i ", &p, &q);
  
  FOR(i,0,q)
    scanf("%i ", rel+i);

  vector<int> reih;
  FOR(i,0,q)
    reih.push_back(rel[i]-1);

  memset(in, true, sizeof(in));

  long long bst=INF,cst;
  while(1)
    {
      IT(reih)
	in[*it]=true; 
      cst=0;
      
      IT(reih)
	{
	  in[*it]=false;
	  for( int i=*it-1;i>=0;i--)
	    if (!in[i]) break;
	    else cst++;

	  for( int i=*it+1;i<p;i++)
	    if (!in[i]) break;
	    else cst++;
	}

      if (bst>cst) {bst=cst;}//IT(reih)printf("%i ",*it);printf("\n");}

      if (!next_permutation(reih.begin(), reih.end()))
	  break;
    }
  printf("%lli\n", bst);
}


int main()
{
  int t=gi();
  FOR(i,0,t)
    testc(i);
  return 0;
}
