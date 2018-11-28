#include <iostream>
#include <vector>

using namespace std;

bool check(vector<int> nums)
{
	int sum = 0;
	for(int i = 0; i < nums.size(); i++)
	{
		sum = sum ^ nums[i];
	}

	return (sum == 0);
}

int main()
{
	vector<int> nums;
	int t, n, temp, sum, lowest;
	cin >> t;
	for(int i = 0; i < t; i++)
	{
		cin >> n;
		nums.clear();
		for(int j = 0; j < n; j++)
		{
			cin >> temp;
			nums.push_back(temp);
		}

		cout << "Case #" << i+1 << ": ";

		if(check(nums))
		{
			lowest = -1;
			sum = 0;
			for(int j = 0; j < nums.size(); j++)
			{
				sum += nums[j];
				if(lowest == -1 || lowest > nums[j])
				{
					lowest = nums[j];
				}
			}
			cout << sum - lowest << endl;
		}
		else
		{
			cout << "NO" << endl;
		}
	}
}
