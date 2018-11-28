#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <list>
using std::cout;
using std::endl;
using std::ifstream;
using std::ofstream;
using std::istringstream;
using std::string;
using std::list;

struct Step
{
	unsigned int step;
	int button;
};

struct Bot
{
	int position;
	list<Step *> instructions;
};

int main(int argc, char *argv[])
{
	if(argc < 3)
		cout << "Usage: " << argv[0] << " <input file> <output file>" << endl;
	
	ifstream inputFile(argv[1]);
	ofstream outputFile(argv[2]);
	unsigned int testCases;
	inputFile >> testCases;
	inputFile.ignore(1, '\n'); // Skips the newline to the next line
	
	string lineString;
	for(int i = 0; i < testCases; i++)
	{
		getline(inputFile, lineString);
		istringstream lineStream(lineString);
		
		Bot orange, blue;
		orange.position = 1;
		blue.position = 1;
		
		unsigned int stepNum;
		lineStream >> stepNum;
		for(int j = 0; j < stepNum; j++)
		{
			char botType;
			lineStream >> botType;
			
			Step *tmpStep = new Step();
			tmpStep->step = j;
			lineStream >> tmpStep->button;
			
			if(botType == 'O')
				orange.instructions.push_back(tmpStep);
			else
				blue.instructions.push_back(tmpStep);
		}
		
		unsigned int clock = 0;
		while(!orange.instructions.empty() || !blue.instructions.empty())
		{
			if(orange.instructions.empty())
			{
				Step *tmpStep = blue.instructions.front();
				int diff = tmpStep->button - blue.position;
				if(diff == 0) // At the button!
				{
					blue.instructions.pop_front();
					delete(tmpStep);
				}
				else // Need to walk.
					blue.position += (diff > 0) ? 1 : -1;
			}
			else if(blue.instructions.empty())
			{
				Step *tmpStep = orange.instructions.front();
				int diff = tmpStep->button - orange.position;
				if(diff == 0) // At the button!
				{
					orange.instructions.pop_front();
					delete(tmpStep);
				}
				else // Need to walk.
					orange.position += (diff > 0) ? 1 : -1;
			}
			else
			{
				Step *orangeStep = orange.instructions.front();
				Step *blueStep = blue.instructions.front();
				bool orangePushed = false;
				bool bluePushed = false;
				
				int diff = orangeStep->button - orange.position;
				if(diff == 0) // At the button!
				{
					if(orangeStep->step < blueStep->step)
						orangePushed = true;
				}
				else // Need to walk.
					orange.position += (diff > 0) ? 1 : -1;
				
				diff = blueStep->button - blue.position;
				if(diff == 0) // At the button!
				{
					if(blueStep->step < orangeStep->step)
						bluePushed = true;
				}
				else // Need to walk.
					blue.position += (diff > 0) ? 1 : -1;
				
				if(orangePushed)
				{
					orange.instructions.pop_front();
					delete(orangeStep);
				}
				
				if(bluePushed)
				{
					blue.instructions.pop_front();
					delete(blueStep);
				}
			}
			clock++;
		}
		outputFile << "Case #" << i + 1 << ": " << clock << endl;
	}
	inputFile.close();
	outputFile.close();
	return 0;
}