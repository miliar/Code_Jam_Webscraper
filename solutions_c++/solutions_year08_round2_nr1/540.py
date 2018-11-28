#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <cmath>
using namespace std;
#define PI 3.14159265358979323846264338327950288
int T, N,a,b,c,d,xx,yy,m;
__int64 x[100001],y[100001];

int main() 
{
	
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);

	int i,j,k, Case = 1;
	scanf("%d", &T);
	while (T --) {
		scanf("%d", &N);
		scanf("%d%d%d%d%d%d%d",&a,&b,&c,&d,&xx,&yy,&m);
		x[0]=xx,y[0]=yy;
		for (i = 1; i < N; i ++)
		{
			x[i]=(a*x[i-1]+b)%m;
			y[i]=(c*y[i-1]+d)%m;
		}
		//sort(all[0], all[0] + N);
		//sort(all[1], all[1] + N);
		int ans=0;
		for (i = 0; i < N; i ++)
		{
			for(j=i+1;j<N;j++)
			{
				for(k=j+1;k<N;k++)
				{
					if( (x[i]+x[j]+x[k])%3==0&&(y[i]+y[j]+y[k])%3==0)
						ans++;
				}
			}
		}
		printf("Case #%d: %d\n", Case ++, ans);
	}
	return 0;
}

