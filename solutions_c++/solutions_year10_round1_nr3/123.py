#include <iostream>
#include <cmath>
using namespace std;
int i,j,n,m,testcase,curcase = 1,A1,A2,B1,B2;
long long ans;
double golden = (sqrt(5)-1)/2;
int rate;
int main()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	for ( scanf("%d\n",&testcase) ; curcase<=testcase ; curcase++ )
	{
		printf("Case #%d: ",curcase);
		scanf("%d %d %d %d\n",&A1,&A2,&B1,&B2);
		ans = 0;
		for ( i = A1 ; i <= A2 ; i++ )
		{
			rate = (int)ceil((double)i*golden);
			if (rate<=B1) continue;
			if ((rate>B1)&&(rate<=B2)) ans += (long long)(rate-B1);
			if (rate>B2) ans += (long long)(B2-B1+1);
		}
		for ( i = B1 ; i <= B2 ; i++ )
		{
			rate = (int)ceil((double)i*golden);
			if (rate<=A1) continue;
			if ((rate>A1)&&(rate<=A2)) ans += (long long)(rate-A1);
			if (rate>A2) ans += (long long)(A2-A1+1);
		}
		cout << ans << endl;
	}
}
