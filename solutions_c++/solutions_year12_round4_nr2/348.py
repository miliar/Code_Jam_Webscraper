#include<cstdio>
#include<algorithm>
#include<functional>
using namespace std;
#define MAXN 1112

double eps = 1e-12;

int T,N;
double W,L;
struct circle
{
	double r,x,y;
	int n;
	bool operator < (const circle &a) const
	{
		return r > a.r;
	}
}C[MAXN];

double Ans[MAXN][2];


int main()
{
	//freopen("B.in","r",stdin);
	//freopen("B.out","w",stdout);
	int i;
	scanf("%d",&T);
	for (int t=1;t<=T;t++)
	{
		scanf("%d%lf%lf",&N,&W,&L);
		for (i=0;i<N;i++)
		{
			scanf("%lf",&C[i].r);
			C[i].n = i;
		}
		sort(C,C+N);
		bool sw = 0;
		if (W > L)
		{
			swap(W,L);
			sw = 1;
		}
		double y = 0.0,next_y = 0.0;
		double x = W;
		int first = -1;
		bool suc = 1;
		for (i=0;i<N;i++)
		{
			if (x + C[i].r <= W + eps)
			{
				if (first == 0)
					C[i].y = 0.0;
				else
					C[i].y = y + C[i].r;	
				C[i].x = x + C[i].r;
				x += 2*C[i].r;
			}
			else
			{
				++first;
				if (first == 0)
				{
					next_y = C[i].r;
					C[i].y = 0.0;
				}
				else
				{
					y = next_y;
					if (next_y > L + eps)
					{
						suc = 0;
						printf("WWWWW\n");
						break;
					}
					next_y = y + C[i].r * 2;
					C[i].y = y + C[i].r;
				}
				C[i].x = 0.0;
				x = C[i].r;
			}
		}
		if (!suc)
			continue;
		for (i=0;i<N;i++)
		{
			Ans[C[i].n][0] = C[i].x;
			Ans[C[i].n][1] = C[i].y;
		}
		if (sw)
			for (i=0;i<N;i++)
				swap(Ans[i][0],Ans[i][1]);
		printf("Case #%d:",t);
		for (i=0;i<N;i++)
			printf(" %.1f %.1f",Ans[i][0],Ans[i][1]);
		printf("\n");
	}
}
