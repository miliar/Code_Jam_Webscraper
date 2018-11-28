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

int main()
{
	int t;
	scanf("%d",&t);
	fru(r,t)
	{
		int P[2],W[2];
		fru(i,2) P[i]=1;
		fru(i,2) W[i]=0;
		int q,ret=0;
		scanf("%d",&q);
		fru(i,q)
		{
			char c; int p;
			scanf(" %c %d",&c,&p);
			c=c=='O';
			int m=abs(P[c]-p);
			m=max(m-W[c],0)+1;
			W[c]=0;
			W[1-c]+=m;
			P[c]=p;
			ret+=m;
		}
		printf("Case #%d: %d\n",r+1,ret);
	}  
  return 0;
}
