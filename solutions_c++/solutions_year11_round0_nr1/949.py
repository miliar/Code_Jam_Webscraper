#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <deque>
#include <string>
#include <cmath>
#include <set>
#include <queue>
#include <map>
#define eps 1e-11
using namespace std;
int n, t, otime, btime, time, cp, bp; vector<int> c, w; char ch;
int main()
{
	scanf("%d", &t);
	for (int T=0; T<t; T++)
	{
		scanf("%d", &n); c.resize(n); w.resize(n);
		for (int i=0; i<n; i++)
		{
			scanf(" %c %d", &ch, &c[i]); if (ch=='B') w[i]=0; else w[i]=1;
		}
		cp=bp=1; otime=btime=time=0;
		for (int i=0; i<n; i++)
		{
			if (w[i])
			{
				btime+=max(0, abs(c[i]-cp)-otime)+1; time+=max(0, abs(c[i]-cp)-otime)+1; cp=c[i]; otime=0;
			}
			else
			{
				otime+=max(0, abs(c[i]-bp)-btime)+1; time+=max(0, abs(c[i]-bp)-btime)+1; bp=c[i]; btime=0;
			}
		}
		printf("Case #%d: %d\n", T+1, time);
	}
	return 0;
}
