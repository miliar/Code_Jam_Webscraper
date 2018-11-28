#include<fstream>
#include<iostream>
#include<queue>
using namespace std;

int H, W;
int input[110][110];
char cat[110][110];

int dir[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

bool isSink(int x, int y)
{
	for(int i = 0; i < 4; ++i)
	{
		int tx = x + dir[i][0];
		int ty = y + dir[i][1];
		if(tx < 0 || tx >= H || ty < 0 || ty >= W)
			continue;
		if(input[tx][ty] < input[x][y])
			return false;
	}
	return true;
}

void flowto(int tx, int ty, int &tox, int &toy)
{
	if(tx < 0 || tx >= H || ty < 0 || ty >= W)
	{
		tox = toy = -1;
		return;
	}
	int tempx, tempy;
	int cur = input[tx][ty];
	for(int i = 0; i < 4; ++i)
	{
		tempx = tx + dir[i][0];
		tempy = ty + dir[i][1];
		if(tempx < 0 || tempx >= H || tempy < 0 || tempy >= W)
		{
			continue;
		}
		if(input[tempx][tempy] < cur)
		{
			cur = input[tempx][tempy];
			tox = tempx;
			toy = tempy;
		}
	}

	if(cur == input[tx][ty])
	{
		tox = toy = -1;
		return;
	}
}

void bfs(int x, int y, int color)
{
	queue<int> q;
	
	while(!q.empty())
		q.pop();
	q.push(x);
	q.push(y);
	cat[x][y] = color;
	while(!q.empty())
	{
		int fx, fy;
		int tx, ty;
		fx = q.front();
		q.pop();
		fy = q.front();
		q.pop();
		int i;
		for(i = 0; i < 4; ++i)
		{
			tx = fx + dir[i][0];
			ty = fy + dir[i][1];
			if(tx < 0 || tx >= H || ty < 0 || ty >= W)
			{
				continue;
			}
			if(cat[tx][ty] != -1)
				continue;
			int tox, toy;
			flowto(tx, ty, tox, toy);
			if(tox == fx && toy == fy)
			{
				cat[tx][ty] = color;
				q.push(tx);
				q.push(ty);
			}
		}
	}
}

int main()
{
	int T;
	int x, y;
	int i, k;

	ifstream ifs("B-small-attempt0.in");
	ofstream ofs("B-small-attempt0.out");
	
	int caseNo;
	ifs >> T;
	for(caseNo = 1; caseNo <= T; ++caseNo)
	{
		ifs >> H >> W;
		for(x = 0; x < H; ++x)
			for(y = 0; y < W; ++y)
				ifs >> input[x][y];
		memset(cat, -1, sizeof(cat));
		
		int color = 0;
		for(x = 0; x < H; ++x)
		{
			for(y = 0; y < W; ++y)
			{
				if(cat[x][y] == -1 && isSink(x, y))
				{
					bfs(x, y, color);
					++color;
				}
			}
		}

		color = 'a' - 1;
		for(x = 0; x < H; ++x)
		{
			for(y = 0; y < W; ++y)
			{
				if( cat[x][y] >= 0 && cat[x][y] <= 30)
				{
					++color;
					int tmp = cat[x][y];
					for(i = 0; i < H; ++i)
					{
						for(k = 0; k < W; ++k)
						{
							if(cat[i][k] == tmp)
								cat[i][k] = color;
						}
					}
				}
			}
		}

		ofs << "Case #" << caseNo << ":" << endl;
		for(x = 0; x < H; ++x)
		{
			for(y = 0; y < W; ++y)
			{
				ofs << cat[x][y] << " ";
			}
			ofs << endl;
		}
	}

	return 0;
}