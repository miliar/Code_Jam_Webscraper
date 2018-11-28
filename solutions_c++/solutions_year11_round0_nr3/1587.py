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
		int n, fin=0, min=10000001, tot=0;
		scanf("%d", &n);
		
		while(n--)
		{
			int num;
			scanf("%d", &num);
			fin ^= num;
			if(min > num) min = num;
			tot += num;
		}
		
		if(fin == 0)
			printf("Case #%d: %d\n", tt-t, tot - min);
		else
			printf("Case #%d: NO\n", tt-t);	
			
	}
	return 0;
}
