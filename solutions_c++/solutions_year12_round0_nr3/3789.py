#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <set>

using namespace std;

bool used[2010000];

int run(int a, int b)
{
	set<pair<int,int> > seta;
	int res = 0;
	char m[100] = "aasdasdasdsadsadasjdhkasdhkasdhkasd";
	char m2[100] = "aasdasdasdsadsadasjdhkasdhkasdhkasd";
	for (int i=a; i<=b; i++)
	{
		itoa(i,m,10);
		int len = strlen(m);

		bool first = false;
		for (int j=0; j<len; j++)
		{
			//shift
			{
				char t = m[0];
				for (int k=0; k+1<len; k++)
				{
					m[k] = m[k+1];
				}
				m[len-1] = t;
			}
			int val = atoi(m);

			//leading zero
			itoa(val,m2,10);
			int len2 = strlen(m2);
			if (len2 != len)
				continue;

			if (val >= a && val <= b && val > i)
			{
				seta.insert(make_pair(i,val));
				//printf("%d %d\n", i, val);
				res++;
			}
		}
	}
	return seta.size();
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++)
	{
		int a,b;
		scanf("%d%d", &a, &b);
		memset(used,0,sizeof(used));
		int res = run(a,b);
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}