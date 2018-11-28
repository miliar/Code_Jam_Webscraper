#include <iostream>
#include <queue>
#include <deque>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		long long int R, k, N;
		cin >> R >> k >> N;
		deque<short> list;
		for (long long int j = 0; j < N; j++)
		{
			int temp;
			cin >> temp;
			list.push_back(temp);
		}	
		long long int sum = 0;
		for (long long int r = 0; r < R; r++)
		{
			long long int currentSum = 0;
			queue<short> car;
			while(!list.empty())
			{
				short front = list.front();
				if (front +  currentSum <= k)
				{
					car.push(front);
					currentSum += front;
					list.pop_front();
				} else 
				{					
					break;
				}
				
			}
			sum += currentSum;
			while (!car.empty())
			{
				short value = car.front();
				list.push_back(value);
				car.pop();
			}
		}
		cout << "Case #" << i+1 << ": " << sum << endl;
	}
}
