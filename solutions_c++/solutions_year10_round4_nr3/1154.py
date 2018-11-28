#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	//freopen("C-large.in", "r", stdin);
	//freopen("C-large.out", "w", stdout);
	
	int t; cin >> t;
	for(int cnt = 0; cnt < t; cnt++)
	{
		int n = 0, r;
		bool arr[200][200] = {0};
		cin >> r;
		for(int g = 0; g < r; g++)
		{
			int x1, y1, x2, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			x1--;y1--;x2--;y2--;
			for(int i = y1; i <= y2; i++)
				for(int j = x1; j <= x2; j++)
				{
					if(!arr[i][j])
					{
						arr[i][j] = true;
						n++;
					}
				}
		}
		/*	for(int i = 0; i < 10; i++)
			{
				for(int j = 0; j < 10; j++)
					cout << arr[i][j];cout << endl;
				}*/
		int k = 0;
		while(n)
		{
			k++;
			for(int i = 100; i >= 0; i--)
				for(int j = 100; j >= 0; j--)
				{
					if(arr[i][j] && !(i == 0 ? false : arr[i - 1][j]) && !(j == 0 ? false : arr[i][j - 1]))
					{
						arr[i][j] = false;
						n--;
					}
					else if(!arr[i][j] && i > 0 && j > 0 && arr[i - 1][j] && arr[i][j - 1])
					{
						arr[i][j] = true;
						n++;
					}
				}
		}
		
		cout << "Case #" << cnt + 1 << ": " << k << endl;
	}
}
