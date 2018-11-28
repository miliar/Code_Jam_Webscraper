#include <iostream>
using namespace std;

int main(void)
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for ( int c = 1 ; c <= T ; c++ )
	{
		int n,k;
		scanf("%d %d",&n,&k);
		k = k%(1<<n);
		bool flag = 1;
		for ( int i = 0 ; i < n ; i++ )
		{
			if ( !(k&(1<<i)) )
			{
				flag = 0;
				break;
			}
		}
		if ( flag )
			printf("Case #%d: ON\n",c);
		else
			printf("Case #%d: OFF\n",c);

	}
//	system("pause");
	return 0;
}