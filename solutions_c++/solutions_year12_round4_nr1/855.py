#include <cmath>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cctype>
#include <stack>
using namespace std;

typedef long long int int64;

#define EPS 10e-9
#define INF 0x3f3f3f3f

#define MAXN 10500

int v[MAXN][2];
int d, n;
int dis[MAXN];

int main()
{	
	int t;
	scanf("%d", &t);
	for (int k = 0; k < t; k++) {
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d %d", &v[i][0], &v[i][1]);
		}
		scanf("%d", &d);
		memset(dis, INF, sizeof(dis));
		for (int i = n-1; i >= 0; i--) {
			if (d - v[i][0] <= v[i][1]) {
				dis[i] = d - v[i][0];	
			}
			for (int j = i+1; j < n; j++) {
				if (v[j][0] - v[i][0] <= v[i][1]) {
					if (v[j][0] - v[i][0] >= dis[j]) {
						dis[i] = min(dis[i], v[j][0] - v[i][0]);	
					} 	
				}	
			}
		}
		printf("Case #%d: ", k+1);
		if (dis[0] <= v[0][0]) {
			printf("YES\n");	
		}
		else {
			printf("NO\n");	
		}
	}
	return 0;
}