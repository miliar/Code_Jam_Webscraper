#include <stdio.h>
#include <queue>
using namespace std;

unsigned int SWT[3][20][20];
unsigned int POS[20][20][4];
int M, N;

struct cross
{
	unsigned int time;
	int x, y, z;
	cross(unsigned int time, int x, int y, int z) : time(time), x(x), y(y), z(z) { }
	bool operator<(const cross &t) const
	{
		if (time > t.time) return true;
		if (time < t.time) return false;
		if (x > t.x) return true;
		if (x < t.x) return false;
		if (y > t.y) return true;
		if (y < t.y) return false;
		return z > t.z;
	}
};

bool canCrossNS(int y, int x, unsigned int &time)
{
	unsigned int s = SWT[0][y][x];
	unsigned int w = SWT[1][y][x];
	unsigned int t = SWT[2][y][x];
	t = t % (s + w);
	unsigned int b = (time + s + w - t) % (s + w);
	if (b < s) return true;
	time += s + w - b;
	return false;
}

bool canCrossWE(int y, int x, unsigned int &time)
{
	unsigned int s = SWT[0][y][x];
	unsigned int w = SWT[1][y][x];
	unsigned int t = SWT[2][y][x];
	t = t % (s + w);
	unsigned int b = (time + s + w - t) % (s + w);
	if (b >= s) return true;
	time += s - b;
	return false;
}

void move0(priority_queue<cross> &pq, const cross &c0)
{
	// up
	if (c0.y != 0 && POS[c0.y-1][c0.x][2] > c0.time + 2)
	{
		POS[c0.y-1][c0.x][2] = c0.time + 2;
		pq.push(cross(c0.time + 2, c0.x, c0.y - 1, 2));
	}
	// left
	if (c0.x != 0 && POS[c0.y][c0.x-1][1] > c0.time + 2)
	{
		POS[c0.y][c0.x-1][1] = c0.time + 2;
		pq.push(cross(c0.time + 2, c0.x - 1, c0.y, 1));
	}
	// cross NS
	if (POS[c0.y][c0.x][2] > c0.time + 1)
	{
		unsigned int t = c0.time;
		if (canCrossNS(c0.y, c0.x, t))
		{
			POS[c0.y][c0.x][2] = c0.time + 1;
			pq.push(cross(c0.time + 1, c0.x, c0.y, 2));
		}
		else
		{
			pq.push(cross(t, c0.x, c0.y, 0));
		}
	}
	// cross WE
	if (POS[c0.y][c0.x][1] > c0.time + 1)
	{
		unsigned int t = c0.time;
		if (canCrossWE(c0.y, c0.x, t))
		{
			POS[c0.y][c0.x][1] = c0.time + 1;
			pq.push(cross(c0.time + 1, c0.x, c0.y, 1));
		}
		else
		{
			pq.push(cross(t, c0.x, c0.y, 0));
		}
	}
}

void move1(priority_queue<cross> &pq, const cross &c0)
{
	// up
	if (c0.y != 0 && POS[c0.y-1][c0.x][3] > c0.time + 2)
	{
		POS[c0.y-1][c0.x][3] = c0.time + 2;
		pq.push(cross(c0.time + 2, c0.x, c0.y - 1, 3));
	}
	// right
	if (c0.x != M - 1 && POS[c0.y][c0.x+1][0] > c0.time + 2)
	{
		POS[c0.y][c0.x+1][0] = c0.time + 2;
		pq.push(cross(c0.time + 2, c0.x + 1, c0.y, 0));
	}
	// cross NS
	if (POS[c0.y][c0.x][3] > c0.time + 1)
	{
		unsigned int t = c0.time;
		if (canCrossNS(c0.y, c0.x, t))
		{
			POS[c0.y][c0.x][3] = c0.time + 1;
			pq.push(cross(c0.time + 1, c0.x, c0.y, 3));
		}
		else
		{
			pq.push(cross(t, c0.x, c0.y, 1));
		}
	}
	// cross WE
	if (POS[c0.y][c0.x][0] > c0.time + 1)
	{
		unsigned int t = c0.time;
		if (canCrossWE(c0.y, c0.x, t))
		{
			POS[c0.y][c0.x][0] = c0.time + 1;
			pq.push(cross(c0.time + 1, c0.x, c0.y, 0));
		}
		else
		{
			pq.push(cross(t, c0.x, c0.y, 1));
		}
	}
}

void move2(priority_queue<cross> &pq, const cross &c0)
{
	// down
	if (c0.y != N - 1 && POS[c0.y+1][c0.x][0] > c0.time + 2)
	{
		POS[c0.y+1][c0.x][0] = c0.time + 2;
		pq.push(cross(c0.time + 2, c0.x, c0.y + 1, 0));
	}
	// left
	if (c0.x != 0 && POS[c0.y][c0.x-1][3] > c0.time + 2)
	{
		POS[c0.y][c0.x-1][3] = c0.time + 2;
		pq.push(cross(c0.time + 2, c0.x - 1, c0.y, 3));
	}
	// cross NS
	if (POS[c0.y][c0.x][0] > c0.time + 1)
	{
		unsigned int t = c0.time;
		if (canCrossNS(c0.y, c0.x, t))
		{
			POS[c0.y][c0.x][0] = c0.time + 1;
			pq.push(cross(c0.time + 1, c0.x, c0.y, 0));
		}
		else
		{
			pq.push(cross(t, c0.x, c0.y, 2));
		}
	}
	// cross WE
	if (POS[c0.y][c0.x][3] > c0.time + 1)
	{
		unsigned int t = c0.time;
		if (canCrossWE(c0.y, c0.x, t))
		{
			POS[c0.y][c0.x][3] = c0.time + 1;
			pq.push(cross(c0.time + 1, c0.x, c0.y, 3));
		}
		else
		{
			pq.push(cross(t, c0.x, c0.y, 2));
		}
	}
}

void move3(priority_queue<cross> &pq, const cross &c0)
{
	// down
	if (c0.y != N-1 && POS[c0.y+1][c0.x][1] > c0.time + 2)
	{
		POS[c0.y+1][c0.x][1] = c0.time + 2;
		pq.push(cross(c0.time + 2, c0.x, c0.y + 1, 1));
	}
	// right
	if (c0.x != M-1 && POS[c0.y][c0.x+1][2] > c0.time + 2)
	{
		POS[c0.y][c0.x+1][2] = c0.time + 2;
		pq.push(cross(c0.time + 2, c0.x + 1, c0.y, 2));
	}
	// cross NS
	if (POS[c0.y][c0.x][1] > c0.time + 1)
	{
		unsigned int t = c0.time;
		if (canCrossNS(c0.y, c0.x, t))
		{
			POS[c0.y][c0.x][1] = c0.time + 1;
			pq.push(cross(c0.time + 1, c0.x, c0.y, 1));
		}
		else
		{
			pq.push(cross(t, c0.x, c0.y, 3));
		}
	}
	// cross WE
	if (POS[c0.y][c0.x][2] > c0.time + 1)
	{
		unsigned int t = c0.time;
		if (canCrossWE(c0.y, c0.x, t))
		{
			POS[c0.y][c0.x][2] = c0.time + 1;
			pq.push(cross(c0.time + 1, c0.x, c0.y, 2));
		}
		else
		{
			pq.push(cross(t, c0.x, c0.y, 3));
		}
	}
}

int main()
{
	int C;
	scanf("%d", &C);
	for (int n = 1; n <= C; n++)
	{
		scanf("%d%d", &N, &M);
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				scanf("%d%d%d", &SWT[0][i][j], &SWT[1][i][j], &SWT[2][i][j]);
			}
		}
		memset(POS, -1, sizeof(POS));
		POS[N-1][0][2] = 0;
		priority_queue<cross> pq;
		pq.push(cross(0, 0, N-1, 2));
		while (!pq.empty())
		{
			cross c0 = pq.top();
			pq.pop();
			switch (c0.z)
			{
			case 0:
				move0(pq, c0);
				break;
			case 1:
				move1(pq, c0);
				break;
			case 2:
				move2(pq, c0);
				break;
			case 3:
				move3(pq, c0);
				break;
			}
		}
		printf("Case #%d: %d\n", n, POS[0][M-1][1]);
	}
	return 0;
}