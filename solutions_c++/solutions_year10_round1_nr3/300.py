#include<stdio.h>
#include<map>

using namespace std;

map< pair<int, int>, int > a;

int Go(int l1, int l2)
{
	if(l1 == l2) return 0; // loser
	if(l1 > l2) return Go(l2, l1);

	if(l1 == 1) return 1;

	if(a.count(make_pair(l1, l2))) return a[make_pair(l1,l2)];
	else
	{
		int l3;
		a[make_pair(l1,l2)] = 0;
		for(l3=1;;l3++)
		{
			if(l2 - l1*l3 < 0) break;

			if(Go(l1, l2-l1*l3) == 0)
			{
				a[make_pair(l1,l2)]=1;
				break;
			}
		}
		return a[make_pair(l1,l2)];
	}
}

int main(void)
{
	int T;
	int v1, v2, w1, w2;
	int l1, l2, l0;

	freopen("C1.in","r",stdin);
	freopen("C1.out","w",stdout);

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		scanf("%d %d %d %d",&v1,&v2,&w1,&w2);
		int ret = 0;
		for(l1=v1;l1<=v2;l1++)
		{
			for(l2=w1;l2<=w2;l2++)
			{
				ret += Go(l1, l2);
			}
		}
		printf("Case #%d: %d\n",l0,ret);
		fflush(stdout);
	}

	return 0;
}