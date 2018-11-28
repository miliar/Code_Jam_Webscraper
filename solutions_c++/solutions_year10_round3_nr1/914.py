#include<iostream>
using namespace std;
const int maxn = 1003;
struct node
{
	int a,b;
};
node win[maxn];

int main( )
{
	int n, t, i, j, cnt, k = 1;
	freopen("A-large.in","r",stdin);
	freopen("out1.txt","w",stdout);
	scanf("%d",&t);
	while( t-- )
	{
		scanf("%d",&n);
		for( i = 0; i < n; i++ )
			scanf("%d%d",&win[i].a,&win[i].b);
		cnt = 0;
		for( i = 0; i < n; i++ )
			for( j = 0; j < n; j++ )
				if( win[j].a > win[i].a && win[j].b < win[i].b )
					cnt++;
		printf("Case #%d: %d\n",k++, cnt);
	}
	return 0;
}