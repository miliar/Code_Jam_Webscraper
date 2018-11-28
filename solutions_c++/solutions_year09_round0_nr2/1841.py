#include <iostream>
#include <queue>
using namespace std;

const int MAX = 110;
const int MINT = 0x7fffffff;

typedef struct _coord {
	int x,y;
	_coord(int xx, int yy){x=xx;y=yy;}
}coord;

int map[MAX][MAX];
char mm[MAX][MAX];
int h,w;
int n;
queue <coord> q;
char fillc;
int fillnum;

char getdir(int hn, int hw, int he, int hs)
{
	char dir = 's';
	int minh = hs;
	if (minh >= he)
	{
		dir = 'e';
		minh = he;
	}
	if (minh >= hw)
	{
		dir = 'w';
		minh = hw;
	}
	if (minh >= hn)
	{
		dir = 'n';
		minh = hn;
	}

	return dir;
}

inline int min(int a, int b, int c, int d)
{
	int ret = a;
	ret = (ret>b) ? b : ret;
	ret = (ret>c) ? c : ret;
	ret = (ret>d) ? d : ret;
	return ret;
}

void flood(int x, int y)
{
	if (mm[x][y]) // already filled
	{
		char tmpfill = mm[x][y];
		fillnum += q.size();
		while (q.size())
		{
			coord tmpcoord = q.front();
			q.pop();
			mm[tmpcoord.x][tmpcoord.y] = tmpfill;
		}
		return;
	}

	int hw=MINT,he=MINT,hn=MINT,hs=MINT;
	if (x > 1)
		hn = map[x-1][y];
	if (x < h)
		hs = map[x+1][y];
	if (y > 1)
		hw = map[x][y-1];
	if (y < w)
		he = map[x][y+1];

	if (map[x][y] <= min(hn, hs, hw, he)) // lowest point
	{
		char tmpfill = fillc;
		fillnum += q.size();
		++fillnum;
		while (q.size())
		{
			coord tmpcoord = q.front();
			q.pop();
			mm[tmpcoord.x][tmpcoord.y] = tmpfill;
		}
		mm[x][y] = tmpfill;
		++fillc;
		return;
	}

	char dir = getdir(hn,hw,he,hs);
	if (dir == 'n')
	{
		coord tmpcoord(x,y);
		q.push(tmpcoord);
		flood(x-1, y);
	}
	else if (dir == 's')
	{
		coord tmpcoord(x,y);
		q.push(tmpcoord);
		flood(x+1,y);
	}
	else if (dir == 'w')
	{
		coord tmpcoord(x,y);
		q.push(tmpcoord);
		flood(x,y-1);
	}
	else if (dir == 'e')
	{
		coord tmpcoord(x,y);
		q.push(tmpcoord);
		flood(x,y+1);
	}
}

int main()
{
	cin >> n;

	for (int xx=1; xx<=n; ++xx)
	{
		fillc='a';
		fillnum = 0;

		memset(mm, 0, sizeof(mm));
		cin >> h >> w;
		for (int i=1; i<=h; ++i)
			for (int j=1; j<=w; ++j)
				cin >> map[i][j];

		//flood(1, 1);
		while (fillnum < h*w)
		{
			//get highest
			int x,y,maxhei=-1;
			for (int i=1; i<=h; ++i)
			{
				bool f = false;
				for (int j=1; j<=w; ++j)
				{
					//if ((map[i][j] > maxhei) && (!mm[i][j]))
					if (!mm[i][j])
					{
						//maxhei = map[i][j];
						x = i;
						y = j;
						f = true;
						break;
					}
				}
				if (f)
					break;
			}

			flood(x, y);
		}

		// print answer
		cout << "Case #" << xx << ":" << endl;
		for (int i=1; i<=h; ++i)
		{
			for (int j=1; j<w; ++j)
				cout << mm[i][j] << " ";
			cout << mm[i][w] << endl;
		}
	}

	//system("pause");
	return 0;
}