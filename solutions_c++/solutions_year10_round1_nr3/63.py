#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;

const double phi = (1+sqrt(5))/2;

typedef long long ll;

int main(){
	int lz;
	scanf("%d", &lz);
	for(int cnt = 1; cnt <= lz; cnt++){
		int a1, a2, b1, b2;
		scanf("%d%d%d%d", &a1, &a2, &b1, &b2);
		ll res = 0;
		for(int a = a1; a <= a2; a++){
			int guess = ((int)(a*phi))+1;
			int lim = max(guess, b1);
			res += max(0, b2-lim+1);
		}
		swap(a1, b1);
		swap(a2, b2);
		for(int a = a1; a <= a2; a++){
			int guess = ((int)(a*phi))+1;
			int lim = max(guess, b1);
			res += max(0, b2-lim+1);
		}		
		printf("Case #%d: %lld\n", cnt, res);
	}

	return 0;
}
