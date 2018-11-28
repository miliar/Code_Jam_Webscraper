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
#define maxSize 100000002
#define LL long long

LL getLarge(LL n)
{
	LL tmp = 1;
	for(LL i=1;i<=n;i++)
		tmp *=2;
	return tmp;
}
void getAC(LL n,LL k)
{
	LL tmp = getLarge(n);
	LL num1 = k % tmp;
	LL num2 = tmp-1;
	if(num1==num2)
		printf("ON\n");
	else printf("OFF\n");
	return ;
}
int main()
{
	freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		LL n,k;
		scanf("%I64d%I64d",&n,&k);
		printf("Case #%d: ",i);
		getAC(n,k);
	}
	return 0;
}
