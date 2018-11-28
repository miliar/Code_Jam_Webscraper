#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <list>

using namespace std;

struct groups
{
	int persons;
	int sumcost;
	int nextpos;
};

int main(void)
{
	int numofp;

	cin >> numofp;
	for(int ncount = 1; ncount <= numofp;ncount++)
	{
		vector<groups> vec_groups;

		int R,k,N;
		cin >> R >> k >> N;

		for(int i = 0; i < N; i++)
		{
			groups a;
			cin >> a.persons;

			vec_groups.push_back(a);
		}

		for(int i = 0; i < N; i++)
		{
			int pos = i;
			int sum = 0;
			while(true)
			{
				if(sum + vec_groups.at(pos).persons > k)
				{
					vec_groups.at(i).sumcost = sum;
					vec_groups.at(i).nextpos = pos;
					break;
				}

				sum += vec_groups.at(pos).persons;
				pos = ++pos % N;

				if(pos == i)
				{
					vec_groups.at(i).sumcost = sum;
					vec_groups.at(i).nextpos = pos;
					break;
				}
			}
		}

		int costs = 0;
		int pos = 0;
		for(int runcount = 0; runcount < R; runcount++)
		{
			costs += vec_groups.at(pos).sumcost;
			pos = vec_groups.at(pos).nextpos;
		}

		cout << "Case #" << ncount << ": " << costs << endl; 

	}

	return 0;
}