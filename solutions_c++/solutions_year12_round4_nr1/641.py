#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

const int N = 10010;
typedef pair<int, int> pii;
#define X first
#define Y second
pii vine[N]; bool ok[N][N];

int main ()
{
	freopen("in.txt", "r", stdin);
	FILE *fp = fopen("out.txt", "w");
	int T; scanf("%d", &T);
	for (int TT = 1; TT <= T; ++TT)
	{
		int n; scanf("%d", &n);
		for (int i = 1; i <= n; i++) scanf("%d %d", &vine[i].X, &vine[i].Y);
		int des; scanf("%d", &des);
		vine[0].X = 0; bool res = false;
		memset(ok, false, sizeof ok);
		ok[0][1] = true;
		for (int i = 0; i < n && !res; i++)
		{
			for (int j = i + 1; j <= n && !res; j++) if (ok[i][j])
			{
				int f = min(vine[j].Y, vine[j].X - vine[i].X);
				int d = vine[j].X + f;
				if (d >= des) res = true;
				else
				{
					for (int k = j + 1; vine[k].X <= d && k <= n; k++)
						ok[j][k] = true; 
				}
			}
		}
		if (res) fprintf(fp, "Case #%d: YES\n", TT);
		else fprintf(fp, "Case #%d: NO\n", TT);
		printf("%d\n", TT);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
