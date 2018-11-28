#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
	int aScore, casos, googlers, i, j, k, max, promedio, resto, sTriplets, topGooglers, totalScore;
	int score[3];
	
	cin >> casos;
	for (i = 0; i < casos; i++)
	{
		topGooglers = 0;
		cin >> googlers >> sTriplets >> aScore;
		for (j = 0; j < googlers; j++)
		{
			cin >> totalScore;
			promedio = floor(totalScore / 3.0f);
			resto = totalScore % 3;
			score[0] = promedio;
			score[1] = promedio;
			score[2] = promedio;
			for (k = 0; k < resto; k++) score[k]++;
			//min = *min_element(score,score+3);
			max = *max_element(score,score+3);
			if (max >= aScore)
			{
				topGooglers++;
			}
			else if ((totalScore > 0) && ((aScore - max) == 1) && ((score[1] == max) || (score[2] == max)) && (sTriplets > 0))
			{
				sTriplets--;
				topGooglers++;
			}
		}
		cout << "Case #" << i+1 << ": " << topGooglers << endl;
	}
	
	return 0;
}

