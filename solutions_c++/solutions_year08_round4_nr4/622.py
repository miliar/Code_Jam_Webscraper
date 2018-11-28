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

#define PI 3.14159265358979323846264338327950288
#define MOD 1000
typedef __int64 int64;

int next[10],n;
char* solve(char *t)
{
	char tmp[1024];
	int i,j;
	memset(tmp,'\0',sizeof(tmp));
	for(i=0;t[i];i+=n)
	{
		for(j=0;j<n;j++)
		{
			tmp[i+j]=t[i+next[j]];
		}
	}
	tmp[i+n]=0;
	return tmp;
}

int doit(char *t)
{
	char x=t[0];
	int ans=1,i;
	for(i=1;t[i];i++)
	{
		if(x!=t[i])
		{
			ans++;
			x=t[i];
		}
	}
	return ans;
}
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	//freopen("D-large.in","r",stdin);
	//freopen("D-large.out","w",stdout);
	int cas,ca;
	char s[1024];
	for(scanf("%d",&cas),ca=1;ca<=cas;ca++)
	{
		printf("Case #%d: ",ca);

		scanf("%d",&n);
		scanf("%s",s);
		for(int i=0;i<n;i++)next[i]=i;
		int ans=1<<30;
		do
		{
			ans=min(ans,doit(solve(s)));
		}while(next_permutation(next,next+n));
		printf("%d\n",ans);
	}
}


