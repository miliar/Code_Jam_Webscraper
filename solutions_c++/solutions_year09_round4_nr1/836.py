#include <vector>
#include <list>

#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;

#define FOR(i,n) for (int i = 0; i < n; i++) 
#define FOR1(i,n) for (int i = 1; i <= n; i++) 
#define SZ(x) ((int)x.size()) 
#define MEM(a,b) memset(a,b,sizeof(a))

int m[100];
int n;
int main()
{
	scanf("%d\n", &n);
	FOR(i, n)
	{
		int s;
		scanf("%d\n", &s);
		FOR(j, s)
		{
			int nb1=0;
			char buf[100];
			scanf("%s\n", buf);
			FOR(k, s)
				if(buf[k] == '1')
					nb1 = k;
			m[j] = nb1;
		}

		int rep = 0;
		FOR(j, s)
		{
			int mini = j-1;
			bool ok = true;
			for(int k = j; k < s && mini == j-1; k++)
			{
				if(m[k] <= j)
					mini = k;
				ok &= m[k] <= k;
			}
			if(!ok)
			{
			
			for(int k = mini; k > j; k--)
			{
				rep++;
				swap(m[k], m[k-1]);
			}

			}
		}
		printf("Case #%d: %d\n", i+1, rep);
	}
}
