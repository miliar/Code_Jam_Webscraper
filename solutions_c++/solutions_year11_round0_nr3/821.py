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
		 printf("Case #%d: ",oo+1);
		 int n;
		 scanf("%d",&n);
		 fru(i,n) scanf("%d",&T[i]);
		 int x=0;
		 fru(i,n) x^=T[i];
		 sort(T,T+n);
		 int sum=0;
		 fru(i,n) sum+=T[i];
		 if(x) printf("NO\n");
		 else printf("%d\n",sum-T[0]);
	}
    return 0;
}
