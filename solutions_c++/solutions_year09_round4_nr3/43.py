#include <iostream>

using namespace std;

const int nn = 128;

int test;

int p[nn][nn];
int b[nn][nn];
int N;

int rm[nn];
int w[nn];

bool dfs(int x)
{
	if (w[x] == 1) return false;
	w[x] = 1;
	
	for (int i = 0; i < N; i++) if (b[x][i])
		if (rm[i] == -1 || dfs(rm[i]))
		{
			rm[i] = x;
			return true;
		}

	return false;
}

int match()
{
	memset(rm, -1, sizeof rm);
	int res = 0;
	for (int i = 0; i < N; i++)
	{
		memset(w, 0, sizeof w);
		if (dfs(i)) res++;
	}
	return res;
}

void solve()
{
	int ans = 0;
	int n, k;
	cin >> n >> k;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < k; j++) cin >> p[i][j];
	}

	memset(b, 0, sizeof b);

	for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) if (i != j)
	{
		bool ok = true;
		for (int l = 0; l < k; l++) if (p[i][l] >= p[j][l]) ok = false;
		if (ok) b[j][i] = 1;
	}
	
	//for (int i = 0; i < n; i++)
	//{
	//	for (int j = 0; j < n; j++) cerr << b[i][j] << ' ';
	//	cerr << endl;
	//}
	//cerr << endl;

	N = n;
	ans = n - match();

	cout << "Case #" << ++test << ": " << ans << endl;
	cerr << "Case #" << test << ": " << ans << endl;
}

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int t;
	cin >> t;
	while (t--)
	solve();
	fclose(stdout);
	return 0;
}