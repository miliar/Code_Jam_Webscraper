#include <functional>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <string>
#include <vector>
#include <cstdio>
#include <bitset>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;
#define MAXN 1005

int w[MAXN],n;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	//printf("Algorithm is Beautiful!\n");
	int T,casetest=1;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",casetest++);
		scanf("%d",&n);
		int cnt=0,ans=0;
		for(int i=1;i<=n;i++)
		{
			scanf("%d",&w[i]);
			cnt=cnt^w[i];
			ans+=w[i];
		}
		sort(w+1,w+n+1);
		if(cnt!=0)printf("NO\n");
		else
		{
			printf("%d\n",ans-w[1]);
		}
	}
	return 0;
}