#include <iostream>
#include <vector>
#include <map>

using namespace std;

int T, M, N;

vector <vector <int> > a;
map <int, int> mp;

void ReadData()
{
	a.clear();
	cin >> M >> N;
	a.resize(M);
	char c;
	int t, tmp;

	for(int i = 0; i < M; i++)
	{
		for(int j = 0; j < N / 4; j++)
		{
			cin >> c;
			
			if( c >= '0' && c <= '9' )
				t = c - '0';
			else
				t = c - 'A' + 10;

			tmp = t / 8;

			a[i].push_back(tmp+1);

			t %= 8;
			tmp = t / 4;

			a[i].push_back(tmp+1);

			t %= 4;
			tmp = t / 2;

			a[i].push_back(tmp+1);

			t %= 2;
			tmp = t;

			a[i].push_back(tmp+1);
		}
	}
}

bool Check(int x, int y, int n)
{
	if( n == 1 )
	{
		return a[x][y] < 3;
	}

	if( a[x][y] == 3 )
		return false;

	for(int i = 1; i < n; i++)
	{
		if( a[x][y+i] * a[x][y+i-1] != 2 )
			return false;
	}	

	for(int i = 1; i < n; i++)
	{
		if( a[x+i][y] * a[x+i-1][y] != 2 )
			return false;

		for(int j = 1; j < n; j++)
		{
			if( a[x+i][y+j] * a[x+i][y+j-1] != 2 )
				return false;
		}
	}

	return true;
}

void Fill(int x, int y, int n)
{
	for(int i = 0; i < n; i++)
	{
		for(int j = 0; j < n; j++)
		{
			a[x+i][y+j] = 3;
		}
	}
}


void Func()
{
	int t = min(N, M);

	for(int k = t; k >= 1; k--)
	{
		for(int i = 0; i <= M - k; i++)
		{
			for(int j = 0; j <= N - k; j++)
			{
				if( Check(i, j, k) )
				{
					mp[k]++;
					Fill(i, j, k);
				}
			}
		}
	}	
}


int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);

	cin >> T;

	for(int i = 0; i < T; i++)
	{
		mp.clear();
		ReadData();
		Func();
		cout << "Case #" << i + 1 << ": " << mp.size() << endl;

		for(map <int, int>::reverse_iterator it = mp.rbegin(); it != mp.rend(); it++)
		{
			cout << it->first << " " << it->second << endl;
		}
	}


	return 0;
}