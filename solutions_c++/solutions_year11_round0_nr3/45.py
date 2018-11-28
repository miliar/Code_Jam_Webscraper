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

template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}

int main()
{
	//freopen("C.in","r",stdin);
	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
	//freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for (int case_id=1;case_id<=testcase;case_id++)
	{
		printf("Case #%d: ",case_id);
		int n,s=0,g=0,m=1000000000;
		scanf("%d",&n);
		for (int i=0;i<n;i++)
		{
			int p;
			scanf("%d",&p);
			g^=p;
			s+=p;
			checkmin(m,p);
		}
		if (g==0)
			printf("%d\n",s-m);
		else
			printf("NO\n");
	}
	return 0;
}
