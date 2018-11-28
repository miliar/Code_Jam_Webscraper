#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <set>
struct A 
{
	int a, b;
	A( int _a, int _b):a(_a),b(_b){}

};
bool operator< ( const A &v1, const A &v2)
{
	return (v1.a < v2.a) || ( v1.a == v2.a && v1.b < v2.b); 
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	char buf[20];
	int count;
	scanf("%d",&count);
	int k = 0;
	while (count--)
	{
		std::set<A> v;
		int min, max;
		scanf("%d%d",&min,&max);
		//int res = 0;
		for ( int i = min; i<=max; ++i)
		{
			itoa(i, buf, 10);
			int len = strlen(buf);
			
			for (int j = 0; j < len -1; ++j)
			{
				buf[len+j] = buf[j];
				buf[len+j+1] = '\0';
				if (buf[j+1] == 0 )
				{
					continue;
				}
				int x = atoi(&(buf[j+1]));
				if( i < x && x <= max )
				{
					//printf("%d-%d\n",i ,x);
					v.insert(A(i,x));
					//res++;				
				}
			}
		}
		printf("Case #%d: %d\n",++k,v.size());
	}
	return 0;
}