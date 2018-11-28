
#include <cstdio>


int main()
{
	freopen("output.txt", "w", stdout);
	int n; scanf("%d", &n);
	for(int i = 0; i<n; i++){
		int a, b; scanf("%d%d", &a, &b);
		if(((1<<a)-1)==(b&((1<<a)-1))) printf("Case #%d: ON\n", i+1);
		else printf("Case #%d: OFF\n", i+1);
	}
}

