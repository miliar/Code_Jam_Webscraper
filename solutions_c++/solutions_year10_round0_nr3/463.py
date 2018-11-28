#if defined(_MSC_VER) && _MSC_VER >= 1400
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long int64;
typedef vector<int> vi;
#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()

static const char * readLine()
{
	static char buffer[2048];
	if (NULL == fgets(buffer, 2048, stdin))
		return NULL;
	int len = (int)strlen(buffer);
	if ('\n' == buffer[len - 1])
		buffer[--len] = '\0';
	return buffer;
}

int g[2000];
int a[2000];
int b[2000];
int64 money[2000];
int R, k, N;


void solve()
{
	scanf("%d %d %d", &R, &k, &N);
	//printf("%d %d %d\n", R, k, N);
	
	for (int i=0; i<N; i++) 
	{
		int tmp;
		scanf("%d", &tmp);
		g[i] = tmp;
	}

	for (int i=0; i<N; i++) 
	{
		b[i] = -1;
	}

	int ind = 0;
	int pos = 0;

	money[ind] = 0;
	a[ind] = pos;

	do 
	{
		b[pos] = ind;

		int count = 0;
		int i;
		for (i=0; i<N; i++) 
		{
			if (count + g[(i+pos) % N] <= k)
				count += g[(i+pos) % N];
			else
				break;
		}

		pos = (pos + i) % N;
		ind++;
		money[ind] = money[ind - 1] + count;
		a[ind] = pos;
		
	} while (-1 == b[pos]);


#if 0
	printf("\n");
	printf("ind = %d\n", ind);
	for (int i=0; i<=ind; i++)
	{
		printf("%d %d\n", a[i], money[i]);
	}
#endif

	int period = ind - b[pos]; 
	//printf("period %d\n", period);

	if (R <= ind)
	{
		printf("%lld", money[R]);
		return;
	}

	int t1 = b[pos];
	int t2 = ind;

	int64 total = money[t1];
	R -= t1;
	total += (money[t2] - money[t1]) * (R / period);

	int tmp = R % period;
	if (0 != tmp)
		total += money[t1 + tmp] - money[t1];

	printf("%lld", total);
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int no=1; no<=T; no++)
	//for (int no=1; no<=1; no++)
	{
		printf("Case #%d: ", no);
		solve();
		printf("\n");
	}
}

const char * const * getConfig()
{
	//static const char * const config[] = {"C-sample.txt", NULL};
	//static const char * const config[] = {"C-small-attempt0.in", "C_out_small.txt"};
	static const char * const config[] = {"C-large.in", "C_out_large.txt"};
	return config;
}
