#include<stdio.h>
#include<algorithm>
#include<math.h>
using namespace std;
const int maxn = 100;

int N,X[maxn],Y[maxn],R[maxn];

double dist(int i,int j)
{
	return sqrt((X[i] - X[j]) * (X[i] - X[j]) + (Y[i] - Y[j]) * (Y[i] - Y[j]));
}

double min(double a,double b){return a < b ? a : b;}

int main()
{
	freopen("watering.in","r",stdin);
	freopen("watering.out","w",stdout);
	int nrt = 0;
	scanf("%d\n",&nrt);
	for(int nr = 0;nrt;++nr,--nrt)
	{

		scanf("%d\n",&N);
		for(int i = 1;i <= N; ++i)
		{
			scanf("%d %d %d\n",&X[i],&Y[i],&R[i]);
		}

		double ans = 1000000000;
		ans = min(ans,max(0.5 * (dist(1,2) + R[1] + R[2]),(double)R[3]));
		ans = min(ans,max(0.5 * (dist(1,3) + R[1] + R[3]),(double)R[2]));
		ans = min(ans,max(0.5 * (dist(2,3) + R[2] + R[3]),(double)R[1]));
		if (N == 2) ans = max(R[1],R[2]);
		if (N == 1) ans = R[1];
		printf("Case #%d: %lf\n",nr + 1,ans);
	}


	return 0;
}



