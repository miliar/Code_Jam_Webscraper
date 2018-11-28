#include <iostream>
#include <fstream>
#include <vector>

using namespace std;



int k;
int d[1000][1000];


void Load()
{
	cin >> k;
	int i, j;
	int x, y;
	for (i = 0; i < 2*k-1; i++)
	{
		x = i;
		y = 0;
		if (x >= k)
		{
			x = k - 1;
			y = i - x; 
		}
		for (j = 0; j <= min(i, 2*k-2-i); j++)
		{
			cin >> d[x][y];
			x--;
			y++;
		}
	}
    
    /*
	for (i = 0; i < k; i++)
	{
		for (j = 0; j < k; j++)
			cerr << d[i][j];
		cerr << "\n";
	}*/
}



bool good1(int x, int y)
{
	int i, j;
	int i2, j2;
	for (i = 0; i < k; i++)
	{
		for (j = 0; j < k; j++)
		{
			i2 = x+y-j;
			j2 = x+y-i;
			if (i2 < 0 || j2 < 0 || i2 >= k || j2 >= k) continue;
			if (d[i][j] != d[i2][j2]) return false;
		}
	}
	for (i = 0; i < k; i++)
	{
		for (j = 0; j < k; j++)
		{
			i2 = x-y+j;
			j2 = y-x+i;
			if (i2 < 0 || j2 < 0 || i2 >= k || j2 >= k) continue;
			if (d[i][j] != d[i2][j2]) return false;
		}
	}
	return true;
}
bool good2(int x, int y)
{
	int i, j;
	int i2, j2;
	for (i = 0; i < k; i++)
	{
		for (j = 0; j < k; j++)
		{
			i2 = x+y-1-j;
			j2 = x+y-1-i;
			if (i2 < 0 || j2 < 0 || i2 >= k || j2 >= k) continue;
			if (d[i][j] != d[i2][j2]) return false;
		}
	}
	for (i = 0; i < k; i++)
	{
		for (j = 0; j < k; j++)
		{
			i2 = x-y+j;
			j2 = y-x+i;
			if (i2 < 0 || j2 < 0 || i2 >= k || j2 >= k) continue;
			if (d[i][j] != d[i2][j2]) return false;
		}
	}
	return true;
}



void Solve()
{

	int ans; 
	int cur;
	ans = 5*k;

	int x, y;
	//point inside the square
	for (x = -2*k; x <= 3*k; x++)
	{
		for (y = -2*k; y <= 3*k; y++)
		{
			if (good1(x,y))
			{
				cur = max(max(x,y),max(k-1-x, k-1-y));
				cur = 2*cur+1;
				if (cur < ans) ans = cur;
			}
		}
	}

	//point between the squares;
	for (x = -2*k; x <= 3*k; x++)
	{
		for (y = -2*k; y <= 3*k; y++)
		{
			if (good2(x,y))
			{
				cur = max(max(x,y),max(k-x, k-y));
				cur = 2*cur;
				if (cur < ans) ans = cur;
			}
		}
	}
	


	cout << ans*ans-k*k << "\n";
}

int main()
{
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ": ";
		Solve();
	}
	return 0;
}
