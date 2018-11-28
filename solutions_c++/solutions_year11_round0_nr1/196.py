#include<cstdio>
#include<cstring>
#include<algorithm>
#include<queue>

using namespace std;

int main() {
	int T, n, t, pos, b[2], o[2];
	char op;
	
	scanf("%d", &T);
	
	for(int nCase = 1; nCase <= T; nCase++) {
		scanf("%d ", &n);
		
		deque<int> pb, po;
		b[0] = o[0] = 1;
		b[1] = o[1] = 0;
		
		t = 0;
		for(int i = 0; i < n; i++) {
			scanf("%c %d ", &op, &pos);
			
			if(op == 'B') {
				t += max(0, abs(pos - b[0]) - (t - b[1]));
				b[0] = pos;
				b[1] = t + 1;
			} else if(op == 'O') {
				t += max(0, abs(pos - o[0]) - (t - o[1]));
				o[0] = pos;
				o[1] = t + 1;
			}
			t++;
		}
		
		printf("Case #%d: %d\n", nCase, t);
	}
}
