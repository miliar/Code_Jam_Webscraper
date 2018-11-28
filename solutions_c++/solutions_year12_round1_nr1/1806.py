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
//	freopen("A.in","r",stdin);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-small-attempt0.in","r",stdin);freopen("A-large.ans","w",stdout);
	int testcase,A,B;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		printf("Case #%d: ",caseId);
		scanf("%d%d",&A,&B);
		double L[A],p[A+2],c[A+2];
		for (int i=0;i<A;i++)
		{
			cin>>L[i];
		}
		for(int i=0;i<A+2;i++)
			{p[i]=0;
			 c[i]=0;
			}
		p[0]=1;
		for(int i=1;i<=A;i++)
			{
				p[i]=p[i-1]*L[i-1];
			}
		p[A+1]=1;
		c[A+1]=p[A]*(B-A+1)+(1-p[A])*(2*B-A+2);
		c[0]=B+2;
		for(int i=0;i<A;i++)
			c[i+1]=p[i]*((A+B-2*i+1))+(1-p[i])*(A+2*B-2*i+2);
		double maxaa=1000000.0;
		for(int i=0;i<A+2;i++)
			if(c[i]<maxaa) maxaa=c[i];
		printf("%f",maxaa);
		printf("\n");

	}
	return 0;
}