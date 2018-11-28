#include <cstdio>
#include <fstream>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <iterator>

using namespace std;


int main()
{
	freopen("F:\\B-large.in", "r", stdin);
	freopen("F:\\result.txt", "w", stdout);
	int C;
	scanf("%d", &C);

	for(int l = 1; l <= C; l++)
	{
		int N, K, B, T;
		cin >> N >> K >> B >> T;
		vector<int> x;
		vector<int> v;
		vector<int> can;

		for(int i = 0; i < N; i++)
		{
			int temp;
			cin >> temp;
			x.push_back(temp);
		}
		for(int i = 0; i < N; i++)
		{
			int temp;
			cin >> temp;
			v.push_back(temp);
		}

		int count = 0;
		for(int i = 0; i < N; i++)
		{
			if(B - x[i] <= T * v[i])
			{
				can.push_back(1);
				count++;
			}
			else
			{
				can.push_back(0);
			}
		}

		if(count < K)
		{
			printf("Case #%d: IMPOSSIBLE\n", l);
		}
		else
		{
			int times = 0;
			int number = 0, pos = N - 1;
			while(number < K)
			{
				if(can[pos] == 1)
				{
					pos--;
					number++;
				}
				else
				{
					int i = pos;
					while(can[i] == 0)
					{
						i--;
					}
					can[pos] = 1;
					can[i] = 0;
					times = times + pos - i;
					number++;
					pos--;
				}
			}

			printf("Case #%d: %d\n", l, times);
		}	
	}

}