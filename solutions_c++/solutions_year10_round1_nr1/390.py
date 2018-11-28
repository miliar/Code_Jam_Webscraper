#include <iostream>
using namespace std;

char f[51][51];
int N, K;

int count()
{
	int ansr = false, ansb = false;
	
	// |
	if (1)
	for (int i = 0; i < N - K + 1; i++)
	{
		for (int j = 0; j < N; j++)
		{
			bool br = true, bb = true;
		
			for (int t = 0; t < K; t++)
			{
				br &= (f[i+t][j] == 'R');
				bb &= (f[i+t][j] == 'B');
			}
			ansr |= br, ansb |= bb;
		}
	}

	// -
	if(1)
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N - K + 1; j++)
		{
			bool br = true, bb = true;
		
			for (int t = 0; t < K; t++)
			{
				br &= (f[i][j+t] == 'R');
				bb &= (f[i][j+t] == 'B');
			}
			ansr |= br, ansb |= bb;
		}
	}
	// \ 
	if(1)
	for (int i = 0; i < N - K + 1; i++)
	{
		for (int j = 0; j < N - K + 1; j++)
		{
			bool br = true, bb = true;
		
			for (int t = 0; t < K; t++)
			{
				br &= (f[i+t][j+t] == 'R');
				bb &= (f[i+t][j+t] == 'B');
			}
			ansr |= br, ansb |= bb;
		}
	}
	// /
	if(1)
	for (int i = N; i >= K; i--)
	{
		for (int j = 0; j < N - K + 1; j++)
		{
			bool br = true, bb = true;
		
			for (int t = 0; t < K; t++)
			{
				br &= (f[i-t][j+t] == 'R');
				bb &= (f[i-t][j+t] == 'B');
			}
			ansr |= br, ansb |= bb;
		}
	}
	return (ansr << 1) + ansb;
}

int rotate()
{
	char tmp[51][51];
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			tmp[j][N-1-i] = f[i][j];
	for (int j = 0; j < N; j++)
	{
		int cur = N - 1;
		for (int i = N - 1; i >= 0; i--)
			if (tmp[i][j] != '.')
			{
				tmp[cur--][j] = tmp[i][j];
			}
		for (int i = cur; i >= 0; i--)
			tmp[i][j] = '.';
	}

	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			f[i][j] = tmp[i][j];
	return count();
}

int main()
{
	int T;
	cin >> T;
	for (int C = 1; C <= T; C++)
	{
		cin >> N >> K;
		memset(f, 0, sizeof(f));
		for (int i = 0; i < N; i++)
			cin >> f[i];
		int a = rotate();
		cout << "Case #" << C << ": ";
		switch(a)     
		{
		case 0:
			cout << "Neither";
			break;
		case 1:
			cout << "Blue";
			break;
		case 2:
			cout << "Red";
			break;
		case 3:
			cout << "Both";
			break;
		}
		cout << endl;
	}
}