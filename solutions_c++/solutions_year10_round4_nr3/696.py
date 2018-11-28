#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ofstream fout("out");
	int C;
	cin >> C;
	for (int c = 1; c <= C; c++)
	{
		int R;
		cin >> R;
		int arr[101][101];
		memset(arr, 0, sizeof(arr));
		for (int i = 0; i < R; i++)
		{
			int X1, Y1, X2, Y2;
			cin >> X1 >> Y1 >> X2 >> Y2;
			for (int x = X1; x <= X2; x++)
				for (int y = Y1; y <= Y2; y++)
				{
					arr[x][y] = 1;	
				}
		}
		int narr[101][101];
		int sec;
		for (sec = 1; ; sec++)
		{
			for (int x = 1; x <= 100; x++)
				for (int y = 1; y <= 100; y++)
				{
					if (arr[x][y])
						narr[x][y] = arr[x - 1][y] || arr[x][y - 1];
					else
						narr[x][y] = arr[x - 1][y] && arr[x][y - 1];
				}
			bool l = false;
			for (int x = 1; x <= 100; x++)
				for (int y = 1; y <= 100; y++)
				{
					l |= (arr[x][y] = narr[x][y]);
				}
			if (!l)
				break;
		}
		cout << "Case #" << c << ": " << sec << endl;
		fout << "Case #" << c << ": " << sec << endl;
	}
}