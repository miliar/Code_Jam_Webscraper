#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

typedef long long ll;

int main()
{

	freopen("test.in" , "r" , stdin);
	freopen("A.out" , "w" , stdout);
	int t ,cas = 0;
	scanf("%d" , &t);
	while ( t-- )
	{
		int n , k;
		cas ++;
		scanf("%d %d" , &n , &k);
		ll B = (1LL << n);
		ll M = k % B;
		if (M == B - 1){
			printf("Case #%d: ON\n" , cas);
		}
		else{
			printf("Case #%d: OFF\n" , cas);
		}
	}

}