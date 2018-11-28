#include <algorithm> 
#include <bitset> 
#include <cassert>
#include <cmath> 
#include <complex>
#include <cstdio> 
#include <cstdlib> 
#include <cstring>
#include <ctime> 
#include <deque> 
#include <functional> 
#include <iomanip> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <utility> 
#include <valarray>
#include <vector> 
using namespace std; 

#define ALL(x) (x).begin(), (x).end()
#define MP make_pair
#define SZ(x) ((int) (x).size())
#define max2(x,y) ((x) = max((x),(y)))
#define min2(x,y) ((x) = min((x),(y)))
typedef long long LL;

int N;
char nums[1010][200];
char sol[200];

void gen_gp_input()
{
	FILE *f = fopen("a", "w");
	assert(f != NULL);

	for (int i = 0; i < 4; ++i)
		fprintf(f, "allocatemem();\n");
	fprintf(f, "a = [");
	for (int i = 0; i < N; ++i) {
		if (i != 0)
			fprintf(f, ", ");
		fprintf(f, "%s", nums[i]);
	}
	fprintf(f, "];\n");

	fprintf(f, "diffs = [");
	for (int i = 0; i < N; ++i) {
		for (int j = i+1; j < N; ++j) {
			if (j != 1)
				fprintf(f, ", ");
			fprintf(f, "abs(a[%d] - a[%d])", i+1, j+1);
		}
	}
	fprintf(f, "];\n");

	fprintf(f, "g = gcd(diffs);\n");
	fprintf(f, "nextEvent = ((a[1] - 1) \\ g) * g + g;\n");
	fprintf(f, "sol = nextEvent - a[1]\n");

	fclose(f);
}

void solve()
{
	gen_gp_input();
	system("gp -q < a > b");

	FILE *f = fopen("b", "r");
	assert(f != NULL);
	fscanf(f, "%s", sol);
	fclose(f);
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int TC = 1; TC <= T; ++TC) {
		fprintf(stderr, "solving case %d\n", TC);
		scanf("%d", &N);
		for (int i = 0; i < N; ++i)
			scanf("%s", nums[i]);
		solve();
		printf("Case #%d: %s\n", TC, sol);
	}
	return 0;
}
