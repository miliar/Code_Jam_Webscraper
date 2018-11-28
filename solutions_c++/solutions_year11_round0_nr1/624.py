#include <cstdio>
#include <algorithm>
using namespace std;

#define maxn 111

int n;
char c;
int t[2][maxn];
int prev[2][maxn], w[2][maxn];
int T[maxn];

void test()
{
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
	{
		scanf(" %c", &c);
		t[0][i] = t[1][i] = 0;
		scanf("%d", &t[c=='O'][i]);
		//printf("%d %d\n", t[0][i], t[1][i]);
	}
	prev[0][0] = prev[1][0] = 1;
	w[0][0] = w[1][0] = -1;
	for(int i=0;i<2;i++) for(int j=1;j<n;j++)
	{
		if(t[i][j-1] == 0)
		{
			prev[i][j] = prev[i][j-1];
			w[i][j] = w[i][j-1];
		}
		else
		{
			prev[i][j] = t[i][j-1];
			w[i][j] = j-1;
		}
		//printf("i=%d, j=%d, prev=%d, w=%d\n", i,j,prev[i][j],w[i][j]);
	}
	T[0] = 0;
	for(int i = 1; i <= n; i++)
	{
		int q;
		if(t[0][i-1] == 0) q = 1;
		else q = 0;
		//printf("q=%d, prev=%d, w=%d, t=%d\n", q, prev[q][i-1], w[q][i-1], t[q][i-1]);
		T[i] = max(T[i-1] + 1, T[w[q][i-1]+1] + abs(t[q][i-1] - prev[q][i-1]) + 1);
		//printf("T[%d] = %d\n", i, T[i]);
	}
	printf("%d\n", T[n]);
}

int main()
{
	int tt;
	scanf("%d", &tt);
	for(int i = 1; i <= tt; i++)
	{
		printf("Case #%d: ", i);
		test();
	}
}
