#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char **argv)
{
	ifstream inputFile("inputfile");
	ofstream outputFile("outputfile");
	int i = 1;
	int cases = 0;
	char temp;
	int dotFlag = 0;
	int somebodyWon = 0;
	string array[4];
	inputFile >> cases;
	inputFile >> temp;
	while(i <= cases)
	{
		dotFlag = 0;
		somebodyWon = 0;
		//get input
		for(int j = 0; j < 4; j++)
			getline(inputFile, array[j]);
		
		outputFile << "Case #"<<i<<": ";
		
		//main logic
		cout<<"Checking Horizontals"<<endl;
		//check horizontals
		for(int a = 0; a < 4; a++)
		{
			if(array[a][0]=='.')
			{
				dotFlag = 1;
				continue;
			}
			char start;
			int flag = 1;
			if(array[a][0]=='T' && array[a][1]=='.')
			{
				dotFlag = 1;
				continue;
			}
			if(array[a][0]=='T')
				start = array[a][1];
			else
				start = array[a][0];
			for(int b = 0; b < 4; b++)
			{
				if(array[a][b] == 'T')
					continue;
				else if(array[a][b] == '.')
				{
					dotFlag = 1;
					flag = 0;
					break;
				}
				else if(array[a][b] != start)
				{
					flag = 0;
					break;
				}
			}
			if(flag)
			{
				//write output
				outputFile << start << " won\n";
				somebodyWon = 1;
				break;
			}
		}
		
		if(somebodyWon)
		{
			i++;
			inputFile >> temp;
			continue;
		}
		
		//check verticals
		cout<<"Checking Verticals"<<endl;
		for(int a = 0; a < 4; a++)
		{
			if(array[0][a]=='.')
			{
				dotFlag = 1;
				continue;
			}
			char start;
			int flag = 1;
			if(array[0][a]=='T' && array[1][a]=='.')
			{
				dotFlag = 1;
				continue;
			}
			if(array[0][a]=='T')
				start = array[1][a];
			else 
				start = array[0][a];
			for(int b = 0; b < 4; b++)
			{
				if(array[b][a] == 'T')
					continue;
				else if(array[b][a] == '.')
				{
					dotFlag = 1;
					flag = 0;
					break;
				}
				else if(array[b][a] != start)
				{
					flag = 0;
					break;
				}
			}
			if(flag)
			{
				//write output
				outputFile << start << " won\n";
				somebodyWon = 1;
				break;
			}
		}
		
		if(somebodyWon)
		{
			i++;
			inputFile >> temp;
			continue;
		}
		
		//check diagonals
		//diagonal 1 - 00,11,22,33
		cout<<"Checking Diagonal1"<<endl;
		char start;
		int flag = 1;
		if(array[0][0]=='.')
		{
			dotFlag = 1;
			goto diagonal2;
		}
		else if(array[0][0]=='T' && array[1][1]=='.')
		{
			dotFlag = 1;
			goto diagonal2;
		}
		if(array[0][0]=='T')
			start = array[1][1];
		else 
			start = array[0][0];
		for(int b = 0; b < 4; b++)
		{
			if(array[b][b] == 'T')
				continue;
			else if(array[b][b] == '.')
			{
				dotFlag = 1;
				flag = 0;
				break;
			}
			else if(array[b][b] != start)
			{
				flag = 0;
				break;
			}
		}
		if(flag)
		{
			//write output
			outputFile << start << " won\n";
			somebodyWon = 1;
			break;
		}
		
		if(somebodyWon)
		{
			i++;
			inputFile >> temp;
			continue;
		}
		
		//diagonal 2 - 03,12,21,30
		cout<<"Checking Diagonal2"<<endl;
		diagonal2:
		flag = 1;
		if(array[0][3]=='.')
		{
			dotFlag = 1;
			goto diagonal2;
		}
		else if(array[0][3]=='T' && array[1][2]=='.')
		{
			dotFlag = 1;
			goto diagonal2;
		}
		if(array[0][3]=='T')
			start = array[1][2];
		else 
			start = array[0][3];
		for(int b = 0; b < 4; b++)
		{
			if(array[b][3 - b] == 'T')
				continue;
			else if(array[b][3 - b] == '.')
			{
				dotFlag = 1;
				flag = 0;
				break;
			}
			else if(array[b][3 - b] != start)
			{
				flag = 0;
				break;
			}
		}
		if(flag)
		{
			//write output
			outputFile << start << " won\n";
			break;
		}
		
		//Draw and incomplete game
		if(dotFlag)
			outputFile << "Game has not completed\n";
		else
			outputFile << "Draw";
		
		i++;
		inputFile >> temp;
	}
	inputFile.close();
	outputFile.close();
	return 0;
}

