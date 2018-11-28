#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>

using namespace std;
int c,d,n,t,cases,i,lastb;

string a,b,x,tem;

int main()
{
	freopen("B-small-attempt5.in","r",stdin);
	freopen("B-small-attempt5.out","w",stdout);
	cin >> t;
	while (t--)
	{
		a.clear();
		b.clear();
		x.clear();
		scanf("%d",&c);
		if (c)
			cin >> a;
		scanf("%d",&d);
		if (d)
			cin >> b;
		scanf("%d",&n);
		cin >> x;
		lastb = -1;

		for (i = 0;i < x.size();i++)
		{
			if (i && c && ((a[0] == x[i - 1] && a[1] == x[i]) || (a[1] == x[i - 1] && a[0] == x[i])))
			{
				tem.clear();
				tem += a[2];
				if (lastb>= 0 && x[lastb] == x[i - 1] && lastb == i - 1 )
					lastb = -1;
				x.replace(i - 1,2,tem);
				i -= 2;
				continue;
			}
			if (d && lastb < 0 && (b[0] == x[i] || b[1] == x[i]))
			{
				lastb = i;
				continue;
			}
			if (d && lastb >= 0)
			{
				if ((x[lastb] == b[0] && x[i] == b[1] ) || (x[lastb] == b[1] && x[i] == b[0]))
				{
					x.erase(0,i + 1);
					i = -1;
					lastb = -1;
				}
			}
		}
		printf("Case #%d: [",++cases);
		if (x.size())
			printf("%c",x[0]);
		for (i = 1;i < x.size();i++)
			printf(", %c",x[i]);
		printf("]\n");
	}
}
