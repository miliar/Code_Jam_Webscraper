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
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for (int case_id=1;case_id<=testcase;case_id++)
	{
		printf("Case #%d: ",case_id);
		int n,s=0,t1=0,t2=0,p1=1,p2=1;
		scanf("%d",&n);
		for (int i=0;i<n;i++)
		{
			char str[10];
			int p;
			scanf("%s%d",str,&p);
			if (str[0]=='O')
			{
				s=t1=max(s,t1+abs(p-p1))+1;
				p1=p;
			}
			else
			{
				s=t2=max(s,t2+abs(p-p2))+1;
				p2=p;
			}
		}
		printf("%d\n",s);
	}
	return 0;
}
