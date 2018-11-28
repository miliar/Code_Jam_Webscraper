#include <stdio.h>
#include <map>
#include <algorithm>
using namespace std;
int Len[205];
int main()
{
	int T;
	scanf("%d",&T);
	for (int kase=1;kase<=T;++kase)
	{
		for (int i=0;i<=200;++i) Len[i] = 0;
		int X,S,R,t,N;
		scanf("%d %d %d %d %d",&X,&S,&R,&t,&N);
		for (int q=0;q<N;++q)
		{
			int s,e,w;
			scanf("%d %d %d",&s,&e,&w);
			Len[ S+w ] += e-s;
			X -= e-s;
		}
		Len[S] = X;
		double timeRemain = t;
		int boost = R - S;
		double ret = 0;
		for (int q=1;q<=200;++q) if (Len[q]>0)
		{
			double fullRun = double(Len[q])/(q+boost);
			if (fullRun <= timeRemain) 
			{
				timeRemain -= fullRun;
				ret += fullRun;
			}
			else
			{
				double remainLength = Len[q] - (q+boost) * timeRemain;
				ret += timeRemain;
				ret += remainLength / q;
				timeRemain = 0;
			}
		}
		printf("Case #%d: %.8lf\n",kase,ret);
	}
	return 0;
}
