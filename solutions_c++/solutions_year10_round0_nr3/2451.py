#include <iostream>
#include <queue>
using namespace std;

void main()
{
	int case_num;
	cin >> case_num;
	int* runtimeperday = (int *) malloc (sizeof(int) * case_num);
	int* seatperrun = (int *) malloc (sizeof(int) * case_num);
	int* groupincase = (int *) malloc (sizeof(int) * case_num);
	//int ** group_num = (int **) malloc (sizeof(int *) * case_num);
	int* benefit = (int *) malloc (sizeof(int) * case_num);
	queue<int> q;
	int seatleft;
	int i, j, k, temp;
	
	for (i = 0; i < case_num; ++i)
	{
		cin >> runtimeperday[i] >> seatperrun[i] >> groupincase[i];
		for (j = 0; j < groupincase[i]; ++j)
		{
			cin >> temp;
			q.push(temp);
		}

		//process
		benefit[i] = 0;
		for (k = 0; k < runtimeperday[i]; ++k)
		{
			seatleft = seatperrun[i];
			for (j = 0; j < groupincase[i]; ++j)
			{
				temp = q.front();
				if (temp <= seatleft)	//play now
				{
					seatleft -= temp;
					q.pop();
					q.push(temp);
					benefit[i] += temp;
					//cout << temp << " ";
				}
				else break;	//still wait next round
			}
			//cout << endl;

			//empty the queue
			
		}
		while (!q.empty()) q.pop();
		//cout << "----------\n";
		//cout << "success in group" << i+1 << endl;
	}

	for (i = 0; i < case_num; ++i)
	{
		printf("Case #%d: %d\n", i+1, benefit[i]);

	}

	//cout << "success\n";
/*Case #1: 21
Case #2: 100
Case #3: 20
*/

	//for (i = 0; i < case_num; ++i)
	//	free (group_num[i]);
	//free (group_num);
	free (benefit);
	free (groupincase);
	free (seatperrun);
	free (runtimeperday);

}