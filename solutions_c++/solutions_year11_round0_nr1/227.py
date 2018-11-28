#include <cstdio>
#include <cmath>

void solve()
{
	int n;
	scanf("%d",&n);
	char c[1000];
	int pos_a = 1;
	int pos_b = 1;
	int time_a = 0;
	int time_b = 0;
	int last_time = 0;
	int next;

	for(int i = 0; i < n; ++i) {
		scanf("%s",c);
		scanf("%d",&next);
		if(c[0] == 'O') {
			time_a += fabs(pos_a - next)+1;
			pos_a = next;
			if(last_time >= time_a) time_a = last_time + 1;
			last_time = time_a;
		}
		else {
			time_b += fabs(pos_b - next)+1;
			pos_b = next;
			if(last_time >= time_b) time_b = last_time + 1;
			last_time = time_b;
		}
	}
	printf("%d\n",last_time);
}

int main(int argc, char *argv[])
{
	int kase;
	scanf("%d",&kase);
	for(int i = 1; i <= kase; ++i) {
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
