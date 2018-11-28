#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>

using namespace std;

const int N=10000;

struct xxx{
	int d,l,k,v;
};

int i,j,k,m,n,l;
xxx a[N+10];

bool cmp(xxx a, xxx b)
{
	return a.d<b.d;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int cas=1; cas<=T; cas++)
	{

		
		scanf("%d", &n);
		for (i=1; i<=n; i++)
		{
			scanf("%d%d", &a[i].d, &a[i].l);
			a[i].k=0;
			a[i].v=false;
		}
		n++;
		scanf("%d", &a[n].d);
		a[n].l=0;
		a[n].v=false;
		
		sort(a+1, a+n+1, cmp);

		if (a[1].l>=a[1].d)
			a[1].k=a[1].d;
		for (i=1; i<=n; i++) if (a[i].k)
			for (j=i+1; j<=n; j++)
			{
				if (a[j].d<=a[i].d+a[i].k)
				{
					a[j].v=true;
					
					a[j].k=max(a[j].k, min(a[j].l, a[j].d-a[i].d));
				}
				else
					break;
			}

            
		printf("Case #%d: ",cas);
		if (a[n].v)
			cout<<"YES"<<endl;
		else
			cout<<"NO"<<endl;
		
	}
	return 0;
}
