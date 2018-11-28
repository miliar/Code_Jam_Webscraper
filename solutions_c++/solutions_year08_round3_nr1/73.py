#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;


int used[1005] ;
bool compare(const int & a, const int & b)
{
	return a > b;
}
int main(void)
{
	int cases ;
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&cases);
	int f = 0;
	while( cases -- )
	{
		int p , k , l ,i,j;
		scanf("%d %d %d",&p,&k,&l);
		for(i = 0 ; i < l ; i ++)
		{
			scanf("%d",&used[i]);
		}
		__int64 total = 0;
		sort(used ,used + l , compare);
		int current = 0;
		printf("Case #%d: ",++f);
		if( p * k < l)
		{
			printf("Impossible\n") ; continue;
		}
		for(i = 1 ; i <= p ; i ++)
		{
			for(j = 0 ; j < k ; j ++ )
			{
				if(current + j == l)
					break;
				total += i * used[current + j];
			}
			if(j != k)
				break;
			current += k;
		}
	printf("%I64d\n",total);
	}
	return 0;
}