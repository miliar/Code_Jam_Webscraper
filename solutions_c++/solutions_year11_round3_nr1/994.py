#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>
#include <string>
#include <map>
#include <set>
#include <math.h>
using namespace std;

int arr[54][54];
int r, c;

void Print()
{
	for(int i = 0; i < r;i++)
	{
		for(int j = 0;  j < c; j++)
		{
			cout << arr[i][j];
		}
		cout << endl;
	}
	cout << endl;
}
int Solve()
{
	cin >> r >> c;
	for(int i = 0; i < r; i++)
	{
		for(int j = 0; j < c; j++)
		{
			char ch;
			cin >> ch;
			if(ch == '#')
				arr[i][j] = 1;
			else
				arr[i][j] = 2;

		}
	}
	bool glfl = false;
	for(int i = 0; i < r; i++)
	{
		for(int j = 0; j < c; j++)
		{
			bool fl = false;
			if(arr[i][j] == 1)
			{
				arr[i][j] = 3;
				int dx[3] = {0,1,1};
				int dy[3] = {1,0, 1};
				for(int k = 0; k < 3; k++)
				{
					int it = i + dx[k];
					int jt = j + dy[k];
					if(it >= 0 && it < r && jt >= 0 && jt < c && arr[it][jt] == 1)
					{
						arr[it][jt] = 3 + 1 + k;
					}
					else
					{
						fl = true;
						break;
					}
				}
				//Print();
				if(fl)
				{
					return 1;
				}
					
			}
		}
	}
	return 0;
}
int main()
{

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int i = 0; i < t; i++)
	{
		int p = Solve();
		if(p == 1)
		{
			cout << "Case #" << i + 1 << ":\n";
			cout << "Impossible\n";
		}
		else
		{
			cout << "Case #" << i + 1 << ":\n";
			for(int l = 0; l < r; l++)
			{
				for(int p = 0; p < c; p++)
				{
					if(arr[l][p] == 1)
					{
						cout << "Impossible\n";
					}
					else if(arr[l][p] == 2)
					{
						cout << ".";
					}
					else if(arr[l][p] == 3)
					{
						cout << "/";
					}
					else if(arr[l][p] == 4)
					{
						cout << "\\";
					}
					else if(arr[l][p] == 5)
					{
						cout << "\\";
					}
					else if(arr[l][p] == 6)
					{
						cout << "/";
					}
				}
				cout << endl;
			}
		}
	}
	return 0;

}