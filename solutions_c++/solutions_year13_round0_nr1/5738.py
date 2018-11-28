#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream infile;
	ofstream outfile;
	infile.open("d:\\testcases.txt");
	outfile.open("D:\\result.txt");

	int testcases = 0;
	char tictactoe [4];
	char status[6];
	char won;
	bool skip = false;
	char rowchar;

	infile>>testcases;
	
	for (int i=0;i<testcases;i++)
	{
		won = 'N';
		skip = false;
		memset (tictactoe, 0, sizeof (char)*4);
		memset (status, 0, sizeof (char)*6);

		for (int j=0;j<4;j++)
		{
			infile>>tictactoe[0];
			infile>>tictactoe[1];
			infile>>tictactoe[2];
			infile>>tictactoe[3];
			if (skip == false)
			{
				if (j ==0)
				{
					if ((tictactoe[0] == tictactoe[1] && tictactoe[1] == tictactoe[2] && tictactoe[2] ==tictactoe[3]) ||
						(tictactoe[0] == tictactoe[1] && tictactoe[1] == tictactoe[2] && tictactoe[3] == 'T') ||
						(tictactoe[0] == tictactoe[1] && tictactoe[1] == tictactoe[3] && tictactoe[2] == 'T') ||
						(tictactoe[0] == tictactoe[2] && tictactoe[2] == tictactoe[3] && tictactoe[1] == 'T')) {
						won = tictactoe[0];
						skip = true;
					}
					else if	(tictactoe[3] == tictactoe[1] && tictactoe[1] == tictactoe[2] && tictactoe[0] == 'T')
					{
						won = tictactoe[3];
						skip = true;
					} else {
						status[0] = tictactoe[0];
						//status[4] = tictactoe[0];
						status[4] = tictactoe[0];
				
						status[1] = tictactoe[1];
						//status[5] = tictactoe[1];
				
						status[2] = tictactoe[2];
						//status[6] = tictactoe[2];
				
						status[3] = tictactoe[3];
						//status[7] = tictactoe[3];
						status[5] = tictactoe[3];
					}

				}
				else {

					if ((tictactoe[0] == tictactoe[1] && tictactoe[1] == tictactoe[2] && tictactoe[2] ==tictactoe[3]) ||
						(tictactoe[0] == tictactoe[1] && tictactoe[1] == tictactoe[2] && tictactoe[3] == 'T') ||
						(tictactoe[0] == tictactoe[1] && tictactoe[1] == tictactoe[3] && tictactoe[2] == 'T') ||
						(tictactoe[0] == tictactoe[2] && tictactoe[2] == tictactoe[3] && tictactoe[1] == 'T')) {
						won = tictactoe[0];
						skip = true;
					}
					else if	(tictactoe[3] == tictactoe[1] && tictactoe[1] == tictactoe[2] && tictactoe[0] == 'T')
					{
						won = tictactoe[3];
						skip = true;
					} else {
						if (status [4] == 'T')
							status[4] = tictactoe[j];

						else if(tictactoe[j] == '.')
							status[4] = tictactoe[j];

						else if (status[4] != tictactoe[j] && status[4] != '.' && status[4] != 'N' && tictactoe[j] != 'T')
							status[4] = 'N';

						if (j==3)
						{
							if (status[4] != 'N')
								won = status [4];
						}
						if (won == 'X' || won == 'O')
							break;


						if (status [5] == 'T')
							status[5] = tictactoe[3-j];

						else if(tictactoe[3-j] == '.')
							status[5] = tictactoe[3-j];

						else if (status[5] != tictactoe[3-j] && status[5] != '.' && status[5] != 'N' && tictactoe[3-j] != 'T')
							status[5] = 'N';

						if (j==3)
						{
							if (status[5] != 'N')
								won = status [5];
						}
						if (won == 'X' || won == 'O')
							break;

						for (int k=0;k<4;k++) {
							if (status [k] == 'T')
								status[k] = tictactoe[k];

							else if(tictactoe[k] == '.')
								status[k] = tictactoe[k];

							else if (status[k] != tictactoe[k] && status[k] != '.' && status[k] != 'N' && tictactoe[k] != 'T')
								status[k] = 'N';

							if (j==3)
							{
								if (status[k] != 'N')
									won = status [k];
							}
							if (won == 'X' || won == 'O')
								break;
						}
					}
				}
			}
		}
		if (won == 'N')
			outfile<<"Case #"<<i+1<<": Draw\n";
		else if (won == '.')
			outfile<<"Case #"<<i+1<<": Game has not completed\n";
		else
			outfile<<"Case #"<<i+1<<": "<<won<<" won\n";
	}
	return 0;
}