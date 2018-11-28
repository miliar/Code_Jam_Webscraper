
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
	//freopen("A.in","r",stdin);
	//freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	int n;
	int A[1001],B[1001];
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		printf("Case #%d: ",caseId);
		scanf("%d",&n);
		for (int i=0;i<n;i++)
		{
			scanf("%d%d",A+i,B+i);
		}
		int ans=0;
		for (int i=0;i<n;i++)
		{
			for (int j=i+1;j<n;j++)
			{
				if ((A[i]-A[j])*(B[i]-B[j])<0)
				{
					ans++;
				}
			}				
		}
		printf("%d\n",ans);

			fflush(stdout);
	}
	return 0;
}
