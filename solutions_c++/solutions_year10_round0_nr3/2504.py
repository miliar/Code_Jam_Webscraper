#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <math.h>
using namespace std;

#define MaxSpace		5000

typedef struct Case
{
	unsigned int r;// number of rounds
	unsigned int k;// capacity of the roller coaster
	unsigned int n; // number of groups
	unsigned int MaxPeople;
}Case;


unsigned int TotalCases;

int main(void)
{
	list<unsigned int> allGroups;

	char temp[MaxSpace];
	ifstream inFile;
	ofstream outFile;
	int Space;
	string t,tmp1, tmp2;
	Case* tempCase;
	char tmpInt[100];
	unsigned int caseNum=1;
	unsigned int Euros =0;
	unsigned int tempPeople;

	inFile.open("C-small-attempt0.in");
	outFile.open("result-small.out");

	// get total number of cases
	inFile.getline(temp, MaxSpace);
	TotalCases = atoi(temp);
	tempCase = (Case*)malloc(sizeof(Case));
	tempCase->MaxPeople = 0;

	for (unsigned int i=0; i < TotalCases; i++)
	{
		inFile.getline(temp, MaxSpace);
		t.assign(temp);

		Space = t.find(' ');
		tmp1 = t.substr(0,Space);
		t = t.substr(Space+1, t.length()-1);
		tempCase->r = atoi(tmp1.c_str());


		Space = t.find(' ');
		tmp1 = t.substr(0,Space);
		t = t.substr(Space+1, t.length()-1);
		tempCase->k =  atoi(tmp1.c_str());
		tempCase->n =  atoi(t.c_str());

		// now let us read in the groups info
		while (!allGroups.empty())
		{
			allGroups.pop_front();
		}
		inFile.getline(temp, MaxSpace);
		t.assign(temp);
		for (unsigned int i=0; i<tempCase->n;i++)
		{
			Space = t.find(' ');
			tmp1 = t.substr(0,Space);
			t = t.substr(Space+1, t.length()-1);
			allGroups.push_back( (unsigned int)atoi(tmp1.c_str()) );
			tempCase->MaxPeople+=allGroups.back();
		}


		printf("readin over\n");
		/************************************************************************/
		/* Start Processing                                                                     */
		/************************************************************************/
		Euros = 0;
		if (tempCase->MaxPeople <= tempCase->k)
		{
			Euros = tempCase->MaxPeople*tempCase->r;
		}
		else
		{
			for (unsigned int rounds=0; rounds<tempCase->r; rounds++)
			{
				tempPeople = 0;
				while ( tempPeople <= tempCase->k)
				{
					tempPeople+= allGroups.front();
					allGroups.push_back(allGroups.front());
					allGroups.pop_front();
				}
				// step back a little bit
				allGroups.push_front(allGroups.back());
				allGroups.pop_back();
				tempPeople-= allGroups.front();

				Euros += tempPeople;

			}
		}


		/************************************************************************/
		/* write file                                                                     */
		/************************************************************************/
		tmp1 = "Case #";
		itoa(caseNum, tmpInt, 10);
		tmp1+=tmpInt;
		tmp1+=": ";
		itoa(Euros, tmpInt, 10);
		tmp1+=tmpInt;
		tmp1+="\n";
		outFile.write(tmp1.c_str(), tmp1.length());
		/************************************************************************/
		/* Garbage collection                                                                     */
		/************************************************************************/
		while (!allGroups.empty())
		{
			allGroups.pop_front();
		}
		caseNum++;
		tempCase->MaxPeople = 0;
	}

	
	inFile.close();
	outFile.close();
	free(tempCase);

	return 1;
}
