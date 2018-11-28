#include <iostream>
using namespace std;
int n, k;
int map[200][200];

void fall(int i, int j) {
	if (i == n-1) return;
	if (map[i][j] == 0) return;
	if (map[i+1][j] == 0) {
		map[i+1][j] = map[i][j];
		map[i][j] = 0;
		fall(i+1,j);
	}
}

int check(int a, int b) {
	
	if (map[a][b] == 0) return 0;
	
	int res[3] = {0,0,0};
	for(size_t i = 0; i < k; ++i)
	{
		if (map[a+i][b] != map[a][b])
			break;
		if (i == k-1)
			res[map[a][b]] = 1;
	}
	for(size_t i = 0; i < k; ++i)
	{
		if (map[a][b+i] != map[a][b])
			break;
		if (i == k-1)
			res[map[a][b]] = 1;
	}
	for(size_t i = 0; i < k; ++i)
	{
		if (map[a+i][b+i] != map[a][b])
			break;
		if (i == k-1)
			res[map[a][b]] = 1;
	}
	for(size_t i = 0; i < k; ++i)
	{
		if (b-i < 0)
			break;
		if (map[a+i][b-i] != map[a][b])
			break;
		if (i == k-1)
			res[map[a][b]] = 1;
	}
	
	return res[1] + res[2]*2;
}

int main (int argc, char const *argv[])
{
	int t;
	cin >> t;
	for(size_t i = 0; i < t; ++i)
	{
		cout << "Case #" << i+1 << ": ";
		for(size_t i = 0; i < 200; ++i)
			for(size_t j = 0; j < 200; ++j)
				map[i][j] = 0;
		cin >> n >> k;
		getchar();
		for(int i = n-1; i >= 0; i--)
		{
			for(int j = 0; j < n; j++)
			{
				char c;
				cin >> c;
				switch (c) {
					case 'R': map[j][i] = 1; break;
					case 'B': map[j][i] = 2; break;
				}
			}
			getchar();
		}
		for(int i = n-2; i >= 0; i--)
			for(int j = 0; j < n; ++j)
				fall(i, j);

		// for(size_t i = 0; i < n; ++i)
		// {
		// 	for(size_t j = 0; j < n; ++j)
		// 	{
		// 		cout << map[i][j];
		// 	}
		// 	cout << endl;
		// }
		// cout << endl;
		
		//check horiton 
			bool R = false;
			bool B = false;
		for(size_t i = 0; i < n; ++i)
		{
			for(size_t j = 0; j < n; ++j)
			{
				int ret = check(i,j);
				if(ret == 1)
				{
					R = true;
				}
				if(ret == 2)
				{
					B = true;
				}
				if(ret == 3)
				{
					R = B = true;
				}
			}
		}
		
		if (R && B) cout << "Both" << endl;
		else if ((!R) && (!B)) cout << "Neither" << endl;
		else if (R) cout << "Red" << endl;
		else if (B) cout << "Blue" << endl;
		
	}
	return 0;
}