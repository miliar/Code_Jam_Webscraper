#include <cstdio>
#include <algorithm>
#include <vector>

#define fru(j,n) for(int j=0;j<n;++j)
#define tr(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define x first
#define y second

using namespace std;

typedef pair<int,int> pii;
typedef long long LL;

const int MAXN = 1001;
int T[MAXN];
int main()
{
	int o;
	scanf("%d",&o);
	fru(oo,o)
	{
		 int n,ret=0;
		 scanf("%d",&n);
		 fru(i,n) scanf("%d",&T[i]);
		 fru(i,n) if(T[i]!=i+1) ++ret;

		 printf("Case #%d: %d.000000\n",oo+1,ret);

	}
    return 0;
}
