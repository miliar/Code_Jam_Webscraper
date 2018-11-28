#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
using namespace std;

int main()
{
	//freopen("in.txt","r", stdin);
	//freopen("out.txt","w",stdout);
	int t,n,k;
	int l;
	scanf("%d",&t);
	for(int c = 1;c<=t;c++)
	{
		scanf("%d%d",&n,&k);
		l = 1;
		for(int i = 0;i<n;++i)
			l = l*2;
		if ( k==l-1 || (k-l+1)%l==0)
			printf("Case #%d: ON\n",c);
		else
			printf("Case #%d: OFF\n", c);
	}
	return 0;
}
