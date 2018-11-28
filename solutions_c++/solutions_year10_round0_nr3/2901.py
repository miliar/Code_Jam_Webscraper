#include<queue>
#include<iostream>
using namespace std;

#include<stdio.h>

int main()
{
	int r, k, n;

	int num_test = 0, group_size = 0;
	long long total = 0;
	int cur_load = 0, temp = 0;

	cin >> num_test;

	for(int t = 0; t < num_test; t++)
	{
		queue<int> q;
		total = cur_load = temp = group_size = 0;

		cin >> r >> k >> n;

		for(int j = 0; j < n; j++)
		{
			cin >> group_size;
			q.push(group_size);
		}

		while(r > 0)
		{
			cur_load = 0;

			int num_groups = 0;

			while(cur_load < k && num_groups < n)
			{
				temp = q.front();

				if(cur_load+temp <= k)
				{
					cur_load += temp;
					q.pop();
					q.push(temp);

					num_groups++;
				}
				else break;
			}

			total += cur_load;

			r --;
		}

		printf("Case #%d: %lld\n", t+1, total);
	}
}
