


#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int n, k;
	int t;
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &t);
	int icase =0 ;
	while(t--) {
		scanf("%d%d", &n, &k);
		++k;
		bool flag = k%((int)pow((double)2, n)) == 0;
		printf("Case #%d: %s\n", ++icase, (flag?"ON":"OFF") );
	}
}
