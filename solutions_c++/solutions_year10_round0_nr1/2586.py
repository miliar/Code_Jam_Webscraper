#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <math.h>
using namespace std;

#define MaxSpace		5000

typedef struct Case
{
	unsigned N;// snapper number
	unsigned K;// number of snap actions
}Case;


char Judge(Case* tempCase);

unsigned int TotalCases;

int main(void)
{
	list<Case> all;

	char temp[MaxSpace];
	char OnOrOff;
	ifstream inFile;
	ofstream outFile;
	int Space;
	string tmp1, tmp2;
	Case* tempCase;
	char tmpInt[100];

	inFile.open("A-large.in");
	outFile.open("result-large.out");

	inFile.getline(temp, MaxSpace);
	TotalCases = atoi(temp);

	for (unsigned int i=0; i < TotalCases; i++)
	{
		inFile.getline(temp, MaxSpace);
		string t(temp);
		Space = t.find(' ');
		tmp1 = t.substr(0,Space);
		tmp2 = t.substr(Space, t.length()-1);
		tempCase = (Case*)malloc(sizeof(Case));
		tempCase->N = atoi(tmp1.c_str());
		tempCase->K = atoi(tmp2.c_str());
		all.push_back(*tempCase);
	}

	printf("readin over\n");
	inFile.close();
	/************************************************************************/
	/* Start Processing                                                                     */
	/************************************************************************/

	int j=1;
	while (!all.empty())
	{
		tempCase = &(all.front());
		
		OnOrOff = Judge(tempCase);
		tmp1 = "Case #";
		itoa(j, tmpInt, 10);
		tmp1+=tmpInt;
		if (OnOrOff == 1)
		{
			tmp1.append(": ON\n");
		}
		else
		{
			tmp1.append(": OFF\n");
		}
		outFile.write(tmp1.c_str(), tmp1.length());

		all.pop_front();
		j++;
	}

	outFile.close();

	return 1;
}

char Judge(Case* tempCase)
{
	int tmp=1;

	for (unsigned int i=0;i<tempCase->N;i++)
	{
		tmp = tmp <<1;
	}

	if ( ( (tempCase->K+1) % tmp ) ==0   ) 
	{
		return 1;
	}
	else return 0;
	
}