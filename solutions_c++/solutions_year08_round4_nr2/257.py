#include <cstdio>
#include <vector>
#define pb push_back
#define fi first
#define se second
#define INF 1000000000
using namespace std;
typedef long long ll;
typedef pair<int,int> pi;
		
int main()
{
	int tests;
	scanf("%d",&tests);
	for (int u=1; u<=tests; u++)
	{
		int x,y,c;
		bool czy=1;
		scanf("%d %d %d",&x,&y,&c);
		for (int i=0; i<=x&&czy; i++)
			for (int j=0; j<=y&&czy; j++)
				for (int k=0; k<=x&&czy; k++)
					for (int l=0; l<=y&&czy; l++)
						if (abs(i*l-j*k)==c)
		{
			czy=0;
			printf("Case #%d: 0 0 %d %d %d %d\n",u,i,j,k,l);
		}
		if (czy) printf("Case #%d: IMPOSSIBLE\n",u);
	}
}
