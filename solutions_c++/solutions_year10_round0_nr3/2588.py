#include <iostream>
#include <queue>


using namespace std;

int main()
{
	int j;

	cin >> j;

	for(int i=0; i<j; i++)
	{

		int r, k, n;

		cin >> r >> k >> n;

		queue<int> group, sitting;    

		for(int x=0; x<n; x++)
		{
			int people;
			cin >> people;
			group.push(people);
		}

		int money=0, seat = k;

		while(r!=0)
		{
			if(group.empty() || seat < int(group.front()))
			{
				r--;
				seat=k;
				for(int y=0; y< int(sitting.size());)
				{
					group.push(sitting.front());
					sitting.pop();
				}
			}
			else
			{
				money+=group.front();
				seat -= group.front();
				sitting.push(group.front());
				group.pop();
			}

		}

		for(int z=0; z< int(group.size());)
			group.pop();

		for(int z=0; z< int(sitting.size());)
			sitting.pop();



		cout << "Case #" << i+1 << ": " << money << "\n";


	}

	return 0;
}