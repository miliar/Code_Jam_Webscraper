#include<iostream>
#include<algorithm>
#include<functional>

using namespace std;

bool invWL;

int W,L,n;

struct Node
{
	int r;
	int idx;
	int x,y;

	bool operator <(const Node& n2) const
	{
		return r>n2.r;
	}

	bool operator >(const Node& n2) const
	{
		return idx<n2.idx;
	}
} p[1000];

void output(int x, int y)
{
	if (x>W)
		printf("wtf1?");
	if (y>L)
		printf("wtf2?");
	if (invWL) swap(x,y);
	printf(" %d.00", x);
	printf(" %d.00", y);
	
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	cin>>T;
	for(int tt=1;tt<=T;tt++)
	{
		cin>>n>>W>>L;
		if (W>L)
		{
			invWL = true;
			swap(W,L);
		}
		else
			invWL = false;

		for(int i=0;i<n;i++)
		{
			cin>>p[i].r;
			p[i].idx = i;
		}

		sort(p,p+n);

		int ve = -1;
		int i=0;
		while(i<n)
		{
			int he = -1;
			int vn;
			if (ve==-1) vn = p[0].r;
			else vn = ve+2*p[i].r;
			while(i<n)
			{
				int x,y;
				if (he==-1)
				{
					x = 0;
					he = p[i].r;
				}
				else
				{
					x = he+p[i].r;
					he += 2*p[i].r;
				}
				if (x>W) break;
				if (ve==-1)
					y = 0;
				else
					y = ve+p[i].r;
				p[i].x = x; p[i].y = y;
				++i;
			}
			ve = vn;
		}

		sort(p,p+n,greater<Node>());

		printf("Case #%d:",tt);

		for(int i=0;i<n;i++)
			output(p[i].x,p[i].y);

		printf("\n");
	}

	return 0;
}