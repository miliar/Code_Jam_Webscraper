#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;

typedef long long LL;
typedef pair <int,int> pii;
typedef vector <int> vi;
typedef vector <double> vd;
typedef vector <string> vs;
typedef vector <LL> vll;
typedef vector <char> vc;

/////////////////////////////////////////

int tc, ntc;

int parent[1001];
int nprim;
int prim[1000];
void genprim()
{
	nprim = 0;
	int i, j;
	for (i=2; i<=1000; i++)
	{
		for (j=2; j*j <= i; j++) if (i%j == 0) break;
		if (j*j > i) prim[nprim++] = i;
	}
}	

int A, B, P;

int gcd(int a, int b)
{
	if (b == 0) return a;
	return gcd(b, a%b);
}

bool valid(int a, int b)
{
	int g = gcd(a, b);
	if (g < P) return false;
	int i;
	for (i=0; i<nprim && prim[i] < P; i++)
		while (g % prim[i] == 0) g /= prim[i];
	if (g != 1) return true;
	return false;
}

int getparent(int x)
{
	if (parent[x] == x) return x;
	return parent[x] = getparent( parent[x] );
}

void join(int a, int b)
{
	int pa = getparent( a );
	int pb = getparent( b );
	if (pa == pb) return;
	parent[pa] = pb;
}

int main()
{
	genprim();
	//printf("%d\n",nprim);
	
	scanf("%d",&ntc);
	int i, j;
	int res;
	for (tc=1; tc<=ntc; tc++)
	{
		scanf("%d %d %d",&A,&B,&P);
		for (i=A; i<=B; i++) parent[i] = i;
		for (i=A; i<=B; i++) for (j=i+1; j<=B; j++)
			if (valid(i,j)) join(i, j);
		
		res = 0;
		for (i=A; i<=B; i++) if (parent[i] == i) res++;
		printf("Case #%d: %d\n",tc, res);		
	}
}

