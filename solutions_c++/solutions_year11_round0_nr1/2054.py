#include <iostream>

using namespace std;


int main()
{
	int n;

	cin >> n;

	for(int i = 0; i < n; ++i)
	{
		int m;
		int start1 = 1;
		int start2 = 1;
		int step1 = 0;
		int step2 = 0;
		bool lastIs1 = true;

		char which;
		int num;

		int stepnow;
		int time = 0;

		cin >> m;

		for(int j = 0; j < m; ++j)
		{
			cin >> which >> num;

			if(which == 'O')
			{
				if(lastIs1)
				{
					stepnow = num - start1 > 0 ? (num - start1) : (start1 - num);
					step1 = step1 + stepnow + 1;
					time = time + stepnow + 1;
					step2 = 0;
				}
				else
				{
					stepnow = num - start1 > 0 ? (num - start1) : (start1 - num);
					if(stepnow <= step2)
					{
						time += 1;
						step1 = 1;
						step2 = 0;
					}
					else
					{
						stepnow = stepnow - step2;
						time = time + stepnow + 1;
						step1 = stepnow + 1;
						step2 = 0;
					}
				}
				lastIs1 = true;
				start1 = num;
			}
			else
			{
				if(lastIs1)
				{
					stepnow = num - start2 > 0 ? (num - start2) : (start2 - num);
					if(stepnow <= step1)
					{
						time += 1;
						step2 = 1;
						step1 = 0;
					}
					else
					{
						stepnow = stepnow - step1;
						time = time + stepnow + 1;
						step2 = stepnow + 1;
						step1 = 0;
					}
				}
				else
				{
					stepnow = num - start2 > 0 ? (num - start2) : (start2 - num);
					step2 = step2 + stepnow + 1;
					time = time + stepnow + 1;
					step1 = 0;
				}
				lastIs1 = false;
				start2 = num;
			}
		}

		cout << "Case #" << i + 1 << ": " << time << endl;

	}

	return 0;
}

						






