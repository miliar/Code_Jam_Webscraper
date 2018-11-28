#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cmath>
#include <cctype>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <iostream>
#include <ctime>

using namespace std;

const int inf = 1 << 30;

typedef long double LD;
typedef vector < int > VI;
typedef vector < string > VS;
typedef pair < int, int > PII;
typedef map < string, int > MSI;

#define MP make_pair
#define PB push_back
#define X first
#define Y second

#define ALL(a) (a).begin(), (a).end()
#define ABS(a) ( (a) < 0 ? -(a) : (a) )
#define SQR(a) ( (a) * (a) )
#define SIZE(a) ( (int) (a).size() )
#define LENGTH(a) ( (int) (a).length() )

#ifdef WIN32
typedef __int64 i64;
#define Ld "%I64d"
#else
typedef long long i64;
#define Ld "%lld"
#endif

const char *const in = "1.in";
const char *const out = "1.out";

VS getS(int n)
{
	VS res;
  	for (int i = 0; i < n; ++i)
   	{
   		char name[512];
   		gets( name );
   		res.PB( name );
   	}
	return res;
}

int main()
{
	int t;

    freopen(in, "rt", stdin);
    freopen(out, "wt", stdout);

    scanf("%d\n", &t);

    for (int T = 0; T < t; ++T)
    {
    	int Q, E, ans = 0;

	   	scanf("%d\n", &E);
	  	getS( E );
    	scanf("%d\n", &Q);
    	VS quer( getS( Q ) );

    	set < string > s;
    	for (int i = 0; i < Q; ++i)
    	{
    		s.insert( quer[i] );
    		if (SIZE( s ) == E)
    		{
    			++ans; --i;
    			s.clear();
    		}
    	}

    	printf("Case #%d: %d\n", T + 1, ans);
    }

    fclose(stdin);
    fclose(stdout);
 
    return 0;
}
