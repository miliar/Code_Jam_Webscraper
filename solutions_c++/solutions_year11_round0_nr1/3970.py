#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <math.h>
using namespace std;

#define MaxSpace		5000
#define O	'O'
#define B	'B'


unsigned int	nTotalTestCase;

typedef struct Rbutton
{
	unsigned int index;
	char	RobotName;
	unsigned int	ButtonPos;
	bool beingTheTarget;
}Rbutton;

Rbutton Hallway[101];
list<Rbutton> OList;
list<Rbutton> BList;
unsigned int nPosNum;

unsigned int OPosLast;
unsigned int BPosLast;

unsigned int Calculate(void);


int main(void)
{
	ifstream inFile;
	ofstream outFile;
	char temp[MaxSpace];
	unsigned int spacePos;
	string tmp1, tmp2;


	inFile.open("A-large.in");
	outFile.open("result-large.out");

	inFile.getline(temp, MaxSpace);
	nTotalTestCase = atoi(temp);

	for (unsigned int i = 0;i < nTotalTestCase; i++)
	{
		inFile.getline(temp, MaxSpace);
		string t(temp);
		spacePos = t.find(' ');
		tmp1 = t.substr(0, spacePos);
		tmp2 = t.substr(spacePos+1, t.length() - 1);
		nPosNum = atoi(tmp1.c_str());
		for (unsigned int j = 0;j<nPosNum;j++)
		{
			spacePos = tmp2.find(' ');
			tmp1 = tmp2.substr(0, spacePos);
			Hallway[j].RobotName = tmp1[0];
			tmp2 = tmp2.substr(spacePos+1, tmp2.length() - 1);
			spacePos = tmp2.find(' ');
			tmp1 = tmp2.substr(0, spacePos);
			Hallway[j].ButtonPos = atoi(tmp1.c_str());
			tmp2 = tmp2.substr(spacePos+1, tmp2.length() - 1);
			Hallway[j].index = j;
			Hallway[j].beingTheTarget = false;
			if (Hallway[j].RobotName == O)
			{
				OList.push_back( (Hallway[j]));
			}
			else
			{
				BList.push_back((Hallway[j]));
			}
			
		}

		tmp1 ="Case #";
		itoa(i+1, temp, 10);
		tmp1 += temp;
		tmp1 += ": ";
		itoa(Calculate(), temp, 10);
		tmp1 += temp;
		tmp1+= "\n";
		outFile.write(tmp1.c_str(), tmp1.length());

	}

	inFile.close();
	outFile.close();
	return 1;
}

unsigned int Calculate() // parameters   nPosNum,   Hallway[100]
{
	unsigned int OCurrentPos = 1;
	unsigned int BCurrentPos = 1;
	unsigned int OCurrentId;
	unsigned int BCurrentId;
	unsigned int ONextPos;
	unsigned int BNextPos;
	unsigned int index=0;
	unsigned int SystemTime = 0;
	bool	AllowedToAction;

// 	if ((OList.size() == 0) || (BList.size() == 0))  // only one robot in the case.
// 	{
// 		for (unsigned int i = 0;i<nPosNum;i++)
// 		{
// 			if (i == 0)
// 			{
// 				SystemTime += Hallway[0].ButtonPos - 1 + 1;
// 			}
// 			else
// 			{
// 				SystemTime += abs((int)Hallway[i].ButtonPos - (int)Hallway[i-1].ButtonPos+1);
// 			}
// 		}
// 	}
// 
// 	else  // two robots
 	{

		while (OList.size() >0 || BList.size() >0)
		{
			SystemTime ++;
			AllowedToAction = true;
			if (OList.size() > 0)
			{
				ONextPos = OList.front().ButtonPos;
				if (ONextPos >OCurrentPos)
				{
					OCurrentPos ++;
				}
				else if (ONextPos < OCurrentPos)
				{
					OCurrentPos--;
				}
				else // equal
				{
					if (OList.front().index == index && AllowedToAction)// reached one button
					{
						OList.pop_front();
						AllowedToAction = false;
						index++;
					}
				}
			}

			if (BList.size() > 0)
			{
				BNextPos = BList.front().ButtonPos;
				if (BNextPos >BCurrentPos)
				{
					BCurrentPos ++;
				}
				else if (BNextPos < BCurrentPos)
				{
					BCurrentPos--;
				}
				else // equal
				{
					if (BList.front().index == index && AllowedToAction)// reached one button
					{
						BList.pop_front();
						AllowedToAction = false;
						index++;
					}
				}
			}



		}
		
	}


	return SystemTime;
}


