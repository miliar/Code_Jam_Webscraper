#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <functional> 

using namespace std;

#define SWAP(a,b)	{int tmp = a; a = b; b = tmp;}

void main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		char N[21];
		cin >> N;

		vector<int> digits;

		int len = 0;
		for (int i = 0; N[i]; i++)
		{
			len++;
		}
		for (int i = 0; i < len; i++)
		{
			char c[1];
			c[0] = N[len - i - 1];
			digits.push_back(atoi(c));
		}
		//sort(digits.begin(), digits.end());
		//int a = 0;

		bool easy = false;
		int max = 0;
		for (int i = 0; i < digits.size(); i++)
		{
			if (digits[i] >= max)
			{
				max = digits[i];
			}
			else
			{
				int minIdx = -1;
				int min = max;
				for (int j = 0; j < i; j++)
				{
					if (digits[j] <= min && digits[j] > digits[i])
					{
						minIdx = j;
						min = digits[j];
					}
				}
				
				SWAP(digits[i], digits[minIdx]);

				vector<int> tmpVec;
				for (int j = 0; j < i; j++)
					tmpVec.push_back(digits[j]);
				
				sort(tmpVec.begin(), tmpVec.end(), greater<int>());
				for (int j = 0; j < i; j++)
					digits[j] = tmpVec[j];
				easy = true;
				break;
			}
		}

		if (!easy)
		{
			digits.push_back(0);

			int max = 0;
			for (int i = 0; i < digits.size(); i++)
			{
				if (digits[i] >= max)
				{
					max = digits[i];
				}
				else
				{
					int minIdx = -1;
					int min = max;
					for (int j = 0; j < i; j++)
					{
						if (digits[j] <= min && digits[j] > digits[i])
						{
							minIdx = j;
							min = digits[j];
						}
					}

					SWAP(digits[i], digits[minIdx]);

					vector<int> tmpVec;
					for (int j = 0; j < i; j++)
						tmpVec.push_back(digits[j]);

					sort(tmpVec.begin(), tmpVec.end(), greater<int>());
					for (int j = 0; j < i; j++)
						digits[j] = tmpVec[j];
					break;
				}
			}
		}

		cerr << "Case #" << t + 1 << ": ";
		cout << "Case #" << t + 1 << ": ";
		for (int i = digits.size() - 1; i >= 0; i--)
		{
			cerr << digits[i];
			cout << digits[i];
		}
		cerr << endl;
		cout << endl;
	}
}