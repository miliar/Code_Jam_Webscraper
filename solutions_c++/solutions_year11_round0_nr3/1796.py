#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int data[1100];

int main () {
	freopen("C-large.in.txt", "r", stdin);
	freopen("C-large.out.txt", "w", stdout);
	int T, N, i, sum=0, Case=0;
	scanf("%d", &T);
	while(T--) {
		Case++;
		sum=0;
		scanf("%d", &N);
		for(i=0;i<N;i++) {
			scanf("%d", &data[i]);
			sum^=data[i];
		}
		if(sum)
			printf("Case #%d: NO\n", Case);
		else {
			sort(data, data+N);
			for(i=1;i<N;i++)
				sum+=data[i];
			printf("Case #%d: %d\n", Case, sum);
		}
	}
	return 0;
}