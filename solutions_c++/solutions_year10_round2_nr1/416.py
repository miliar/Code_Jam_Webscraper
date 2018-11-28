#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

struct ele{
	string name;
	int depth;
};
char str[1000000];

map < string , bool > h;

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
		int n , m;
		h.clear();
		scanf("%d %d" , &n , &m);
		int i , j;
		for (i = 0 ; i < n ; i ++){
			scanf("%s" , str);
			int len = strlen(str);
			string dir = str;
			h[dir] = 1;
		}
		int ans = 0;
		for (i = 0 ; i < m ; i ++){
		
			scanf("%s" , str);
			if (h[str] == 1)continue;
			int len = strlen(str);
			string root = "/";
			for (j = 1 ; j <= len ; j ++){
				if (j == len || str[j] == '/'){
					if (h[root] == 0){
						h[root] = 1;
						ans ++;
					}
				}
				root = root + str[j];
			}

		}

		printf("Case #%d: %d\n" , cas , ans);
	}
}