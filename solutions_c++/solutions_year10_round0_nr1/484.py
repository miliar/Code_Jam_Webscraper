#include <iostream>
using namespace std;
int i,j,n,m,testcase,curcase = 1;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	for ( scanf("%d\n",&testcase) ; curcase <= testcase ; curcase++ )
	{
		scanf("%d %d\n",&n,&m);
		for ( i = 0 ; i < n ; i++ )
			if ((( 1 << i )&m)==0) break;
		printf("Case #%d: ",curcase);
		if (i==n) printf("ON\n"); else printf("OFF\n");
	}
}
