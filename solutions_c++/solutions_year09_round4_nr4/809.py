#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;
#define rep(i,n) for (int i=0;i<n;i++)

typedef vector<int> vi;

int main()
{
	freopen("smd.in", "r", stdin);
	freopen("outd.txt", "w", stdout);

	int tno; scanf("%d",&tno);
	for (int tc=1;tc<=tno;tc++)
	{
		int n;
		int x[100],y[100],r[100];
		scanf("%d", &n);
		rep(i,n) scanf("%d%d%d", &x[i], &y[i], &r[i]);

		double r1 = 1000000000.0;

		if (n==1) r1=r[0];
		else if (n==2) r1=max(r[0],r[1]);
		else {
			for (int i=0;i<n;i++)
				for (int j=0;j<n; j++) {
					if (i==j) continue;
					for (int k=0;k<n;k++) {
						if (j==k || k==i) continue;

#define SQ(x) ((x)*(x))
						double rr1;
						double d1 = sqrt( (double)SQ(x[i]-x[j])+SQ(y[i]-y[j]) );
						rr1 = (d1 + r[i]+r[j])/2.0;

						double rr2 = r[k];

						double rr3 = max(rr1, rr2);
						if ( rr3<r1 )
							r1=rr3;


					}
					
				}
		}
		printf("Case #%d: %.7f\n", tc, r1);
		fflush(stdout);
	}
	return 0;
}