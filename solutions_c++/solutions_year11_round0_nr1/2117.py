#include <iostream>
#include <stdio.h>
#include <fstream>
#include <math.h>
using namespace std;

int main()
{
	int T;
	cin >> T;
	int N, i, j;
	char R[101];
	int P[101];
	int res[101];
	int delay, needTime, delayChange;
	int CPO, CPB;

	for (i=1; i<=T; i++)
	{
		cin >> N;
		for (j=0; j<N; j++)
		{
			cin >> R[j] >> P[j];
		}
		res[i] = 0;
		delay = 0;
		CPO = 1;
		CPB = 1;

		//1-ая кнопка
		res[i] = P[0];
		if (R[0]=='O') CPO=P[0];
		else CPB=P[0];
		delay = P[0];

		for (j=1; j<N; j++)
		{
			if (R[j]==R[j-1])
			{
				//следующее действие по той же кнопке
				
				delay = delay + abs(P[j]-P[j-1]) + 1;
				res[i] = res[i] + abs(P[j]-P[j-1]) + 1;
				
				if (R[j]=='O') CPO=P[j];
				else CPB=P[j];
			}
			else
			{
				//следующее дествие по другой кнопке
				if (R[j]=='O') 
					{
						needTime = abs(P[j]-CPO);
						CPO = P[j];
					}
				else 
					{
						needTime = abs(P[j]-CPB);
						CPB = P[j];
				}

				delayChange = delay - needTime;
				if (delayChange < 0)
				{
					//т.е. действие не укладывается
					delay = - delayChange;
					res[i] = res[i] - delayChange;
				}
				else
				{
					delay = 0;
				}

				delay = delay + 1;
				res[i] = res[i] + 1;

			}
		}
	}

	for (i=1; i<=T; i++)
	{
		cout << "Case #" << i <<": " << res[i] << endl;
	}

	return 0;
}