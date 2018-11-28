#include <fstream>
#include <string>

using namespace std;

char winningRow (string s)
{
	if (s.find('X') == -1)
		return 'O';
	if (s.find('O') == -1)
		return 'X';
	return 'A';
}

int main(void)
{

	ifstream input("A-large.in");
	ofstream output("output.out");
	string len;
	getline(input,len);
	int numCases = atoi(len.c_str());
	char arr[4][4];
	string s1;
	bool winnerDone;
	bool complete = true;
	for (int i = 0; i < numCases; i++)
	{
		complete = true;
		if (i != 0)
		{
			getline(input,s1);
			while (s1 != "")
				getline(input,s1);
		}
		winnerDone = false;
		for (int j = 0; j < 4 ; j++)
		{
			getline(input,s1);
			if (s1.find('.') != -1)
				complete = false;
			else 
			{
				char winner = winningRow(s1);
				if (winner != 'A')
				{
					output << "Case #" << i+1 << ": " << winner << " won\n";
					winnerDone = true;
					break;
				}
			}

			for (int k = 0 ; k < 4 ; k++)
				arr[j][k] = s1[k];
		}
		if (winnerDone)
			continue;
		string s3= "";
		string s4= "";
		for (int k = 0 ; k < 4 ; k++)
		{
			s3 += arr[k][k];
			s4 += arr[k][3-k];
			string s2 = "";
			s2 += arr[0][k];
			s2 += arr[1][k];
			s2 += arr[2][k];
			s2 += arr[3][k];
			if (s2.find('.') != -1)
				continue;
			char winner = winningRow(s2);
			if (winner != 'A')
			{
				output << "Case #" << i+1 << ": " << winner << " won\n";
				winnerDone = true;
				break;
			}
		}
		if (winnerDone)
			continue;
		char winner;
		if (s3.find('.')==-1)
		{
			winner = winningRow(s3);
			if (winner != 'A')
			{
				output <<"Case #" << i+1 << ": " << winner << " won\n";
				continue;
			}
		}
		if (s4.find('.')== -1)
		{
			winner = winningRow(s4);
			if (winner != 'A')
			{
				output << "Case #" << i+1 << ": " << winner << " won\n";
				continue;
			}
		}
		if (complete == false)
		{
			output << "Case #" << i+1 << ": Game has not completed\n";
		}
		else 
			output << "Case #" << i+1 << ": Draw\n";

	}
	input.close();
	output.close();
	return 0;
}
