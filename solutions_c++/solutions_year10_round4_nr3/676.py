#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <assert.h>
using namespace std;

typedef long long LL;
typedef vector <string> vs;
typedef vector <int> vi;
typedef vector <LL> vll;
typedef vector <double> vd;
typedef pair <int,int> pii;

int tc, ntc;
int n;

int ar[105][105];
int xar[105][105];

bool finish()
{
	int i, j;
	for (i=1; i<n; i++) for (j=1; j<n; j++)
		if (ar[i][j]) return false;
	return true;
}

void proc()
{
	memset(xar, 0, sizeof(xar));
	int i, j;
	for (i=1; i<n; i++) for (j=1; j<n; j++)
	{
		if (ar[i][j])
		{
			if (ar[i-1][j] == 0 && ar[i][j-1] == 0)
				xar[i][j] = 0;
			else
				xar[i][j] = 1;
		}
		else
		{
			if (ar[i-1][j] == 1 && ar[i][j-1] == 1)
				xar[i][j] = 1;
			else
				xar[i][j] = 0;
		}
	}

	memcpy(ar, xar, sizeof(ar));
}

int main()
{
	FILE* fi = fopen("C-small0.in", "r");
	FILE* fo = fopen("C-small0.out", "w");

	fscanf(fi, "%d", &ntc);
	for (tc = 1; tc <= ntc; tc++)
	{
		n = 101;
		memset(ar, 0, sizeof(ar));

		int r;
		fscanf(fi, "%d", &r);
		int i, j;
		while (r--)
		{
			int y1, x1, y2, x2;
			fscanf(fi, "%d %d %d %d", &y1, &x1, &y2, &x2);

			for (i=y1; i<=y2; i++) for (j=x1; j<=x2; j++)
				ar[i][j] = 1;
		}

		for (i=0;;i++)
		{
			if (finish()) break;
			proc();
		}

		printf("Case #%d: %d\n", tc, i);
		fprintf(fo, "Case #%d: %d\n", tc, i);
	}
	return 0;
}