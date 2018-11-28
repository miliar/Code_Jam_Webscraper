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
#define lo(i, a, b) for(i = a; i <= b; i++)
#define lod(i, a, b) for(i = a; i >= b; i--)
#define pb push_back
#define sz(c) (c).size()

#define Max_S 150
#define Max_Q 1050
#define Len 150

typedef vector <int> vi;
typedef vector <vi > vvi;
typedef pair <int, int> ii;

FILE *inf = fopen("A.in", "r"), *outf = fopen("A.out", "w");

int S, Q;
vector<string> Comp;
vi V(Max_S);
int Data[ Max_Q];

void input()
{
	int i, st, en, mid;
	char temp[ Len];
	string cmp;

	fscanf(inf, "%d ", &S);
	Comp.clear();
	Comp.reserve(S);

	fr(i, S)
	{
		fgets( temp, Len, inf);
		Comp.pb(temp);
	}

	sort(Comp.begin(), Comp.end());

	fscanf(inf, "%d ", &Q);

	fr(i, Q)
	{
		fgets( temp, Len, inf);
		cmp = temp;

		st = 0, en = S-1;

		while( st <= en)
		{
			mid = (st + en) / 2;
			if( Comp[ mid] == cmp)
				break;
			if( Comp[ mid] < cmp)
				st = mid + 1;
			else
				en = mid - 1;
		}

		Data[i] = mid;
	}
}

int work()
{
	int i, j, res = 0, cnt = 0;

	V = vi(S, 0);

	fr(i, Q)
	{
		if( V[ Data[i]] == 0)
		{
			V[ Data[i]] = 1;
			cnt++;

			if(cnt == S)
			{
				res++;
				V = vi(S, 0);
				V[ Data[i]] = 1;
				cnt = 1;
			}
		}
	}

	return res;
}

int main()
{
	int T, i;
	fscanf(inf, "%d", &T);

	fr(i, T)
	{
		input();
		fprintf(outf, "Case #%d: %d\n", i+1, work());
	}

	return 0;
}