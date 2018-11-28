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
#define Max_T 300

typedef vector <int> vi;
typedef vector <vi > vvi;
typedef pair <int, int> ii;

FILE *inf = fopen("B.in", "r"), *outf = fopen("B.out", "w");

int an[2], ex[2];		// 0 : A, 1 : B
int NA, NB, P;
vi V(Max_T);

struct Time{
	int h, m;

	bool operator < (const Time &t) const{
		if( h < t.h || (h == t.h && m < t.m)) return true;
		return false;
	};
};

struct Train{
	Time s, t;
	int p;

	bool operator < (const Train &x) const{
		if( s < x.s) return true;
		return false;
	};
} train[ Max_T];

void input()
{
	int i;
	char str[ 100];
	fscanf(inf, "%d%d%d ", &P, &NA, &NB);

	fr(i, (NA + NB))
	{
		fgets(str, 100, inf);
		sscanf(str, "%d:%d %d:%d", &train[i].s.h, &train[i].s.m, &train[i].t.h, &train[i].t.m);
		train[i].p = i < NA ? 0 : 1;
	}

	sort(train, train + (NA+NB));
}

void work()
{
	int i, j;

	V = vi(NA + NB, 0);

	fr(i, (NA + NB))
	{
		fr(j, i)
		{
			if(V[j] == 1)
				continue;

			Time temp = train[j].t;
			temp.m += P-1;
			temp.h += temp.m / 60;
			temp.m %= 60;

			if( temp < train[i].s)
			{
				V[j] = 1;
				ex[ !train[j].p]++;
			}
		}

		if( ex[ train[i].p] != 0)
			ex[ train[i].p]--;
		else
			an[ train[i].p]++;
	}
}

int main()
{
	int i, T;
	fscanf(inf, "%d", &T);
	fr(i, T)
	{
		input();
		an[0] = an[1] = 0;
		ex[0] = ex[1] = 0;
		work();
		fprintf(outf, "Case #%d: %d %d\n", i+1, an[0], an[1]);
	}
	return 0;
}