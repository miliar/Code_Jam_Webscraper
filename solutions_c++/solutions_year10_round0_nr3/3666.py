#include <cstdlib>
#include <iostream>
#include <queue>
using namespace std;

int main()
{
	int t;
	long long int r, k, n;
	long long int elem, total, pre_total;
	cin >> t;
	for(int i=0; i<t; i++)
	{
		cin >> r >> k >> n;
		queue<long long int> fifo;
		queue<long long int> in_rc;
		for(int j=0; j<n; j++)
		{
			long long int g;
			cin >> g;
			fifo.push(g);
		}

		total = 0;
		elem = 0;
		for(long long int j=0; j<r; j++)
		{
			int count=0;
			if(j==0) count = -1;
			pre_total=0;
			while(elem+pre_total <= k && count<n)
			{
				//cout << elem << " ";
				pre_total += elem;
				if(!fifo.empty())
				{
					elem = fifo.front();
					fifo.pop();
					fifo.push(elem);
					count++;
				}
			}

			//cout << endl;
			total+=pre_total;
		}

		cout << "Case #" << i+1 << ": " << total << endl;
	}
	return 0;
}
