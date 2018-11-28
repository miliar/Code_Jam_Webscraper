#include <cstdio>
#include <string>
#include <vector>
#include <memory>
#include <cmath>
#include <algorithm>
#include <set>
#include <deque>
#include <stack>
#include <numeric>
#include <functional>
#include <map>
#include <queue>
using namespace std;
int main(void)
{
	int t,q,n,k,res;
	freopen("Ab.in","r",stdin);
	freopen("Ab.out","w",stdout);
	scanf("%d",&t);
	for (q=1;q<=t;q++)
	{
		scanf("%d%d",&n,&k);
		res=(1<<n)-1;
		k%=(1<<n);
		if (k==res)
			printf("Case #%d: ON\n",q); else
			printf("Case #%d: OFF\n",q);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}