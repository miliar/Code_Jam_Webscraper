#include <iostream>
#include <deque>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int i = 0; i < T; i++)
	{
		int H, W;
		cin >> H >> W;

		int** map = new int*[H];
		int** rain = new int*[H];
		int** fall = new int*[H];
		for(int j = 0; j < H; j++)
		{
			rain[j] = new int[W];
			map[j] = new int[W];
			fall[j] = new int[W];
			for(int k = 0; k < W; k++)
			{
				cin >> rain[j][k];
				map[j][k] = fall[j][k] = 0;
			}
		}
		
		for(int j = 0; j < H; j++)
			for(int k = 0; k < W; k++)
			{
				int minimum = rain[j][k];
				if(j > 0 && rain[j - 1][k] < minimum)
					fall[j][k] = 1, minimum = rain[j - 1][k];
				if(k > 0 && rain[j][k - 1] < minimum)
					fall[j][k] = 2, minimum = rain[j][k - 1];
				if(k < W - 1 && rain[j][k + 1] < minimum)
					fall[j][k] = 3, minimum = rain[j][k + 1];
				if(j < H - 1 && rain[j + 1][k] < minimum)
					fall[j][k] = 4, minimum = rain[j + 1][k];
			}
		
		int basin = 'a';
		for(int j = 0; j < H; j++)
			for(int k = 0; k < W; k++)
				if(map[j][k] == 0)
				{
					int a = j, b = k;
					while(fall[a][b])
						switch(fall[a][b])
						{
							case 1: a--; break;
							case 2: b--; break;
							case 3: b++; break;
							case 4: a++; break;
						}
					
					deque<int> height, width;
					height.push_back(a), width.push_back(b);
					while(!height.empty())
					{
						a = height.front(), b = width.front();
						map[a][b] = basin;
						if(a > 0 && fall[a - 1][b] == 4)
							height.push_back(a - 1), width.push_back(b);
						if(a < H - 1 && fall[a + 1][b] == 1)
							height.push_back(a + 1), width.push_back(b);
						if(b > 0 && fall[a][b - 1] == 3)
							height.push_back(a), width.push_back(b - 1);
						if(b < W - 1 && fall[a][b + 1] == 2)
							height.push_back(a), width.push_back(b + 1);
						height.pop_front(), width.pop_front();
					}
					basin++;
				}

		cout << "Case #" << i + 1 << ":" << endl;
		for(int j = 0; j < H; j++)
		{
			for(int k = 0; k < W; k++)
			{
				cout << (char)map[j][k];
				if(k < W - 1)
				     cout << " ";
            }
			cout << endl;
		}
		
		for(int j = 0; j < H; j++)
		{
			delete rain[j];
			delete map[j];
			delete fall[j];
		}
		delete rain;
		delete map;
		delete fall;
	}
	return 0;
}
