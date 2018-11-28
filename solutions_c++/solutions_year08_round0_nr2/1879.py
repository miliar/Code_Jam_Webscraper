#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

const int MAX_N = 128;

struct el { int a, b, type; };

bool operator<(el &a, el &b) { return a.b<b.b; }

int dt, n, m;
vector<el> A;

int V[2*MAX_N];
int ans[2];

void input ()
{
	int i, a, b;
	el p;

	scanf ("%d", &dt);
	scanf ("%d%d", &n, &m);
	A.clear();

	for (i=0; i<n; i++) {
		scanf ("%d:%d", &a, &b);
		p.a = a*100 + b;
		scanf ("%d:%d", &a, &b);
		p.b = a*100 + b;
		p.type = 0;
		A.push_back (p);
	}

	for (i=0; i<m; i++) {
		scanf ("%d:%d", &a, &b);
		p.a = a*100 + b;
		scanf ("%d:%d", &a, &b);
		p.b = a*100 + b;
		p.type = 1;
		A.push_back (p);
	}
}

void dfs (int endtime, int type)
{
	int i;

	for (i=A.size()-1; i>=0; i--)
		if (!V[i] && A[i].b<=endtime-dt && A[i].type==type) {
			V[i] = 1;
			dfs (A[i].a, !type);
			return;
		}

	ans[!type]++;
}

void solve ()
{
	int i;
	
	ans[0]=0, ans[1]=0;
	memset (V,0,sizeof(V));

 	sort (A.begin(), A.end());

	for (i=A.size()-1; i>=0; i--) {
		if (!V[i]) {
			V[i]=1;
			dfs (A[i].a, !A[i].type);
		}
	}

	printf ("%d %d\n", ans[0], ans[1]);
}

int main ()
{
	freopen ("a.in", "r", stdin);
	freopen ("a.out", "w", stdout);

	int i, t;

	scanf ("%d", &t);

	for (i=1; i<=t; i++) {
		input ();
		printf ("Case #%d: ", i);
		solve ();
	}

	return 0;
}