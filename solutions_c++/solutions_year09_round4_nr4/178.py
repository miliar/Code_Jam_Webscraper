#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;
int X[3],Y[3],R[3],N;
double RAR(int a,int b)
{
		return R[a]+R[b]+sqrt( (X[a]-X[b])*(X[a]-X[b]) + (Y[a]-Y[b])*(Y[a]-Y[b]) );
}
int main()
{
		int T;
		scanf("%d",&T);
		for (int kase=1;kase<=T;++kase)
		{
				scanf("%d",&N);
				for (int q=0;q<N;++q)
						scanf("%d %d %d",&X[q],&Y[q],&R[q]);
				printf("Case #%d: ",kase);
				if (N==1) printf("%.6lf\n",(double)R[0]);
				else if (N==2) printf("%.6lf\n",(double)max(R[0],R[1]));
				else
				{
						double ret=987654321;
						for (int q=0;q<3;++q)
						{
								int a=(q+1)%3,b=(q+2)%3;
								double my = max(RAR(a,b)/2,(double)R[q]);
								if (my<ret) ret=my;
						}
						printf("%.6lf\n",ret);
				}
		}
		return 0;
}
