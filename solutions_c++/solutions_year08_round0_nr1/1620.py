#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctype.h>
#include <bitset>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <queue>
#include <map>
#include <set>

using namespace std;

typedef long long ll;
#define dist2(x1, y1, x2, y2) (sqr((x1)-(x2)) + sqr((y1)-(y2))) 
#define mset(a, val) memset(a, val, sizeof(a))
#define deb(x) cout<<#x<<" = "<<(x)<<endl
#define all(a) (a).begin(),(a).end() 
#define ab(a) (((a)>0)?(a):(-(a))) 
#define sqr(a) ((a)*(a)) 
#define sz(a) int((a).size())

#define PB push_back
#define MP make_pair
#define INF 0x3fffffff
#define X first
#define Y second

char s[1000];

int main()
{
	int i, j, k, n, m;
	int max = 0, T;

	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	scanf("%d", &T);

	k = 1;
	while(k <= T)
	{
		scanf("%d\n", &n);
		map<string , int> mi;
		map<string , int>::iterator it, it2;

		int pt = 1;
		for(i = 0; i < n; i++)
		{
			gets(s);
			mi[s] = 0;
		}

		scanf("%d\n", &m);
		int res = 0, t;

		for(i = 0; i < m; i++)
		{
			gets(s);
			for(it = mi.begin(), t = 0; it != mi.end(); it++)
				if(it->second == 0)
					t++;
			if(mi[s] == 0 && t == 1 )
			{
				res++;
				for(it = mi.begin(), t = 0; it != mi.end(); it++)
					it->second = 0;
				mi[s]++;
			}
			else mi[s]++;
			

		}
		printf("Case #%d: %d\n", k, res);
	
		k++;
	}

	return 0;
}