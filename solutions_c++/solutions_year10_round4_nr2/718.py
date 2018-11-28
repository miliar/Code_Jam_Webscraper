#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <map>
#include <iostream>
#include <sstream>
#include <queue>
#include <cstring>
#include <ctime>
#include <cfloat>

using namespace std;

int p2[12];
int m[1200];
int tot[1200];
int price[12][1200];

int main()
{
	freopen("B-small-attempt1.in", "rt", stdin);
	freopen("B-small.out", "wt", stdout);

	//freopen("B-large.in", "rt", stdin);
	//freopen("B-large.out", "wt", stdout);

	int inp, kase, i, j, k, p;
	p2[0] = 1;
	for(i = 1; i < 12; i++)
	{
		p2[i] = p2[i - 1] * 2;
	}
	scanf("%d", &inp);
	
	for(kase = 1; kase <= inp; kase++)
	{
		scanf("%d", &p);
		for(i = 0; i < p2[p]; i++)
		{
			scanf("%d", &m[i]);
			tot[i] = p;
		}
		for(i = 0; i < p; i++)
		{
			for(j = 0; j < p2[p - i - 1]; j++)
			{
				scanf("%d", &price[i][j]);
			}
		}
		int mx;
		int mxind;
		int cnt = 0;
		while(true)
		{
			mx = 0;
			mxind = -1;
			for(i = 0; i < p2[p]; i++)
			{
				if(tot[i] - m[i] > mx)
				{
					mx = tot[i] - m[i];
					mxind = i;
				}
			}
			if(mx == 0)
				break;
			cnt += mx;
			int st = tot[mxind] - mx;
			for(i = 0; i < p2[p]; i++)
			{
				for(j = st + 1; j <= st + mx; j++)
				{
					if((mxind / p2[j]) == (i / p2[j]))
						tot[i]--;
				}
			}
		}
		printf("Case #%d: %d\n", kase, cnt);
	}
	
	return 0;

}
