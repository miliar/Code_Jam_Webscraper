#include <vector>
#include <list>
#include <map>
#include <set>
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
#include<math.h>
using namespace std;
__int64 power(__int64 x,__int64 y)
{
	__int64 ans=1;
	for(int i=0;i<y;i++)
		ans*=x;
	return ans;
}
int main()
{
	//freopen("A-small-attempt0.in","r",stdin); freopen("A-small-attempt0.out","w",stdout);
	//freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	freopen("B-small-attempt0.in","r",stdin); freopen("B-small-attempt0.out","w",stdout);
	//freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
	//freopen("C-small-attempt0.in","r",stdin); freopen("C-small-attempt0.out","w",stdout);
	//freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
	int cases;
	scanf("%d",&cases);
	for(int cas=1;cas<=cases;cas++)
	{
		__int64 L,P,C;
		cin>>L>>P>>C;
		int ans;
		for(int i=0;;i++)
		{
			if(L*power(C,power(2LL,i))>=P)
			{
				ans=i;
				break;
			}
		}
		printf("Case #%d: %d\n",cas,ans);
	}
}

