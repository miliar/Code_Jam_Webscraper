#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
//#include <cmath>

struct SwitchStruct
{
public:
	SwitchStruct(unsigned int aPos, unsigned int aRank) :
	  Position(aPos),
		Rank(aRank)
	  {

	  }

	unsigned int Position;
	unsigned int Rank;
};

std::vector<SwitchStruct> gOrangeList;
std::vector<SwitchStruct> gBlueList;

unsigned int gStep=0;

class Robot
{
public:
	Robot(std::vector<SwitchStruct> &aList) :
		mCurrentHalPosition(1),
		mList(aList),
		mListIt(aList.begin())	
	{

	}

	bool isMyTurn()
	{
		return (mListIt!=mList.end() && gStep==mListIt->Rank);
	}

	/*unsigned int frame()
	{
		unsigned int time(0);
		if(mListIt != mList.end())
		if()
		{
			time=push();
		}
		else
		{
			time=move();
		}
		return time;
	}*/

	unsigned int push()
	{
		unsigned int time = abs((int)(mCurrentHalPosition-mListIt->Position));
		mCurrentHalPosition=mListIt->Position;
		++mListIt;
		++gStep;
		return time +1;
	}

	unsigned int move()
	{
		unsigned int time = abs((int)(mCurrentHalPosition-mListIt->Position));
		mCurrentHalPosition=mListIt->Position;
		return time;
	}

	void move(unsigned int aMaxSteps)
	{
		if(mListIt!=mList.end())
		{

			if (abs((int)(mCurrentHalPosition-mListIt->Position)) <= aMaxSteps)
			{
				mCurrentHalPosition=mListIt->Position;
			}
			else
			{
				if (mCurrentHalPosition > mListIt->Position)
				{
					mCurrentHalPosition-=aMaxSteps;
				}
				else
				{
					mCurrentHalPosition+=aMaxSteps;
				}
			}
		}
	}

private:
	unsigned int mCurrentHalPosition;
	std::vector<SwitchStruct> &mList;
	std::vector<SwitchStruct>::iterator mListIt;
};

Robot *gOrange;
Robot *gBlue;

void gCleanMethod()
{
	gOrangeList.clear();
	gBlueList.clear();

	gStep = 0;
	delete(gOrange);
	delete(gBlue);

}

int main()
{
	std::ofstream outfile;
	outfile.open ("A-large.out");



	std::ifstream myfile;
	myfile.open ("A-large.in", std::ios::in);



	std::string line;
	getline(myfile, line);

	std::istringstream iss(line);

	unsigned int gNbCases;
	iss >> gNbCases;

#ifdef DEBUG
	std::cout << "Nb test cases : " << gNbCases << std::endl;
#endif

	for (unsigned int testId=0;
		testId < gNbCases;
		++testId)
	{
		getline(myfile, line);
		iss = (std::istringstream(line));

		unsigned int nbEntries;
		iss >> nbEntries;

#ifdef DEBUG
		std::cout << "Nb entries line " << testId << " : " << nbEntries << std::endl;
#endif
		char robotColor;
		unsigned int switchPosition;

		for (unsigned int stepId=0;
			stepId<nbEntries;
			++stepId)
		{
			iss >> robotColor >> switchPosition;
#ifdef DEBUG
			std::cout << "Switch " << stepId << " : " << robotColor << "|" << switchPosition << std::endl;
#endif
			switch(robotColor)
			{
				case 'O':
					gOrangeList.push_back(SwitchStruct(switchPosition, stepId));
					break;
				case 'B':
					gBlueList.push_back(SwitchStruct(switchPosition, stepId));
					break;
			}
		}

		gOrange = new Robot(gOrangeList);
		gBlue = new Robot(gBlueList);

		unsigned long time(0);
		unsigned int steps;

		while(gStep<nbEntries)
		{
			if(gOrange->isMyTurn())
			{
				steps = gOrange->push();
				gBlue->move(steps);
			}
			else
			{
				steps = gBlue->push();
				gOrange->move(steps);
			}

			time += steps;
		}


		std::cout << "Case #" << testId+1 << ": " << time << std::endl;
		outfile  << "Case #" << testId+1 << ": " << time << std::endl;

		//Clean code
		gCleanMethod();
	}

	outfile.close();
}