#include <iostream>
#include <vector>

using namespace std;

int add(int a,int b);


vector<int> nums;

int main()
{

	int T,N;
	int temp;
	int total=0;

	cin >> T;
	for ( int i = 0; i < T; i++)
	{
		total = 0;
		nums.clear();
		cin >> N;
		nums.reserve(N);
		for ( int j = 0; j < N; j++ )
		{
			cin >> temp;
			nums.push_back(temp);
			total = add(total,temp);
		}
		if ( total == 0 ){
			int lowest = nums[0],sum = 0;
			for ( int k = 0;k <nums.size();k++ )
			{
				if (nums[k] < lowest ){
					lowest = nums[k];
				}
				sum += nums[k];
			}
			cout << "Case #"<<i+1<<": "<<sum-lowest<<endl;
		}
		else{
			cout << "Case #"<<i+1<<": NO"<<endl;
		}

	}
}


int add(int a, int b)
{
	return a^b;
}
