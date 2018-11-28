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

class node
{
public:
	int a;
	int b;
};
int N=0;
int a,b=0;
int ans = 0;
vector<node> nodeVec;

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		printf("Case #%d:",caseId);
		scanf("%d",&N);
		string str;
		for (int i=0;i<N;i++) 
		{
			scanf("%d%d", &a,&b);
			node p;
			p.a = a;
			p.b = b;
 			nodeVec.push_back(p);
		}

		for (int i=0; i<nodeVec.size(); i++)
		{
			for (int j=1; j<nodeVec.size(); j++)
			{
				if ((nodeVec[i].a < nodeVec[j].a && nodeVec[i].b > nodeVec[j].b)
					||(nodeVec[i].a > nodeVec[j].a && nodeVec[i].b < nodeVec[j].b))
				{
					ans++;
				}
			}
		}
		printf(" %d\n",ans);
		ans = 0;
		nodeVec.clear();
		fflush(stdout);
	}
	return 0;
}