#include <iostream>
#include <queue>
using namespace std;

int ti[100][100];
int fl[100][100];
int ce[100][100];
int w, h;

struct point
{
	int x, y, t;

	bool operator<(const point& rhs) const
	{
		return t > rhs.t;
	}
};
priority_queue<point> q;

void Move(int x, int y, int dx, int dy, int startTime, int waterLevel)
{
	int nx = x+dx;
	int ny = y+dy;
	if (nx < 0 || nx >= w)
		return;
	if (ny < 0 || ny >= h)
		return;
	bool beforeStart = (startTime == -1);
	if (beforeStart)
		startTime = 0;
	// Constraints, see the task...
	int nt = startTime;
	int wl = waterLevel;
	if (fl[ny][nx] > ce[ny][nx] - 50) // Ceiling too close to floor
		return;
	if (fl[y][x] > ce[ny][nx] - 50) // Ceiling too close to floor
		return;
	if (fl[ny][nx] > ce[y][x] - 50) // Ceiling too close to floor
		return;
	if (wl > ce[ny][nx] - 50) // Water level too close to ceiling
	{
		int dt = wl - (ce[ny][nx] - 50);
		nt += dt;
		wl -= dt;
	}
	// Move
	point destP;
	destP.x = nx;
	destP.y = ny;
	if (wl - fl[y][x] < 20)
		destP.t = nt + 100; // 10 seconds
	else
		destP.t = nt + 10; // 1 second
	if (beforeStart && nt == 0)
		destP.t = -1; // Before the water starts to sink
	q.push(destP);
}

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		int waterLevel;
		cin >> waterLevel >> h >> w;
		for (int y = 0; y < h; ++y)
			for (int x = 0; x < w; ++x)
				ti[y][x] = -2;
		for (int y = 0; y < h; ++y)
			for (int x = 0; x < w; ++x)
				cin >> ce[y][x];
		for (int y = 0; y < h; ++y)
			for (int x = 0; x < w; ++x)
				cin >> fl[y][x];
		{
			point p;
			p.y = 0;
			p.x = 0;
			p.t = -1;
			q.push(p);
		}
		while (!q.empty())
		{
			point curP = q.top();
			q.pop();
			if (ti[curP.y][curP.x] != -2)
				continue; // Already visited
			ti[curP.y][curP.x] = (curP.t == -1 ? 0 : curP.t);
			if (curP.y == h-1 && curP.x == w-1)
			{
				cout << "Case #" << (t+1) << ": " << (ti[curP.y][curP.x] / 10.0) << endl;
				break;
			}
			int wl;
			if (curP.t == -1)
				wl = waterLevel;
			else
			{
				wl = waterLevel - curP.t;
				if (wl < 0)
					wl = 0;
			}
			Move(curP.x, curP.y, 0, 1, curP.t, wl);
			Move(curP.x, curP.y, 0, -1, curP.t, wl);
			Move(curP.x, curP.y, 1, 0, curP.t, wl);
			Move(curP.x, curP.y, -1, 0, curP.t, wl);
		}
		q.swap(priority_queue<point>());
	}
	return 0;
}
