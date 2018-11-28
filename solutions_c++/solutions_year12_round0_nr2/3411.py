#include <iostream>
#include <fstream>

#define FLAG_SURP 1
#define FLAG_INC 2
#define FLAG_SURP_AND_INC 3
#define FLAG_SURP_THEN_INC 4

int main(void)
{
	std::ifstream ifs("input.txt");
	std::ofstream ofs("output.txt");

	int testCase;
	ifs >> testCase;

	for(int i=0; i<testCase; i++)
	{
		///y => the number of triplet score that is greater than or equal to p
		int googlerNum, surpriNum, p, y;
		ifs >> googlerNum >> surpriNum >> p;
		y = 0;

		int *googlerScores = new int[googlerNum];
		int *Flag = new int[googlerNum];
		for(int j=0; j<googlerNum; j++)
		{
			ifs >> googlerScores[j];
			Flag[j] = 0;
		}

		// 1 Pass - check a surprising flag, count triplet score cases which always g.t. or equal to p.
		// surprisingFlag is true => score can contribute to increase surprising number only.
		// increaseFlag is true => score can contribute to increase y only.
		for(int j=0; j<googlerNum; j++)
		{
			//remainder == 0
			if(googlerScores[j] % 3 == 0 && googlerScores[j] / 3 >= p)
			{
				if(!(googlerScores[j] / 3 == 10 || googlerScores[j] / 3 == 0))
					Flag[j] = FLAG_SURP_AND_INC;
				Flag[j] = FLAG_INC;
			}

			else if(googlerScores[j] % 3 == 0 && (googlerScores[j] / 3) + 1 >= p && googlerScores[j] - 1 >= 0)
			{
				Flag[j] = FLAG_SURP_THEN_INC;
			}

			else if(googlerScores[j] % 3 == 0 && !(googlerScores[j] / 3 == 10 || googlerScores[j] / 3 == 0))
			{
				Flag[j] = FLAG_SURP;
			}

			//remainder == 1
			else if(googlerScores[j] % 3 == 1 && (googlerScores[j] / 3) + 1 >= p)
			{
				if(!((googlerScores[j] / 3) - 1 < 0))
					Flag[j] = FLAG_SURP_AND_INC;
				Flag[j] = FLAG_INC;
			}

			else if(googlerScores[j] % 3 == 1 && !(googlerScores[j] / 3 == 0))
			{
				Flag[j] = FLAG_SURP;
			}

			//remainder == 2
			else if(googlerScores[j] % 3 == 2 && (googlerScores[j] / 3 ) + 1 >= p)
			{
				if((googlerScores[j] / 3) + 2 <= 10)
					Flag[j] = FLAG_SURP_AND_INC;
				Flag[j] = FLAG_INC;
			}

			else if(googlerScores[j] % 3 == 2 && (googlerScores[j] / 3 ) + 2 >= p)
			{
				Flag[j] = FLAG_SURP_THEN_INC;
			}

			else if(googlerScores[j] % 3 == 2)
			{
				Flag[j] = FLAG_SURP;
			}
		}

		//2 Pass - Calculate y.
		int currentSurprising = 0;
		for(int j=0; j<googlerNum; j++)
		{
			if(currentSurprising == surpriNum)
				break;
			if(Flag[j] == FLAG_SURP_THEN_INC)
			{
				currentSurprising++;
				y++;
				Flag[j] = 0;
			}
		}

		for(int j=0; j<googlerNum; j++)
		{
			if(currentSurprising == surpriNum)
				break;
			if(Flag[j] == FLAG_SURP_AND_INC)
			{
				currentSurprising++;
				y++;
				Flag[j] = 0;
			}
		}

		for(int j=0; j<googlerNum; j++)
		{
			if(currentSurprising == surpriNum)
				break;
			if(Flag[j] == FLAG_SURP)
			{
				currentSurprising++;
				Flag[j] = 0;
			}
		}

		for(int j=0; j<googlerNum; j++)
		{
			if(Flag[j] == FLAG_INC || Flag[j] == FLAG_SURP_AND_INC)
				y++;
		}

		ofs << "Case #" << i+1 << ": " << y << std::endl;

		delete[] googlerScores;
		delete[] Flag;

	}



	return 0;
}