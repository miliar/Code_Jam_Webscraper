#include <iostream>

using namespace std;

int main()
{
	int testcase;
	
	cin >> testcase;
	int* result = new int[testcase];

	int i = 0;

	while (i < testcase)
	{
		int num, sur, p;
		int count = 0;

		cin >> num >> sur >> p;

		int* score = new int[num];
		
		for (int j = 0; j < num; j++)
		{
			int counted = 0;
			bool surp = false;

			cin >> score[j];

			int arr[3] = {0};

			int median = score[j] / 3;
			
			arr[0] = arr[1] = arr[2] = median;

			if (median < p)
				surp = true;
			else
			{
				count++;
				counted = 1;
			}

			int rem = score[j] % 3;

			
			if (!counted && (rem == 0) && ((arr[2]+1) >= p) && sur )
			{
				if (arr[0] >= 1)
				{
					arr[0]--;
					arr[2]++;
					sur--;
				}
			}
			

			while(rem)
			{
				if (surp)
				{
					if ((rem == 2) && ((arr[rem]+2) >= p) && sur)
					{
						arr[rem] += 2;
						rem -= 2;
						sur--;
					}
					else
					{
						arr[rem]++;
						rem--;
					}


				}
				else
				{
					arr[rem]++;
					rem--;
				}
			}

			if (((arr[1] >= p) ||  (arr[2] >= p)) && !counted)
				count++;

		}

		delete[] score;
		
		result[i] = count;
		
		i++;
	}

	for (int t = 0; t < testcase; t++)
	{
		cout << "Case #" << t+1 << ": " << result[t] << endl;
	}

	delete[] result;
}