#include <iostream>
#include <string>
using namespace std;

int Value(char c)
{
	if(c == 'X') return  1;

	if(c == 'O') return -1;

	if(c == 'T') return  0;

	return 100;
}

int main()
{
	int T, N;
	string s[4];
	bool yet;
	int winner;

	cin >> T;
	N = T;

	while(T--)
	{
		for(int i = 0 ; i < 4 ; i++)
		{
			cin >> s[i];
		}


		int tmp;
		yet = true;
		winner = 0;

		for(int i = 0 ; i < 4 ; i++)
		{
			tmp = 0;
			for(int j = 0 ; j < 4 ; j++)
			{
				tmp += Value(s[i][j]);
			}

			if(tmp > 10) yet = false;

			if(tmp >= 3 && tmp < 9) winner =  1;
			if(tmp <= -3) winner = -1;
		}

		for(int i = 0 ; i < 4 ; i++)
		{
			tmp = 0;
			for(int j = 0 ; j < 4 ; j++)
			{
				tmp += Value(s[j][i]);
			}

			if(tmp > 10) yet = false;

			if(tmp >= 3 && tmp < 9) winner =  1;
			if(tmp <= -3) winner = -1;
		}

		tmp = 0;
		tmp = (Value(s[0][0]) + Value(s[1][1]) + Value(s[2][2]) + Value(s[3][3]));
		if(tmp >= 3 && tmp < 9) winner =  1;
		if(tmp <= -3) winner = -1;

		tmp = 0;
		tmp = (Value(s[0][3]) + Value(s[1][2]) + Value(s[2][1]) + Value(s[3][0]));
		if(tmp >= 3 && tmp < 9) winner =  1;
		if(tmp <= -3) winner = -1;

		if(winner)
		{
			if(winner ==  1) cout << "Case #" << N-T << ": X won" << endl;
			if(winner == -1) cout << "Case #" << N-T << ": O won" << endl;
		}
		else
		{
			if(yet == false)
			{
				cout << "Case #" << N-T << ": Game has not completed" << endl;
			}
			else
			{
				cout << "Case #" << N-T << ": Draw" << endl;
			}
		}
	}
}