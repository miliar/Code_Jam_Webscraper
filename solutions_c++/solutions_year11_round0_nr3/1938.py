#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <cctype>
#include <assert.h>
using namespace std;

#define forn(i,n) for(int i=1;i<=n;i++)

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int t,n,x;
	scanf("%d",&t);
	forn(tcase,t)
	{
		int min=1000006;
		int ans=0,temp=0;
		scanf("%d",&n);
		scanf("%d",&x);
		temp=x;
		ans=x;
		if(x<min)
			min=x;
		n--;
		while(n--)
		{
			scanf("%d",&x);
			if(min>x)
				min=x;
			ans+=x;
			temp^=x;
		}
		if(temp!=0)
			printf("Case #%d: NO\n",tcase);
		else
			printf("Case #%d: %d\n",tcase,ans-min);
	}
	return 0;
}