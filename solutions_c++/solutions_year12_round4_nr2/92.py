#include <algorithm>
#include <stdio.h>
using namespace std;

#define LEFT 1
#define RIGHT 2
#define UP 4
#define DOWN 8

int n;
int w, l;

int head, tail;
int queue[100010][5];

struct _data {
	int x, index;

	inline bool operator < (const _data &rhs) const { 
		return x > rhs.x; }
};
_data r[1010];

double answer[1010][2];

inline void queue_insert(int x, int y, int dx, int dy, int state){
	queue[tail][0]=x;
	queue[tail][1] = y;
	queue[tail][2]=dx;
	queue[tail][3] = dy;
	queue[tail++][4] = state;
	if (tail==100000) perror("xxx");
}

inline bool inside(int r, int x, int y, int flag)
{
	if (x<0 || y<0) return false;
	int dx = (flag & LEFT) ? r : 2*r;
	int dy = (flag & DOWN) ? r : 2*r;
	int cx = dx-r, cy = dy-r;
	return cx <= x && cy <= y && 
		((flag & RIGHT) || dx <= x) && 
		((flag & UP) || dy <= y);
}

inline int min(int x, int y) { return x<y ? x:y;}
int main()
{
	int i, j;

	int t, tt=0;
	scanf("%d", &t);
	while (t--) {
		scanf("%d", &n);
		scanf("%d %d", &w, &l);
		for (i=0; i<n; i++) scanf("%d", &r[i].x);

		printf("Case #%d:", ++tt);
		head = tail = 0;
		queue_insert(w, l, 0, 0, 15);

		for (i=0; i<n; i++) r[i].index = i;

		sort(r, r+n);
		for (i=0; i<n; i++) {
			int x = queue[head][0], y = queue[head][1];
			int dx= queue[head][2], dy= queue[head][3];
			int flag = queue[head][4];
			head++;

			if (inside(r[i].x, x, y, flag)) {
				answer[r[i].index][0] = dx + (!(flag&LEFT) ? r[i].x : 0);
				answer[r[i].index][1] = dy + (!(flag&DOWN) ? r[i].x : 0);

				if (x<y) {
					if (!(flag & LEFT) && !(flag & DOWN)) {
						queue_insert(x-r[i].x*2, r[i].x*2, dx + r[i].x*2, dy, flag & (DOWN | RIGHT));
						queue_insert(x, y-r[i].x*2, dx, dy + r[i].x*2, flag & (LEFT | UP | RIGHT));
					}
					else if (!(flag & LEFT)) {
						queue_insert(x-r[i].x*2, r[i].x, dx + r[i].x*2, dy, flag & (DOWN | RIGHT));
						queue_insert(x, y-r[i].x, dx, dy + r[i].x, flag & (LEFT | UP | RIGHT));
					}
					else if (!(flag & !DOWN)) {
						queue_insert(x-r[i].x, r[i].x*2, dx + r[i].x, dy, flag & (DOWN | RIGHT));
						queue_insert(x, y-r[i].x*2, dx, dy + r[i].x*2, flag & (LEFT | UP | RIGHT));
					}
					else {
						queue_insert(x-r[i].x, r[i].x, dx + r[i].x, dy, flag & (DOWN | RIGHT));
						queue_insert(x, y-r[i].x, dx, dy + r[i].x, flag & (LEFT | UP | RIGHT));
					}
				}
				else {
					if (!(flag & LEFT) && !(flag & DOWN)) {
						queue_insert(r[i].x*2, y-r[i].x*2, dx, dy + r[i].x*2, flag & (LEFT | UP));
						queue_insert(x-r[i].x*2, y, dx + r[i].x*2, dy, flag & (DOWN | UP | RIGHT));
					}
					else if (!(flag & LEFT)) {
						queue_insert(r[i].x*2, y-r[i].x, dx, dy + r[i].x, flag & (LEFT | UP));
						queue_insert(x-r[i].x*2, y, dx + r[i].x*2, dy, flag & (DOWN | UP | RIGHT));
					}
					else if (!(flag & DOWN)) {
						queue_insert(r[i].x, y-r[i].x*2, dx, dy + r[i].x*2, flag & (LEFT | UP));
						queue_insert(x-r[i].x, y, dx + r[i].x, dy, flag & (DOWN | UP | RIGHT));
					}
					else {
						queue_insert(r[i].x, y-r[i].x, dx, dy + r[i].x, flag & (LEFT | UP));
						queue_insert(x-r[i].x, y, dx + r[i].x, dy, flag & (DOWN | UP | RIGHT));
					}
				}
			}
			else {
				queue_insert(x, y, dx, dy, flag);
				i--;
			}
		}

		for (i=0; i<n; i++) printf(" %.1lf %.1lf", answer[i][0], answer[i][1]);
		printf("\n");
	}

	return 0;
}
