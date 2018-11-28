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

FILE *inf = fopen("D.in", "r"), *outf = fopen("D.out", "w");

int State[ 70000 * 17];
int R, C, W, S;
int Plus[ 5][5], Map[ 5][5], Ori[ 5][5];

void input()
{
	int i, j;
	char a;
	fscanf(inf, "%d%d", &R, &C);

	fr(i, R)
	{
		fr(j, C)
		{
			Ori[i][j] = 0;
			if(i == 0 && j == 0)
				Plus[i][j] = R*C;
			else
				Plus[i][j] = (j != 0 ? Plus[i][j-1] : Plus[i-1][C-1]) * 2; 
		}
	}

	W = S = 0;

	fr(i, R)
	{
		fr(j, C)
		{
			fscanf(inf, "%c", &a);
			if( a == '#' || a == '.' || a == 'K')
			{
				if( a == '#')
					W += Plus[i][j], S++, Ori[i][j] = 1;
				if( a == 'K')
					W += C * i + j;
			}

			else
				j--;
		}
	}
}

void make(int left, int x, int y, int Now)
{
	if(x == R)
	{
		if( left != 0)
			return;

		int i, j, k, sx, sy;
		int X[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
		int Y[8] = {-1, 0, 1, -1, 1, -1, 0, 1};

		fr(i, R)
		{
			fr(j, C)
			{
				if( Map[i][j] == 1)
					continue;

				State[ Now + C*i + j] = -1;

				fr(k, 8)
				{
					sx = i + X[k];
					sy = j + Y[k];

					if( 0 <= sx && sx < R && 0 <= sy && sy < C && Map[ sx][sy] == 0 && State[ Now + Plus[i][j] + C*sx + sy] == -1)
					{
						State[ Now + C*i + j] = 1;
						break;
					}
				}
			}
		}

		return;
	}

	if( left > 0)
	{
		Map[x][y] = 1;
		make(left-1, x + (y == C-1 ? 1 : 0), y == C-1 ? 0 : y+1, Now + Plus[x][y]);
		Map[x][y] = 0;
	}

	if( Ori[x][y] == 0)
		make(left, x + (y == C-1 ? 1 : 0), y == C-1 ? 0 : y+1, Now);
}

void work()
{
	int i, j, k;

	lod(i, R*C, (S-1))
	{
		fr(j, R)
		{
			fr(k, C)
				Map[j][k] = 0;
		}

		make(i, 0, 0, 0);
	}
}

void output(int x)
{
	fprintf(outf, "Case #%d:", x);

	if( State[ W] == 1)
		fprintf(outf, " A\n");
	else
		fprintf(outf, " B\n");
}

int main()
{
	int i, T;
	fscanf(inf, "%d", &T);

	fr(i, T)
	{
		input();
		work();
		output(i+1);
	}
	return 0;
}