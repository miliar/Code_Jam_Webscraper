#include <iostream>
using namespace std;


struct way
{
	int B,E,w;
};

way w[1000];

int cmp(const void* a, const void* b)
{
	return ((way*)a)->w - ((way*)b)->w;
}

int main()
{
	int X,S,R,t,N;
	int T;
	cin >> T;
	for(int c=1;c<=T;c++)
	{
		cin >> X >> S >> R >> t >> N;
		double tt = t;
		for(int i=0;i<N;i++)
		{
			cin >> w[i].B >> w[i].E >> w[i].w;
			X -= w[i].E - w[i].B;
		}
		qsort(w,N,sizeof(way),cmp);
		double times = 0;
		if((X+0.0)/R<=tt)
		{
			times = (X+0.0)/R;
			tt -= times;
		}
		else
		{
			times = (X - R * t + 0.0) / S + tt;
			tt = 0;
		}
		for(int i=0;i<N;i++)
		{
			int len = w[i].E - w[i].B;
			if((len+0.0)/(R+w[i].w) <= tt)
			{
				times += (len+0.0)/(R+w[i].w);
				tt -= (len+0.0)/(R+w[i].w);
			}
			else
			{
				times += (len - (R+w[i].w) * tt + 0.0) / (S+w[i].w) + tt;
				tt = 0;
			}
		}
		printf("Case #%d: %.7lf\n",c,times);
	}
}
