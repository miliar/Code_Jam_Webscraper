#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <utility>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <iterator>

using namespace std;

typedef long long LL;
typedef pair< int, int > PRII;
typedef pair< double ,double > PRDD;
typedef vector< string > VS;
typedef vector< int > VI;

#define Size(a) ((int)a.size())
#define sqr(x) ((x)*(x))
#define lowbit(x) ((x)&(-(x)))

#define x first
#define y second
#define p_b push_back
#define m_p make_pair
#define oo 1000000000
#define eps 1e-12
const double pi = acos(-1.0);

#define maxn 10000 + 10

int n;
int d[maxn],l[maxn],f[maxn];

int main()
{
    int T,Test;
	int i,j;

	freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    
	scanf("%d",&Test);
	for( T = 1 ; T <= Test ; ++T )
		{
			scanf("%d",&n);
			for( i = 1 ; i <= n ; ++i )
				scanf("%d%d",&d[i],&l[i]);
			l[++n] = 0;
			scanf("%d",&d[n]);

			for( i = 1 ; i <= n ; ++i )
				f[i] = -oo;
			f[1] = d[1];
			for( i = 1 ; i <= n ; ++i )
				for( j = i+1 ; j <= n ; ++j )
					if( d[j]-d[i] <= f[i] )
						f[j] = max(f[j],min(d[j]-d[i],l[j]));

			if( f[n] == -oo )
				printf("Case #%d: NO\n",T);
			else printf("Case #%d: YES\n",T);
		}

    return 0;
}
