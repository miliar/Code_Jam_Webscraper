#include <stdio.h>
#include <stdlib.h>
#define M 10000

#define OR 0
#define AND 1
#define INF (M*2)

int min(int a, int b)
{
    return a<b? a: b;
}


int main(void)
{
    int ncase;
    scanf("%d", &ncase);

    for (int casen=0; casen < ncase; casen++) {
	int ans = 0;

	int tree[M] = {0};
	int gate[M];
	int changable[M];
	int value[M];
	int dist[M][2];

	int m, v;
	scanf("%d %d", &m, &v);

	// interior
	for (int i=1; i<=(m-1)/2; i++) {
	    if (scanf("%d %d", &gate[i], &changable[i]) != 2) exit(1);
	}
	// leaf
	for (int i=(m-1)/2+1; i<=m; i++) {
	    if (scanf("%d", &value[i])!=1) exit(1);
	}

	for (int i=m; i>=(m-1)/2+1; i--) {
	    dist[i][value[i]] = 0;
	    dist[i][!value[i]] = INF;
	}

	for (int i=(m-1)/2; i>=1; i--) {
	    int l = i*2;
	    int r = i*2+1;

	    dist[i][0] = dist[i][1] = INF;
	    for (int v1=0; v1<2; v1++) {
		for (int v2=0; v2<2; v2++) {
		    if (gate[i] == AND) {
			dist[i][v1 && v2] = min(dist[i][v1 && v2], dist[r][v1] + dist[l][v2]);
		    } else if (gate[i] == OR) {
			dist[i][v1 || v2] = min(dist[i][v1 || v2], dist[r][v1] + dist[l][v2]);
		    }
		    if (changable[i]) {
			if (gate[i] == OR) {
			    dist[i][v1 && v2] = min(dist[i][v1 && v2], dist[r][v1] + dist[l][v2] + 1);
			} else if (gate[i] == AND) {
			    dist[i][v1 || v2] = min(dist[i][v1 || v2], dist[r][v1] + dist[l][v2] + 1);
			}
		    }
		}
	    }

	}

	//printf("%d %d\n", dist[1][0], dist[1][1]);


	if (dist[1][v] > m) {
	    printf("Case #%d: IMPOSSIBLE\n", casen+1);
	} else {
	    printf("Case #%d: %d\n", casen+1, dist[1][v]);
	}
    }
    return 0;
}

