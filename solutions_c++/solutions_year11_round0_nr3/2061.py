#include <iostream>

using namespace std;


int main()
{
	int n;

	cin >> n;

	int m;
	int ele;
	int sum;
	int sumbit;

	for(int i = 0; i < n; ++i)
	{
		int small;

		cin >> m;

		for(int j = 0; j < m; ++j)
		{
			cin >> ele;
			if(j == 0) 
			{
				small = ele;
				sum = ele;
				sumbit = ele;
			}
			else
			{
				if(ele < small) small = ele;
				sum += ele;
				sumbit ^= ele;
			}

		}

		if(sumbit != 0) cout << "Case #" << i + 1 << ": NO" << endl;
		else
		{
			cout << "Case #" << i + 1 << ": " << sum - small << endl;
		}
	}

	return 0;
}


			
