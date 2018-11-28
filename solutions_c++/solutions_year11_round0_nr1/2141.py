#include<iostream>
#include<vector>
#include<cstdio>
#include<algorithm>
using namespace std;
struct robot {
	int push_time;
	int point;
} bot[2];
main() {
	int t, n, no = 1, n_t;
	char b;
	int x, time, ind;
	scanf("%d", &t);
	while(t--) {
		scanf("%d", &n);
		bot[0].push_time = 0;
		bot[0].point = 1;
		bot[1].push_time = 0;
		bot[1].point = 1;
		time = 0;
		for(int i = 0; i < n; i++) {
			scanf(" %c %d", &b, &x);
//			cout<<b<<" "<<x<<endl;
			if(b == 'O')
				ind = 0;
			else
				ind = 1;
			n_t = abs(bot[ind].point - x);
			n_t = max(n_t + bot[ind].push_time, time);
			time = n_t + 1;
			bot[ind].point = x;
			bot[ind].push_time = time;
		}
		printf("Case #%d: %d\n", no++, time);
	}
}
