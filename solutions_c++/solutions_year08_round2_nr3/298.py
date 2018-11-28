#include <stdio.h>
#include <string.h>
#include <iostream>

#include <map>
#include <vector>
#include <string>

using namespace std;

void main()
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		int K;
		cin >> K;

		int n;
		cin >> n;

		vector<int> d;
		for(int i = 0; i < n; i++)
		{
			int d_i;
			cin >> d_i; 
			d.push_back(d_i);
		}

		vector<int> deck;
		deck.assign(K, 0);

		int zerocount = K;

		int pos = 0;

		for(int i = 1; i <= K; i++)
		{
			while(deck[pos] != 0)
			{
				pos = (pos + 1) % K;
			}

			int limit = i % zerocount == 0 ? zerocount : i % zerocount;
			for(int j = 1; j < limit; j++)
			{
				while(deck[pos] != 0)
				{
					pos = (pos + 1) % K;
				}
				pos = (pos + 1) % K;
			}
			while(deck[pos] != 0)
			{
				pos = (pos + 1) % K;
			}

			deck[pos] = i;
			
			pos = (pos + 1) % K;

			zerocount--;

			//cout << "[" << pos << "]";
			//for(int q = 0; q < K; q++)
			//{
			//	cout << " " << deck[q];
			//}
			//cout << endl;

			//if(i % 10000 == 0)
			//{
			//	cout << "[" << i << "]" << endl;
			//}

		}

		//for(int i = 0; i < K; i++)
		//{
		//	cout << " " << deck[i];
		//}
		//cout << endl;

		cout << "Case #" << t << ":";

		for(int i = 0; i < n; i++)
		{
			cout << " " << deck[d[i] - 1];
		}
		cout << endl;
	}
}

