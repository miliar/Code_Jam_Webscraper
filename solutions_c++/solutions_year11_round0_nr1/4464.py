#include <iostream>

#define rep(i, n) for(int i=0; i<(n); i++)

using namespace std;

// I guess I know an algorithm in O(n), but it is more complex to implement.
// So, I wrote one in O(n^2), since constraints are small.

int main(void) {
	int T, N;
	char r[101];
	int p[101];

	int o_tar, b_tar;
	int o_pos, b_pos;
	int t, dt, cur;

	scanf("%d", &T);
	rep(u, T) {
		scanf("%d", &N);
		rep(i, N) scanf(" %c %d", &r[i], &p[i]);
		o_pos = 1;
		b_pos = 1;
		t = 0;

		rep(i, N) {
			o_tar = -1;
			b_tar = -1;
			for(int j=i; j<N && (o_tar == -1 || b_tar == -1); j++) {
				if (o_tar == -1 && r[j] == 'O') o_tar = p[j];
				if (b_tar == -1 && r[j] == 'B') b_tar = p[j];
			}
			//printf("## O(%d, %d) B(%d, %d)\n", o_pos, o_tar, b_pos, b_tar);
			if (o_tar == -1) o_tar = o_pos;
			if (b_tar == -1) b_tar = b_pos;
			if(r[i] == 'O') {
				dt = abs(o_tar - o_pos) + 1;
				t += dt;
				o_pos = o_tar;
				if (b_tar > b_pos) b_pos = min(b_pos+dt, b_tar);
				else if (b_tar < b_pos) b_pos = max(b_pos-dt, b_tar);
			} else {
				dt = abs(b_tar - b_pos) + 1;
				t += dt;
				b_pos = b_tar;
				if (o_tar > o_pos) o_pos = min(o_pos+dt, o_tar);
				else if (o_tar < o_pos) o_pos = max(o_pos-dt, o_tar);
			}
			//printf("$ i=%d dt=%d o_pos=%d b_pos=%d\n", i, dt, o_pos, b_pos);
		}

		printf("Case #%d: %d\n", u+1, t);
		fflush(stdout);
	}

	return 0;
}
