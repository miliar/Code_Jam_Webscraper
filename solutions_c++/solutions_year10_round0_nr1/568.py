#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int n,k;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.txt","w",stdout);
	int i,j;
	int cn=1,cs;
	scanf("%d",&cs);
	while(cs--)
	{
		scanf("%d%d",&n,&k);
		int tt = 1<<n;
		k %= tt;
		if(tt-1 == k) printf("Case #%d: ON\n",cn++);
		else printf("Case #%d: OFF\n",cn++);
	}
	return 0;
}
