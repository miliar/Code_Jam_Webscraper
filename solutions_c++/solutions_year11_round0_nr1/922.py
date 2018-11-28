#include <cstdio>

int dis(int a, int b) {
	int r = a - b;
	return r>0?r:-r;
}

int main (int argc, char const *argv[])
{
	int t;
	int n;
	int seq[100][2];
	scanf("%d", &t);
	int index = 0;
	while(t--) {
		index++;
		scanf("%d", &n);
		for(int i = 0; i < n; i++) {
			char c;
			scanf(" %c %d", &c, &seq[i][1]);
			if (c=='O') {
				seq[i][0] = 0;
			} else {
				seq[i][0] = 1;
			}
		}
		int total = 0;
		int pos[2] = {1, 1};
		int slot[2] = {0, 0};
		int current = seq[0][0];
		for(int i = 0; i < n; i++) {
			if (current != seq[i][0]) {
				current = (current+1)%2;
				int ts = dis(pos[current], seq[i][1]);
				ts = ts - slot[current];
				if (ts < 0) ts = 0;
				total += (ts + 1);
				slot[(current+1)%2] = ts+1;
				pos[current] = seq[i][1];
			} else {
				int ts = dis(pos[current], seq[i][1]) + 1;
				total += ts;
				slot[(current+1)%2] += ts;
				pos[current] = seq[i][1];
			}
		}
		printf("Case #%d: %d\n",index, total);
	}
	return 0;
}