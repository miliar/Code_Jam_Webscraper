#include<iostream>
#include<fstream>
#include<math.h>

using namespace std;

#define INFILE "A-small-attempt0.in"
#define OUTFILE "A-small-attempt0.out"

int main()
{
	ifstream inStream;
	ofstream outStream;
	int T;					//Number of test cases
	int N;					//Number of buttons needing to be pressed
	int OmaxPos = 1;
	int BmaxPos = 1;
	int maxPos;
	string robotName;
	int robotPos;
	string lastActedRobot;
	int Opushes = 0;
	int Bpushes = 0;
	string donatedRobot;
	
	outStream.open(OUTFILE);
	inStream.open(INFILE);
	
	inStream >> T;
	cout << "T = " << T << endl;
	for (int i = 1; i <= T; i ++)
	{
		inStream >> N;
		int j = 1;
		OmaxPos = 1;
		BmaxPos = 1;
		Opushes = 0;
		Bpushes = 0;
		while (j <= N)
		{
			inStream >> robotName;
			inStream >> robotPos;
			if (robotName == "O")
			{
				Opushes ++;
				if (robotPos > OmaxPos)
					OmaxPos = robotPos;
			}
			if (robotName =="B")
			{
				Bpushes ++;
				if (robotPos > BmaxPos)
					BmaxPos = robotPos;
			}
			if (j == N)
			{
				if (robotName == "O")
				{
					lastActedRobot = "O";
				}
				else
				{
					lastActedRobot = "B";	
				}
			}
			j++;
		}
		if (OmaxPos > BmaxPos)
		{
			donatedRobot = "O";
			maxPos = OmaxPos;
		}
		else 
		{
			donatedRobot = "B";
			maxPos = BmaxPos;	
		}
		outStream << "Case #" << i << ": ";
		if (donatedRobot == "O")
		{
			outStream << maxPos + Opushes << endl;
		}
		if (donatedRobot == "B")
		{
			outStream << maxPos + Bpushes << endl;
		}
	}
	inStream.close();
	outStream.close();
	//system("pause");
	return 0;	
}
