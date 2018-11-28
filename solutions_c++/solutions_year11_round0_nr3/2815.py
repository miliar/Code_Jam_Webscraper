#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
	freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
	int t;
	cin >> t;
	for(int cases=1;cases<=t;cases++)
	{
		int res=0,n;
		int minv = 10000000,sum=0;
		scanf("%d",&n);
		int num[2000];
		for(int i=0;i<n;i++)
		{
			scanf("%d",&num[i]);
			res ^= num[i];
			minv = std::min(minv,num[i]);
			sum += num[i];
		}
		if(res==0)
		{
		    printf("Case #%d: %d\n",cases,sum-minv);
		}
		else printf("Case #%d: NO\n",cases);
	}
	return 0;
}
