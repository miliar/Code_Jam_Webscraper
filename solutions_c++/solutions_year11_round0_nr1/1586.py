#include <vector>
#include <list>
#include <map>
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
#include <ctime>
#include <cstring>

using namespace std;

int main()
{
	int t;
	scanf("%d", &t);
	int tt = t;
	while(t--)
	{
		//printf("sad");
		int n, bt=0, ot=0, bp=1, op=1, pt=0;
		scanf("%d", &n);
		while(n--)
		{
			//cout<<"n:"<<n;
			char c;
			int m;
			scanf("%c", &c);
			scanf("%c", &c);
			scanf("%d", &m);
			if(c == 'O')
			{
				ot = max(ot + abs(m-op) + 1, pt+1);
				op = m;
				pt = ot;
			}
			else if(c == 'B')
			{
				bt = max(bt + abs(m-bp) + 1, pt+1);
				bp = m;
				pt = bt;
			}
			//n--;
		}
		printf("Case #%d: %d\n", tt-t, pt);
	}
	return 0;
}
