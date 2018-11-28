#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

int x[100];
int v[100];
map < string , bool > h;

struct ele{
	int x;
	int v;
};

bool cmp(ele a , ele b)
{
	return a.x < b.x;
}

int main()
{
	freopen("test.in" , "r" , stdin);
	freopen("test.out" , "w" , stdout);

	int t;
	int cas = 0;
	scanf("%d" , &t);
	while (t --)
	{
		cas ++;


		int n , k , b , t;
		int ans = 0;

		scanf("%d %d %d %d" , &n , &k , &b , &t);
		int i , j;
		for (i = 0 ; i < n ; i ++)
			scanf("%d" , &x[i]);
		for (i = 0 ; i < n ; i ++)
			scanf("%d" , &v[i]);
		ele e[100];

		for (i = 0 ; i < n ; i ++){
			e[i].x = x[i];
			e[i].v = v[i];
		}
		sort(e , e + n , cmp);
		int tp = 0;
		for (i = n - 1 ; i >= 0 ; i --){
			if (k == 0)break;
			if ( b - e[i].x > e[i].v * t){
				tp ++;
			}
			else{
				k --;
				ans += tp;
			}
			
		}
		if (k > 0)
			printf("Case #%d: IMPOSSIBLE\n" , cas);
		else printf("Case #%d: %d\n" , cas , ans);
	}
}