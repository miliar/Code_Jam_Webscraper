#include <stdio.h>
#include <math.h>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <functional>

#define fi(t,a,b,c) for(t a = ( b ); a < ( c ); ++ a )
#define fd(t,a,b,c) for(t a = ( b ); a >= ( c ); -- a )
#define fii(a,b,c) fi( int, a, ( b ), ( c ) )
#define fdi(a,b,c) fd( int, a, ( b ), ( c ) )
#define fiii(a) fii( i, 0, ( a ) )
#define fiij(a) fii( j, 0, ( a ) )
#define fiik(a) fii( k, 0, ( a ) )
#define fdii(a) fdi( i, 0, ( a ) )
#define fdij(a) fdi( j, 0, ( a ) )
#define fdik(a) fdi( k, 0, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )

using namespace std;

int ni() { int a; scanf( "%d", &a ); return a; }
float nf() { float a; scanf( "%f", &a ); return a; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }

template <class T> void out( T a, T b ) { bool first = true; for( T i = a; i != b; ++ i ) { if( !first ) printf( " " ); first = false; cout << * i; } printf( "\n" ); }
template <class T> void outl( T a, T b ) { for( T i = a; i != b; ++ i ) { cout << * i << "\n"; } }

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;

struct RPI
{
	double wp;
	double owp;
	double oowp;
	int wins;
	int matches;
};

void solve()
{
	int n;
	char ch;
	scanf("%d", &n);
	vector<RPI> rpis(n);
	int** schedule = new int*[n];
	for(int i = 0; i < n; i++)
	{
		scanf("%c", &ch);
		schedule[i] = new int[n];
		rpis[i].matches = 0;
		rpis[i].wins = 0;
		for (int j = 0; j < n; j++)
		{
			char ch;
			scanf("%c", &ch);
			schedule[i][j] = -1;
			if(ch == '1')
			{
				schedule[i][j] = 1;
				rpis[i].wins++;
				rpis[i].matches++;
			}
			else if(ch == '0')
			{
				schedule[i][j] = 0;
				rpis[i].matches++;
			}
		}
		rpis[i].wp = 0;
		if(rpis[i].matches > 0)
		{
			rpis[i].wp = rpis[i].wins / (double)rpis[i].matches;
		}
	}

	for(int i = 0; i < n; i++)
	{
		float owp = 0;
		int count = 0;
		for(int j = 0; j < n; j++)
		{
			if(schedule[i][j] != -1)
			{
				count++;
				double tempOWP = (rpis[j].wins - schedule[j][i]) / (double)(rpis[j].matches - 1);
				if(tempOWP > 0)
				{
					owp += tempOWP;
				}
			}
		}
		owp /= (double)count;
		rpis[i].owp = owp;
	}

	for(int i = 0; i < n; i++)
	{
		float oowp = 0;
		int count = 0;
		for(int j = 0; j < n; j++)
		{
			if(schedule[i][j] != -1)
			{
				count++;
				oowp += rpis[j].owp;
			}
		}
		oowp /= (double)count;
		rpis[i].oowp = oowp;
	}

	for(int i = 0; i < n; i++)
	{
		float rpi = 0.25 * rpis[i].wp + 0.50 * rpis[i].owp + 0.25 * rpis[i].oowp;
		printf("%.7lf\n", rpi);
	}

	for(int i = 0; i < n; i++)
	{
		delete[] schedule[i];
	}
	delete[] schedule;
}

int main(int argc, char** argv)
{
   freopen( "input.txt", "r", stdin );
   freopen( "output.txt", "w", stdout );

   int tt = ni();
   fiii(tt)
   {
      printf("Case #%d:\n", i + 1);
	  solve();
	  printf("\n");
   }
   return 0;
}