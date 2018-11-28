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
int N,K;
bool r;
int maxn;
int cur;
void init()
{
	maxn = pow(2,N);
	cur = K%maxn;
}
int solve()
{
	r = (cur == maxn -1) ? true:false;
	return 0;
}
int main()
{
//	freopen("a-test.in","r",stdin);//freopen("a-test.out","w",stdout);
//	freopen("A-small-attempt0.in","r",stdin);freopen("a-small.out","w",stdout);
	freopen("a-large.in","r",stdin);freopen("a-large.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		scanf("%d%d",&N,&K);
		init();
		solve();
		printf("Case #%d: ",caseId);
		if(r == true)
			printf("ON\n");
		else
			printf("OFF\n");
		cerr<<caseId<<"/"<<testcase<<endl;
	}
	return 0;
}