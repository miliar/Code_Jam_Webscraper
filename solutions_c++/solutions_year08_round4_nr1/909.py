#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <string>
#include <vector>
#include <sstream>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std;

#define AND 1
#define OR 0

int type[10][1000], values[10][1000], leaf[10][1000];
int changes[25][2];
int n, expected, total, possible, ans;

int calc(int i, int j) {
	//printf("%d %d\n",i,j);
	if (leaf[i][j])
		return values[i][j];
	else {
		if (type[i][j] == AND)
			return calc(i+1,2*j) && calc(i+1,2*j+1);
		return calc(i+1,2*j) || calc(i+1,2*j+1);
	}
}

void all(int i, int n) {
	if (i == n) {
		if (calc(0,0) == expected) {
			if (ans == -1 || total < ans)
				ans = total;
		}
	}
	else {
		type[changes[i][0]][changes[i][1]] = 1 - type[changes[i][0]][changes[i][1]], total++, all(i+1,n);
		type[changes[i][0]][changes[i][1]] = 1 - type[changes[i][0]][changes[i][1]], total--, all(i+1,n);
	}
}

int main() {
	int cases, t = 1;
	int k, i, j, a, b;
	
	scanf("%d",&cases);
	while (cases--) {
		scanf("%d %d",&n,&expected);
		memset(leaf,0,sizeof(leaf));
		
		i = j = 0, possible = 0;
		for (k=0; k < (n-1)/2; k++) {
			scanf("%d %d",&a,&b);
			type[i][j] = a;
			if (b) {
				changes[possible][0] = i;
				changes[possible][1] = j;
				possible++;
			}
			j++;
			if ((1<<i) == j)
				i++, j = 0;
		}
		for ( ; k < n; k++) {
			scanf("%d",&values[i][j]);
			leaf[i][j] = 1;
			j++;
			if ((1<<i) == j)
				i++, j = 0;
		}
		
		total = 0, ans = -1;
		all(0,possible);
		printf("Case #%d: ",t++);
		if (ans == -1)
			puts("IMPOSSIBLE");
		else
			printf("%d\n",ans);
	}
	
	return 0;
}
