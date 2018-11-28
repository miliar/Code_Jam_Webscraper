#include <stdio.h>
#include <string.h>
#include <cmath>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;

int tc, ntc;

int D, I, M;
int n;
int ar[200];
int val[200][260];
bool used[200][260];

#define INF 100000000

struct tt
{
	int pos, val;
	tt() {}
	tt (int a, int b) {pos = a; val = b;}
};
bool operator<(const tt& a, const tt& b) { return false; }

priority_queue < pair<int, tt> > pq;
void add(int a, int b, int v)
{
	if (val[a][b] > v)
	{
		val[a][b] = v;
		pq.push( make_pair( -v, tt(a,b) ) );
	}
}

int doit()
{
	while (!pq.empty()) pq.pop();
	
	int i, j;
	for (i=0; i<=n; i++) for (j=0; j<=256; j++)
	{
		val[i][j] = INF;
		used[i][j] = 0;
	}
		
	add(0, 256, 0);
	
	//printf("D = %d\n", D);
	while (!pq.empty())
	{
		pair <int, tt> xx = pq.top(); pq.pop();
		
		int cval = -xx.first;
		tt cur = xx.second;
		if (used[cur.pos][cur.val]) continue;
				
		if (cur.pos == n) continue;
		
		// remove pos
		add(cur.pos+1, cur.val, cval + D);		
		int i;
		for (i=0; i<=255; i++) if (cur.val == 256 || abs(cur.val-i) <= M)
		{
			// change the value
			add(cur.pos+1, i, cval + abs(ar[cur.pos]-i));			
			
			// add one point
			add(cur.pos, i, cval + I);
		}
	}
	
	int res = INF;
	for (i=0; i<=256; i++) res <?= val[n][i];
	return res;
}

int main()
{
	scanf("%d", &ntc);
	int i;
	for (tc = 1; tc <= ntc; tc++)
	{
		scanf("%d %d %d %d", &D, &I, &M, &n);
		for (i=0; i<n; i++) scanf("%d", &ar[i]);
		
		int res = doit();
		printf("Case #%d: %d\n", tc, res);
	}
}