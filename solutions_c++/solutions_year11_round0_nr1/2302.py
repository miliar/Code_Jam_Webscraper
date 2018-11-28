#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;
int solve()
{
	int n;
	scanf("%d",&n);
	int timeO=0,timeB=0;
	int posO=1,posB=1;
	for(int i=0;i<n;i++)
	{
		char str[1024];
		scanf("%s",str);
		int z;
		scanf("%d",&z);
		if(*str=='O')
		{
			timeO=max(timeB+1,timeO+abs(posO-z)+1);
			posO=z;
		}
		else
		{
			timeB=max(timeO+1,timeB+abs(posB-z)+1);
			posB=z;
		}
	}
	return max(timeO,timeB);
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		printf("Case #%d: %d\n",i,solve());
	}
	return 0;
}
