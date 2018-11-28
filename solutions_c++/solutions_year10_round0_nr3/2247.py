#include<iostream.h>
#include<math.h>


int main(int argc, char** argv)
{

	int T, R, k, N;
	int *groups;
	int income;
	int groupIndx, roundIndex, peopleInRC, tempGroupIndex, lastTempGroupIndex;

	cin >> T;
	
	for( int caseIndex = 0; caseIndex < T; caseIndex++ )
	{
		//cout << "Input R ";
		cin >> R;
		//cout << "Input K ";
		cin >> k;

		cin >> N;

		income = 0;
		groupIndx = 0;
		roundIndex = 0;

		groups = new int[N];

		for(int i = 0; i < N; i++)
		{
			cin >> groups[i];
		}

		while(roundIndex < R)
		{
			peopleInRC = 0;

			tempGroupIndex = groupIndx;
			lastTempGroupIndex = tempGroupIndex;

			while(peopleInRC <= k)
			{
				if((peopleInRC + groups[tempGroupIndex]) > k)
				{
					groupIndx = tempGroupIndex;
					break;
				}
				else
				{
					income += groups[tempGroupIndex];
					peopleInRC += groups[tempGroupIndex];

					if(tempGroupIndex == (N - 1))
					{
						lastTempGroupIndex = tempGroupIndex;
						tempGroupIndex = 0;
					}
					else 
					{
						lastTempGroupIndex = tempGroupIndex;
						tempGroupIndex++;
					}


					if(tempGroupIndex == groupIndx)
					{
						groupIndx = lastTempGroupIndex;
						break;
					}
				}

			}

			++roundIndex;
		}

		cout << "Case #" << (caseIndex + 1) << ": " << income << endl;

		delete [] groups;
	}
		return 0;
}
