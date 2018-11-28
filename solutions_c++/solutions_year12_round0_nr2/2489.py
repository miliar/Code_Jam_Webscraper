#include<cstdio>
#include<algorithm>

using namespace std;

int tt;
int n,s,p;
int pt;

#define NP 0
#define PS 1
#define PNS 2
#define P 3

int typ(int total)
{
	int mx=total/3;
	switch (total%3)
	{
		case 0:
			if (mx>=p)
			{
				if (mx&&mx+1<=10) return P;
				return PNS;
			}
			if (mx&&mx+1<=10&&mx+1>=p) return PS;
			return NP;
		case 1:
			if (mx+1>=p)
			{
				if (mx) return P;
				return PNS;
			}
			return NP;
		case 2:
			if (mx+1>=p)
			{
				if (mx+2<=10) return P;
				return PNS;
			}
			if (mx+2>=p&&mx+2<=10) return PS;
			return NP;
	}
	return NP;
}

int main()
{
	scanf("%d",&tt);
	for(int t=1;t<=tt;++t)
	{
		scanf("%d%d%d",&n,&s,&p);
		int sg=0,g=0;
		for(int i=0;i<n;++i)
		{
			scanf("%d",&pt);
			int k=typ(pt);
			switch (k)
			{
				case NP:
					break;
				case PS:
					sg++;
					break;
				case PNS:
				case P:
					g++;
					break;
			}
		}
		g+=min(sg,s);
		printf("Case #%d: %d\n",t,g);
	}
	return 0;
}
