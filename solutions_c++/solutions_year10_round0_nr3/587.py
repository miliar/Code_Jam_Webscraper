#include<algorithm>
#include<cstdio>
#include<vector>
using namespace std;

#define fore(i,n) for(int i = 0; i < (n); i++)
#define fort(i,v) for(typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)

#define err(...) fprintf(stderr, __VA_ARGS__)

#define maxn 1010

int n,k,r;
int next[maxn], earn[maxn], gr[2*maxn];
int g[33][maxn];
long long c[33][maxn];

void test()
{
	scanf("%d%d%d", &r, &k, &n);
	fore(i,n) scanf("%d", &gr[i]);
	fore(i,n) gr[n+i] = gr[i];
	fore(i,n)
	{
		int sum = 0;
		next[i] = 0;
		fore(j,n)
		{
			if(sum + gr[i+j] > k)
			{
				next[i] = (i+j)%n;
				break;
			}
			sum += gr[i+j];
		}
		earn[i] = sum;
		//printf("%d %d\n", next[i], earn[i]);
	}
	fore(i,n)
	{
		c[0][i] = earn[i];
		g[0][i] = next[i];
	}
	for(int j = 1; j < 30; j++)
	{
		fore(i,n)
		{
			c[j][i] = c[j-1][i] + c[j-1][g[j-1][i]];
			g[j][i] = g[j-1][g[j-1][i]];
		}
		//fore(i,n) printf("%d ", g[j][i]); printf("\n");
		//fore(i,n) printf("%lld ", c[j][i]); printf("\n");
	}
	long long res = 0;
	int cur = 0;
	for(int j = 29; j >= 0; j--)
	{
		if(r >= (1<<j))
		{
			r -= 1<<j;
			res += c[j][cur];
			cur = g[j][cur];
		}
	}
	printf("%lld\n", res);
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int TT = 1; TT <= T; TT++)
	{
		printf("Case #%d: ", TT);
		test();
	}
}
