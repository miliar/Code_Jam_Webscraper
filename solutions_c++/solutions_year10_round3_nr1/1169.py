#include <cstdio>
#include <cstring>
#include <utility>
#define a first
#define b second
#define N 1005

using namespace std;

pair<int, int> A[N];

int main()
{
    int t;
	freopen("large.in","r",stdin);
	freopen("large.out","w",stdout);
	scanf("%d",&t);
	for (int k=1; k<=t; k++)
	{
	    int n,kont=0;
	    scanf("%d",&n);
	    int x,y;
	    for (int i=1; i<=n; i++)
	    {
	        scanf("%d%d",&x,&y);
	        A[i]=make_pair(x,y);
	    }

	    for (int i=1; i<n; i++)
            for (int j=i+1; j<=n; j++)
                if (A[i].a>A[j].a && A[i].b<A[j].b || A[i].a<A[j].a && A[i].b>A[j].b)
                    kont++;

        printf("Case #%d: %d\n",k,kont);

        memset(A,0,sizeof(A));
	}

	return 0;
}
