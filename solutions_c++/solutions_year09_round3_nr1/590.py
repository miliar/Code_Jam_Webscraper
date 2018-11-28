
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


char buf[100];
int map[255];
unsigned long long numb[100];

void testc(int tc)
{
	printf("Case #%i: ", tc+1);
	
	gets(buf);
	int  l=strlen(buf);

	memset(map, 0xff, sizeof(map));
	map[buf[0]]=1;

	unsigned long long nx=0;
	FOR(i,0,l)
	{
		if (map[buf[i]]==-1)
		{
			map[buf[i]]=nx;
			nx++;
			if (nx==1) nx++;
		}

		numb[i]=(unsigned long long)map[buf[i]];
		//printf("%i,", numb[i]);
	}	
	//printf("\n");

	if (nx<2) nx=2;
	
	unsigned long long sum = 0;
	unsigned long long pot=1;
	for(int i=l-1;i>=0;i--)
	{
		sum+=pot*numb[i];
		pot*=nx;
	}
	printf("%llu\n", sum);
}


int main()
{
  int t=gi();
  FOR(i,0,t)
    testc(i);
  return 0;
}
