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
	//freopen("D.in","r",stdin);
	freopen("D-small-attempt0.in","r",stdin); freopen("D-small-attempt0.out","w",stdout);
	//freopen("D-large.in","r",stdin); freopen("D-large.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for (int case_id=1;case_id<=testcase;case_id++)
	{
		int n,s=0,p;
		scanf("%d",&n);
		for (int i=1;i<=n;i++)
		{
			scanf("%d",&p);
			if (p!=i) s++;
		}
		printf("Case #%d: %.9lf\n",case_id,(double)s);
	}
	return 0;
}
