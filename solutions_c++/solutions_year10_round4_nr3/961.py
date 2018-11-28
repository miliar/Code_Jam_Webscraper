#include <iostream>
#include <vector>

using namespace std;

int arr[200][200], tmp[200][200];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int tc = 0; tc < t; tc++)
	{
		memset(arr, 0, sizeof(arr));
		int n;
		cin >> n;
		for(int i = 0; i < n; i++)
		{
			int x1, x2, y1, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			//x1--;
			//x2--;
			//y1--;
			//y2--;
			for(int x = x1; x <= x2; x++)
				for(int y = y1; y <= y2; y++)
					arr[x][y] = 1;
		}
		bool ok = true;
		int cnt = 0;
		while(ok)
		{
			cnt++;
			memset(tmp, 0, sizeof(tmp));
			ok = false;
			for(int i = 1; i <= 100; i++)
				for(int j = 1; j <= 100; j++)
				{
					if(arr[i][j] && (arr[i - 1][j] || arr[i][j - 1]))
						tmp[i][j] = 1;
					if(arr[i - 1][j] && arr[i][j - 1])
						tmp[i][j] = 1;
					if(tmp[i][j] == 1)
						ok = true;
				}
			memcpy(arr, tmp, sizeof(arr));
		}
		printf("Case #%d: %d\n", tc + 1, cnt);
	}
	return 0;
}