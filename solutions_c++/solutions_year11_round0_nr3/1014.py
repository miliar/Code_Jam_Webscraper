#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
    int t;
    scanf("%d", &t);

    for(int z = 1; z <= t; z++) {
	int n;
	scanf("%d", &n);

	int x = 0, sum = 0, mini = 999999999;
	for(int i = 0; i < n; i++) {
	    int tmp;
	    scanf("%d", &tmp);

	    x ^= tmp;
	    mini = min(mini, tmp);
	    sum += tmp;
	}

	if(x != 0)
	    printf("Case #%d: NO\n", z);
	else
	    printf("Case #%d: %d\n", z, sum - mini);
    }
}
