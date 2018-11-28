/*
 * dancing.cpp
 *
 *  Created on: Apr 13, 2012
 *      Author: labrus
 */

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int i = 0; i < T; i++)
	{
		int N;
		int S;
		int p;
		int count = 0;
		cin >> N;
		cin >> S;
		cin >> p;
		vector<int> scores(N);
		for(int j = 0; j < N; j++)
		{
			cin >> scores[j];
		}
		sort(scores.begin(), scores.end());
		for(int j = 0; j < N; j++)
		{
			int best = -1;
			if(S > 0 && scores[j] > 1) //assume surprising
			{
				for(int k = 2; k <= 4; k++)
				{
					if((scores[j]+k) % 3 == 0)
					{
						best = (scores[j]+k) / 3;
						break;
					}
				}
				if(best >= p)
				{
					count++;
					S--;
				}
			}
			else
			{
				for(int k = 0; k <= 2; k++)
				{
					if((scores[j]+k) % 3 == 0)
					{
						best = (scores[j]+k) / 3;
						break;
					}
				}
				if(best >= p)
				{
					count++;
				}
			}
		}
		cout << "Case #" << i+1 << ": " << count << endl;
	}
}




