#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <math.h>
#include <map>
#include <set>

using namespace std;

#define max(a, b) a > b ? a : b
#define min(a, b) a < b ? a : b
#define fr(i, n) for(i = 0; i < n; i++)
#define frd(i, n) for(i = n-1; i >= 0; i--)
#define lo(i, a, b) for(i = a; i < b; i++)
#define lod(i, a, b) for(i = a; i > b; i--)

#define pb push_back

#define Eps 1e-09
#define Inf 0x7fffffff

typedef vector <int> vi;
typedef vector <vi > vvi;
typedef pair <int, int> ii;

FILE *inf = fopen("B.in", "r"), *outf = fopen("B.out", "w");

int N, List[ 50], Sp[ 50];
__int64 res;

void input()
{
	int i;
	char str[ 50];
	fscanf(inf, " %s", str);

	N = strlen(str);

	fr(i, N)
		List[i] = str[i] - '0';
}

void work(int x)
{
	if(x == N)
	{
		__int64 su = List[0], C = 0;
		int mode = 0;	// 0 : plus, 1 : minus
		int i;

		lo(i, 1, N)
		{
			if( Sp[i] == 0 || Sp[i] == 1)
			{
				C += (mode == 0 ? su : -su);
				su = List[i];
				mode = Sp[i];
			}

			else
				su = su * 10 + List[i];
		}

		C += (mode == 0 ? su : -su);

		if(C < 0)
			C = -C;

		if( C % 2 == 0 || C % 3 == 0 || C % 5 == 0 || C % 7 == 0)
			res++;
		
		return;
	}

	Sp[x] = 0;
	work(x+1);
	Sp[x] = 1;
	work(x+1);
	Sp[x] = 2;
	work(x+1);
}

int main()
{
	int i, T;
	fscanf(inf, "%d", &T);

	fr(i, T)
	{
		input();
		res = 0;
		work(1);
		fprintf(outf, "Case #%d: %I64d\n", i+1, res);
	}
	return 0;
}