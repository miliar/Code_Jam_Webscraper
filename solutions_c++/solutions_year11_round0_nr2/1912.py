#include <cstdio>
#include <cstring>

int T, C, D, N, rear, count[30];
char buf[200], input[200];
char conv[30][30];
bool op[30][30];

bool have_op() {
	if(rear == 0) return false;
//	printf("rear %c\n", input[rear-1]+'A');
	for(int i=0; i<30; i++) {
//		printf("vs %c : %d %d\n", i+'A', op[input[rear-1]][i], count[i]);
		if(op[input[rear-1]][i] && count[i])
			return true;
	}
	return false;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &T);
	for(int cc=1; cc<=T; cc++) {
		rear = 0;
		memset(conv, -1, sizeof(conv));
		memset(op, 0, sizeof(op));
		memset(count, 0, sizeof(count));
		scanf("%d", &C);
		for(int i=0; i<C; i++) {
			scanf("%s", buf);
			buf[0] -= 'A';
			buf[1] -= 'A';
			buf[2] -= 'A';
			conv[buf[0]][buf[1]] = buf[2];
			conv[buf[1]][buf[0]] = buf[2];	
		}
		scanf("%d", &D);
		for(int i=0; i<D; i++) {
			scanf("%s", buf);
			buf[0] -= 'A';
			buf[1] -= 'A';
			op[buf[0]][buf[1]] = op[buf[1]][buf[0]] = true;
		}
		scanf("%d%s", &N, buf);
		for(int i=0; i<N; i++) {
			int now = buf[i]-'A';
			count[now] ++;
			input[rear] = now; rear++;
			while(rear>1 && conv[input[rear-1]][input[rear-2]]!=-1) {
				int t = conv[input[rear-1]][input[rear-2]];
				count[input[rear-1]] --;
				count[input[rear-2]] --;
				count[t] ++;
				rear--;
				input[rear-1] = t;
			}
			if(have_op()) {
				memset(count, 0, sizeof(count));
				rear = 0;
			}
//			for(int j=0; j<rear; j++) putchar(input[j]+'A'); puts("");
		}
		printf("Case #%d: [", cc);
		for(int i=0; i<rear; i++) {
			if(i!=0) putchar(' ');
			putchar(input[i]+'A');
			if(i!=rear-1) putchar(',');
		}
		puts("]");
	}
}
