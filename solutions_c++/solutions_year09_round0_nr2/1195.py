#include <iostream>
#include <string>

using namespace std;



int w, h;

int map[200][200];

const int dy[4] = {0,-1,1,0};
const int dx[4] = {-1,0,0,1};


int rt[20000];


void Load()
{
	cin >> h >> w;
	int i, j;
	for (i = 1; i <= h; i++)
	{
		for (j = 1; j <= w; j++)
		{
			cin >> map[i][j];
			rt[(i-1)* w + j] = (i-1)* w + j;
		}
	}
}


int Root(int i)
{
	if (rt[i] != i)	rt[i] = Root(rt[i]);
	return rt[i];
}



char mpc[20000];

void Solve()
{
	int i, j, k, ni, nj, p, q;
	int md, mh;
	for (i = 1; i <= h; i++)
	{
		for (j = 1; j <= w; j++)
		{

			//cerr << i << ' ' << j << "\n";
			mh = 100000;
			md = -1;
			for (k = 0; k < 4; k++)	
			{
				ni = i + dx[k]; nj = j + dy[k];
				if (ni < 1 || nj < 1 || ni > h || nj > w) continue;
				if (map[ni][nj] < mh)
				{
					mh = map[ni][nj];
					md = k;
				}
			}
			if (mh < map[i][j])
			{

				ni = i + dx[md]; nj = j + dy[md];
//				cerr << i << ' ' << j << " --> " << ni << " " << nj << "\n";
				rt[Root((i-1)* w + j)] = (ni-1) * w + nj;
			}
		}
	}
	memset(mpc, 0, sizeof(mpc));

	char lstc = 'a';
	for (i = 1; i <= h; i++)
	{
		for (j = 1; j <= w; j++)
		{
			p = Root((i-1)* w + j);
//			cerr << "root from " << i << ' ' << j << " = " << p << "\n";
			if (mpc[p] == (char)0)
			{
				mpc[p] = lstc++;
			}
			cout << mpc[p] << ' ';
		}
		cout << "\n";
	}
}

int main()
{
    int nt, tt;
    cin >> nt;
    for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ":\n";
		Solve();
	}
	return 0;
}
