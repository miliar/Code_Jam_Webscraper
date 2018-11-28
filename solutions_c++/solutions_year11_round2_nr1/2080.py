#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
using std::cout;
using std::endl;
using std::ifstream;
using std::ofstream;
using std::istringstream;
using std::string;
using std::vector;

struct Score
{
	unsigned int wins;
	unsigned int losses;
	Score();
};

Score::Score()
{
	wins = 0;
	losses = 0;
}

int main(int argc, char *argv[])
{
	if(argc < 3)
		cout << "Usage: " << argv[0] << " <input file> <output file>" << endl;
	
	ifstream inputFile(argv[1]);
	ofstream outputFile(argv[2]);
	unsigned int testCases;
	inputFile >> testCases;
	
	for(unsigned int caseNum = 0; caseNum < testCases; caseNum++)
	{
		unsigned int teamNum;
		inputFile >> teamNum;
		
		string scoreTable[teamNum];
		Score teamScore[teamNum];
		double rpi[teamNum], OWP[teamNum];
		
		for(int i = 0; i < teamNum; i++)
		{
			inputFile >> scoreTable[i];
			for(int j = i + 1; j < teamNum; j++)
			{
				if(scoreTable[i][j] != '.')
				{
					if(scoreTable[i][j] == '1')
					{
						teamScore[i].wins += 1;
						teamScore[j].losses += 1;
					}
					else
					{
						teamScore[j].wins += 1;
						teamScore[i].losses += 1;
					}
				}
			}
		}
		
		for(int i = 0; i < teamNum; i++)
		{
			OWP[i] = 0;
			unsigned int opponents = 0;
			for(int j = 0; j < teamNum; j++)
				if(j != i && scoreTable[i][j] != '.')
				{
					Score tmpScore = teamScore[j];
					if(scoreTable[i][j] == '1')
						tmpScore.losses--;
					else
						tmpScore.wins--;
					OWP[i] += (double)tmpScore.wins / (double)(tmpScore.wins + tmpScore.losses);
					opponents++;
				}
			OWP[i] /= (double)opponents;
		}
		
		for(int i = 0; i < teamNum; i++)
		{
			double OOWP = 0;
			unsigned int opponents = 0;
			for(int j = 0; j < teamNum; j++)
				if(j != i && scoreTable[i][j] != '.')
				{
					OOWP += OWP[j];
					opponents++;
				}
			OOWP /= (double)opponents;
			
			rpi[i] = 0.25 * (((double)(teamScore[i].wins)) / (double)(teamScore[i].wins + teamScore[i].losses)) + 0.50 * OWP[i] + 0.25 * OOWP;
			//cout << "WP: " <<  ((double)(teamScore[i].wins) / (double)(teamScore[i].wins + teamScore[i].losses)) << " OWP: " << OWP[i] << " OOWP: " << OOWP << endl;
		}
		outputFile.precision(12);
		outputFile << "Case #" << caseNum + 1 << ": " << endl;
		for(int i = 0; i < teamNum; i++)
			outputFile << rpi[i] << endl;
	}
	outputFile.close();
	inputFile.close();
	return 0;
}