#include <stdio.h>
#include <map>

using namespace std;

int main()
{
	int n;
	scanf("%d", &n);
	for (int ca=1; ca<=n; ca++)
	{
		int t, na, nb;
		scanf("%d%d%d", &t, &na, &nb);
		
		map<int,int> ma, mb;
		for (int i=0; i<na+nb; i++)
		{
			int sh, sm, th, tm;
			scanf("%d:%d %d:%d", &sh, &sm, &th, &tm);
			int st = sh * 60 + sm;
			int tt = th * 60 + tm + t;

//			printf("st tt: %d %d\n", st, tt);
			if (i < na)
			{
				ma[st]--;
				mb[tt]++;
			}
			else
			{
				mb[st]--;
				ma[tt]++;
			}
		}
		int xa = 0, xb = 0, c = 0;
		
		c=0;
		for (map<int,int>::iterator it=ma.begin(); it!=ma.end(); it++)
		{
			c += it->second;
			if (c < 0)
			{
				xa-=c;
				c=0;
			}
		}
		c=0;
		for (map<int,int>::iterator it=mb.begin(); it!=mb.end(); it++)
		{
//			printf("%d %d\n", it->first, it->second);
			c += it->second;
			if (c < 0)
			{
				xb-=c;
				c=0;
			}
		}
		printf("Case #%d: %d %d\n", ca, xa, xb);
		
	}
	return 0;
}
