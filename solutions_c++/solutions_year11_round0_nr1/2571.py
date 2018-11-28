#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

typedef struct pereche
{
	int btn, idx;
};
int T, N;
vector <pereche> A, B;

int ab(int x) { return x >= 0 ? x : -x; }

void solve(int Na, int Nb, int caseNr)
{
	//printf("%d %d\n", Na, Nb);
	int i, crt, ia, ib, pa, pb, ta, tb;
	i = pa = pb = 1;
	crt = ia = ib = ta = tb = 0;
	while (i <= N)
	{
		if (i == A[ia].idx && ia < Na)
		{
			ta += ab(A[ia].btn - pa);
			if (ta < crt) ta = crt;
			ta++; 
			pa = A[ia].btn;
			crt = ta;
			ia++;
		}
		else if (i == B[ib].idx && ib < Nb)
		{
			tb += ab(B[ib].btn - pb);
			if (tb < crt) tb = crt;
			tb++;
			pb = B[ib].btn;
			crt = tb;
			ib++;
		}
		i++;
	}
	printf("Case #%d: %d\n", caseNr, crt);
}

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int i, j, k;
	scanf("%d\n", &T);
	
	for (k = 1; k <= T; k++)
	{
		char c;
		int b;
		pereche x;
		while (A.size()) A.pop_back();
		while (B.size()) B.pop_back();
		
		scanf("%d ", &N);
		for (i = 1; i <= N; i++)
		{
			scanf("%c %d ", &c, &b);
			x.idx = i;
			x.btn = b;
			if (c == 'B') B.push_back(x);
			else A.push_back(x);
		}
		int na = A.size(), nb = B.size();
		solve(na, nb, k);
	}
	return 0;
}
