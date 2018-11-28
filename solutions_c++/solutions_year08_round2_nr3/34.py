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

/////////////////////////

int tc, ntc;

int N;
int lab[1000001];
int bit[1000001];

int nq;
void add(int x, int v)
{
	x++;
	while (x <= N)
	{
		bit[x]+=v;
		x += x^(x&(x-1));
	}
}

int get(int x)
{
	x++;
	int res = 0;
	while (x)
	{
		res += bit[x];
		x -= x^(x&(x-1));
	}
	return res;
}

int getv(int x)
{
	// cari lowest index i, yang get(i) >= x
	
	int a = 0;
	int b = N-1;
	int mid;
	while (a < b)
	{
		mid = (a+b)/2;
		if (get(mid) >= x) b = mid;
		else a = mid+1;
	}
	return a;
}

int main()
{
	scanf("%d",&ntc);
	int cur;
	int i, a;
	int it;
	int n;
	
	for (tc=1; tc<=ntc; tc++)
	{
		scanf("%d",&N);
		
		cur = 0;
		n = N;
		memset(bit,0,sizeof(bit));
		for (i=0; i<N; i++) add( i, 1 );

		for (it = 1; it <= N; it++)
		{
			cur = (cur + it - 1)%n;
			a = getv( cur+1 );
			lab[ a ] = it;
			
			add( a, -1 );
			n--;
			
		}
		
		//printf("\n");
		//for (i=0; i<N; i++) printf("%d ",lab[i]); printf("\n");
		
		printf("Case #%d:",tc);
		scanf("%d",&nq);
		while (nq--)
		{
			scanf("%d",&a);
			printf(" %d",lab[a-1]);
		}
		printf("\n");
		
	}
}