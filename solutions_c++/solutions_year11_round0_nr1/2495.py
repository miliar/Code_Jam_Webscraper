#include<cstdio>
#include<cmath>

using namespace std;

int main() {
	int i, T;
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	scanf("%d\n", &T);

	for (i = 0; i < T; i++) {
		int startO = 0;
		int lastO = 1;
		int startB = 0;
		int lastB = 1;
		int n, poz, j;
		char turn;
		scanf("%d ", &n);
		for (j = 0; j < n; j++) {
			scanf("%c %d ", &turn, &poz);

			if (turn == 'O') {
				startO += abs(lastO - poz) + 1;
				lastO = poz;

				if(startO <= startB) startO = startB + 1;
			}
			else {
				startB += abs(lastB - poz) + 1;
				lastB = poz;

				if(startB <= startO) startB = startO + 1;			
			}
		}
		printf("Case #%d: %d\n",i+1, startB > startO?startB:startO );
	}

	return 0;
}