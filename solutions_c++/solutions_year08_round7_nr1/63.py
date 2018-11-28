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

#define Eps 1e-11

#define PI 3.141592653589

template<class T> void replaceMin(T &a, T b){if(b<a) a=b;}
template<class T> void replaceMax(T &a, T b){if(b>a) a=b;}

bool isUpperCase(char c){return c>='A' && c<='Z';}
bool isLowerCase(char c){return c>='a' && c<='z';}
bool isLetter(char c){return c>='A' && c<='Z' || c>='a' && c<='z';}
bool isDigit(char c){return c>='0' && c<='9';}
char toLowerCase(char c){return (isUpperCase(c))?(c+32):c;}
char toUpperCase(char c){return (isLowerCase(c))?(c-32):c;}

int gcd(int a, int b){if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}

int ccw(double a,double b,double c,double d,double e,double f)
  {double t=(c-a)*(f-b)-(e-a)*(d-b);if (-Eps <= t && t <=Eps) return 0;return (t<0)?-1:1;}

typedef vector <int> vi;

FILE *inf = fopen("A.in", "r"), *outf = fopen("A.out", "w");

int N, M, Res;
char Name[ 1200][ 40];
int Sons[ 1200][ 1200], List[ 1200][ 1200];

char get( char* str)
{
	int i;

	fr(i, M)
	{
		if( strcmp( str, Name[i]) == 0)
			break;
	}

	if(i == M)
	{
		strcpy( Name[i], str);
		M++;
	}

	return i;
}

void input()
{
	int i, j, x, y, su;
	char str[ 40];

	fscanf(inf, "%d ", &N);
	M = 0, Res = 1;

	fr(i, N)
	{
		fscanf(inf, "%s", str);

		x = get( str);
		Sons[x][0] = 0;

		fscanf(inf, "%d", &su);

		fr(j, su)
		{
			fscanf(inf, "%s", str);
			if( isLowerCase(str[0]))
				continue;

			y = get(str);
			Sons[x][0]++;
			Sons[x][ Sons[x][0]] = y;
		}
	}
}

int work(int x)
{
	int i, res = 1;

	if( Sons[x][0] == 0)
		return res;

	else
	{
		lo(i, 1, (Sons[x][0]+1))
		{
			List[x][i] = work( Sons[x][i]);
		}

		List[ x][0] = List[x][ Sons[x][0]];
		sort( List[x], List[x] + Sons[x][0]);

		lod(i, Sons[x][0]-1, -1)
		{
			replaceMax(res, (List[x][ i] + (Sons[x][0] - i - 1)));
		}

		replaceMax( res, (Sons[x][0] + 1));
		replaceMax( Res, res);
		
		return res;
	}
}

void output(int x)
{
	fprintf(outf, "Case #%d: %d\n", x, Res);
}

int main()
{
	int i, T = 0;
	fscanf(inf, "%d", &T);

	fr(i, T)
	{
		input();
		work(0);
		output(i+1);
	}

	return 0;
}