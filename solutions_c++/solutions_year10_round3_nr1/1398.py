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
int N;
long long a[10000],b[10000];
int countt;
int main()
{
//	freopen("A.txt","r",stdin);freopen("B.txt","w",stdout);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
        countt=0;
		scanf("%d",&N);
		for(int i=0;i<N;i++)
		scanf("%ld %ld",&a[i],&b[i]);
		
		for(int i=1;i<N;i++)
		for(int j=i-1;j>=0;j--)
		if(  (a[i]-a[j])*(b[i]-b[j]) < 0)
		countt++;
		
		printf("Case #%d: %d\n",caseId,countt);
		
		
	}
	return 0;
}
