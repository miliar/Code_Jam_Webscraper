#include <iostream>
#include <cstring>

using namespace std;

const int MAX_N = 1004;

int k, x1, y1, x2, y2;
char a[MAX_N][MAX_N], b[MAX_N][MAX_N];
int res;

int fill(int cx, int cy)
{
	memset(b, ' ', sizeof(b));
	for (int i = x1; i <= x2; ++i)
		for (int j = y1; j <= y2; ++j)
			b[i][j] = a[i][j];
			
	int kk = k + abs(cx-3*k+1) + abs(cy-3*k+1);
	
	for (int di = 0; di < kk; ++di)
	{
		int si = cx-di;
		int bi = cx+di;
		for (int dj = 0; dj < kk; ++dj)
		{
			int sj = cy-dj;
			int bj = cy+dj;
			
			if (b[si][sj] != b[bi][sj])
			{
				if (b[si][sj] == ' ') 
					b[si][sj] = b[bi][sj];
				else
				if (b[bi][sj] == ' ')
					b[bi][sj] = b[si][sj];
				else return -1;
			}
			
			if (b[si][bj] != b[bi][bj])
			{
				if (b[si][bj] == ' ') 
					b[si][bj] = b[bi][bj];
				else
				if (b[bi][bj] == ' ')
					b[bi][bj] = b[si][bj];
				else return -1;
			}
		}
	}

	for (int dj = 0; dj < kk; ++dj)
	{
		int sj = cy-dj;
		int bj = cy+dj;
		for (int di = 0; di < kk; ++di)
		{
			int si = cx-di;
			int bi = cx+di;
			if (b[si][sj] != b[si][bj])
			{
				if (b[si][sj] == ' ') 
					b[si][sj] = b[si][bj];
				else
				if (b[si][bj] == ' ')
					b[si][bj] = b[si][sj];
				else return -1;
			}
			
			if (b[bi][sj] != b[bi][bj])
			{
				if (b[bi][sj] == ' ') 
					b[bi][sj] = b[bi][bj];
				else
				if (b[bi][bj] == ' ')
					b[bi][bj] = b[bi][sj];
				else return -1;
			}
		}
	}
	return kk*kk-k*k;
}

int main()
{
	int nTests;
	cin >> nTests;
	for (int run = 1; run <= nTests; ++run)
	{
		cin >> k;
		x1 = 2*k; y1 = 2*k;
		x2 = 4*k-2; y2 = 4*k-2;
		memset(a, ' ', sizeof(a));
		char s[MAX_N];
		cin.getline(s, MAX_N);
		
		for (int i = x1; i <= x2; ++i)
		{
			cin.getline(s, MAX_N);
			int si = 0;
			int sl = strlen(s);
			for (int j = y1; j <= y2; ++j)
			{
				if (si >= sl) a[i][j] = ' ';
				else a[i][j] = s[si++];
			}
		}
		/*
		for (int i = x1; i <= x2; ++i)
		{
			for (int j = y1; j <= y2; ++j)
				cout << a[i][j];
			cout << endl;
		}*/
		
		
		res = 1000000000;
		for (int cx = x1; cx <= x2; ++cx)
			for (int cy = y1; cy <= y2; ++cy)
			{
				int f = fill(cx, cy);
				if (f != -1 && res > f)
				{
					res = f;
					/*
					for (int i = 0; i < 6*k; ++i)
					{
						for (int j = 0; j < 6*k; ++j)
							cout << b[i][j];
						cout << endl;
					}*/
				}
			}
		
		cout << "Case #" << run << ": " << res << endl;
	}
	return 0;
}
