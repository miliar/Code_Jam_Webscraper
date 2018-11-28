#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
    int d[10000];
    const int M = 100000;
    int t, n;
    int a, b;

    scanf("%d", &t);
    for (int icas = 1; icas <= t; icas ++){
	scanf("%d", &n);
	for (int i = 0; i < n; i ++){
	    scanf("%d %d", &a, &b);
	    d[i] = a * M + b;
	}
	sort(d, d + n);
	for (int i = 0; i < n; i ++)
	    d[i] = d[i] % M;
	int ans = 0;
	for (int i = 0; i < n; i ++)
	    for (int j = i+1; j < n; j ++){
		if (d[j] < d[i])
		    ans ++;
	    }
        printf("Case #%d: %d\n", icas, ans);
    }
    return 0;
}
	
	
