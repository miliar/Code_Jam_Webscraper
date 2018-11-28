#include <cstdio>
#include <queue>
#include <memory.h>

using namespace std;

int R, C, F;

char data[51][51];
int row[51];

int did[11][7][(1 << 6)][(1 << 6)];

int ans;

struct state_s
{
	state_s() {}
	state_s(int _r, int _c, int _cur_row, int _next_row) : r(_r), c(_c), cur_row(_cur_row), next_row(_next_row) {}
	int r;
	int c;
	int cur_row;
	int next_row;
};

int fall_down(int &r, int &c, int cur_row, int next_row)
{
	int ret = 0;
	for (;;ret++)
	{
		if (ret == 0)
		{
			if (r == R - 1 || ((next_row >> c) & 1))
				break;
		}
		else
		{
			if (r == R - 1 || data[r + 1][c] == '#')
				break;
		}
		r++;
	}
	return ret;
}

void process()
{
	memset(did, 0, sizeof(did));
	queue< state_s> que;

	que.push(state_s(0, 0, row[0], row[1]));
	did[0][0][row[0]][row[1]] = true;

	int cost = 0;
	for (;;cost++)
	{ 
		queue< state_s> nque;
		if (que.empty())
			return;
		for (;!que.empty();)
		{
			state_s now = que.front();
			que.pop();

			if (now.r == R - 1)
			{
				fprintf(stderr, "%d %d %d %d\n", now.r, now.c, now.cur_row, now.next_row);
				ans = cost;
				return;
			}

			// move to left/right
			
			int dc;
			for (dc = -1;dc <= 1;dc++)
			{
				if (!dc)
					continue;
				int nr = now.r;
				int nc = now.c + dc;

				if (nc < 0 || nc >= C)
					continue;
				if ((now.cur_row >> nc) & 1) // blocked here
					continue;


				int fd = fall_down(nr, nc, now.cur_row, now.next_row);

				if (fd > F)
					continue;

				state_s next;
				if (!fd)
				{
					next.cur_row = now.cur_row;
					next.next_row = now.next_row;
				}
				else if (fd == 1) // single row
				{
					next.cur_row = now.next_row;
					next.next_row = row[nr + 1];
				}
				else
				{
					next.cur_row = row[nr];
					next.next_row = row[nr + 1];
				}
				next.r = nr;
				next.c = nc;

				if (did[next.r][next.c][next.cur_row][next.next_row])
					continue;
				did[next.r][next.c][next.cur_row][next.next_row] = true;

				if (next.r == 3 && next.c == 0 && next.cur_row == 2 && next.next_row == 0)
					fprintf(stderr, "> %d %d %d %d\n", now.r, now.c, now.cur_row, now.next_row);
				que.push(next);
			}

			// dig ld/rd
			for (dc = -1;dc <= 1;dc++)
			{
				if (!dc)
					continue;
				// not R - 1
				int nr = now.r;
				int nc = now.c + dc;

				if (nc < 0 || nc >= C)
					continue;
				if ((now.cur_row >> nc) & 1) // blocked here
					continue;
				if (!((now.next_row >> nc) & 1)) // empty here
					continue;

				state_s next;
				next.r = nr;
				next.c = now.c;
				next.cur_row = now.cur_row;
				next.next_row = now.next_row - (1 << nc);

				if (did[next.r][next.c][next.cur_row][next.next_row])
					continue;
				did[next.r][next.c][next.cur_row][next.next_row] = true;

				nque.push(next);
			}
		}
		que = nque;
	}
}

int main()
{
	int t, ti;
	scanf("%d", &t);
	for (ti = 1;ti <= t;ti++)
	{
		scanf("%d %d %d", &R, &C, &F);
		int i, j;
		for (i = 0;i < R;i++)
		{
			scanf("%s", data[i]);
			int v = 0;
			for (j = 0;j < C;j++)
				v += ((data[i][j] == '#') << j);
			row[i] = v;
		}

		ans = 0x7F7F7F7F;
		process();


		printf("Case #%d: ", ti);
		if (ans == 0x7F7F7F7F)
			printf("No\n");
		else
			printf("Yes %d\n", ans);

	}
}
