#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	freopen("a.txt", "r", stdin);
	freopen("C-small-out0.txt", "w", stdout);

	int T, R, k, N;
	int t, i, j;
	int sum, pr, money;
	int g[1200], next[1200];

	scanf("%d", &T);
	for (t=1; t<=T; ++t) {
	    scanf("%d%d%d", &R, &k, &N);
	    for (i=0; i<N; ++i){
	        scanf("%d", &g[i]);
	        next[i] = i+1;
	    }
	    next[N-1] = 0;

	    money = sum = pr = 0;
	    while (R -- ) {
            for (sum=i=0; i<N; ++i) {
                if (sum + g[pr] > k) break; // Тњди

                sum += g[pr];
                pr = next[pr];
            }

            money += sum;
	    }

	    printf("Case #%d: %d\n", t, money);
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}
