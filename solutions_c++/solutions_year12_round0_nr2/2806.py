#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

int getBest(int n){
	if(n == 0)return 0;
	if(n%3 == 0)return n/3;
	return n/3 + 1;
}

int getBestSurprising(int n){
	if(n == 0)return 0;
	if(n%3 == 0)return n/3 + 1;
	if((n-2)%3 != 0)return -1;
	return (n-2)/3 + 2;
}

int main()
{
	int t;
	scanf("%d", &t);
	int c = 1;
	while(t--){
		int n, s, p;
		scanf("%d %d %d", &n, &s, &p);
		int ans = 0;
		for(int i = 0; i < n; ++i){
			int g;
			scanf("%d", &g);
			int best = getBest(g);
			if(best >= p)
				ans++;
			else if (s > 0){
				best = getBestSurprising(g);
				if(best >= p){
					ans++;
					s--;
				}
			}
		}
		printf("Case #%d: %d\n",c++, ans);
	}
    return 0;
}
