/*
 * in the name of god
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 */

#include <iostream>
#include <cstdio>

using namespace std;

const int maxN= 1000 + 5;

int Q,n;
int cost[maxN];

int main(){
	scanf ("%d", &Q);

	for (int t=1;t<=Q;t++){
		scanf ("%d", &n);

		int sum=0;

		for (int i=1;i<=n;i++){
			scanf ("%d", &cost[i]);
			sum= (sum^cost[i]);
		}

		printf ("Case #%d: " , t);

		if (sum!=0)
			printf ("NO\n");
		else{
			sort (cost+1, cost+n+1);
			sum=0;
			for (int i=2;i<=n;i++)
				sum+= cost[i];
			printf ("%d\n", sum);
		}
	}

	return 0;
}
