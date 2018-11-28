#include <iomanip>
#include <algorithm>
#include <map>
#include <fstream>
#include <stack>
#include <queue>
#include <vector>
#include <cmath>
#include <iostream>
#include <string>
#include <set>

#include <time.h>
#include <sys/time.h>

using namespace std;


int main()
{
//	freopen("anarc05b.in","r",stdin);
//	freopen("anarc05b.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int t = 0; t < T; t++)
	{
		printf("Case #%d: ",t+1);

		int n;
		int x1 = 1, t1 = 0;
		int x2 = 1, t2 = 0;
		int tt = max(t1,t2);

		scanf("%d",&n);
		for (int i = 0; i < n; i++)
		{
			char s;
			int o;
			cin >> s >> o;
			
			if (s == 'O')
			{
				int p = x1 - o;
				if (p < 0) p = -p;
				p++;
				t1+=p;
				if (t1 <= tt) t1 = tt+1;
				if (t1 > tt) tt = t1;
				x1 = o;
			}
			else
			{
				int p = x2 - o;
				if (p < 0) p = -p;
				p++;
				t2+=p;	
				if (t2 <= tt) t2 = tt + 1;
				if (t2 > tt) tt = t2;
				x2 = o;
			}
		}
		printf("%d\n",tt);
	}

//	in.getline(s);

	return 0;	
}
