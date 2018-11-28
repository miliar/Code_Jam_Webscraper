#include <cstdio>

int N, K;

void read() {
	scanf("%d%d", &N, &K);
}

void process() {
	int num = (1<<N);
	
	if ((K % num) == (num-1)) {
		printf("ON\n");
	} else {
		printf("OFF\n");
	}
}

int main() {
	
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int casos;
	scanf("%d", &casos);
	for (int i = 0; i < casos; i++) {
		read();
		printf("Case #%d: ", i+1);
		process();
	}

	return 0;
}