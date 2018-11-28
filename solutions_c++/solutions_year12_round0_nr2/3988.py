#include<iostream>
#include<fstream>

using namespace std;

struct Person
{
	int myTotalScore;
	int myMinScore;
	int myMaxScore;
	bool isSurpriseReq;
};
int getResult(struct Person** aPersons, int numPersons, int numSurprisings, int minReqScore);
void getMinMaxScores(struct Person* aPerson);

int main()
{
   int numExamples;
   int numPersons;
   int numSurprisings;
   int minReqScore;
   ifstream ipfile1;
   ipfile1.open("input.txt");
   ipfile1>>numExamples;
   for (int i=0; i<numExamples; i++)
   {
	ipfile1>>numPersons;
	ipfile1>>numSurprisings;
	ipfile1>>minReqScore;
	struct Person** persons = new struct Person*[numPersons];
	for (int j=0; j<numPersons; j++)
	{
		persons[j] = new struct Person;
		ipfile1>>persons[j]->myTotalScore;
		getMinMaxScores(persons[j]);
	}

	cout<<"Case #"<<i+1<<":"<<" "<<getResult(persons, numPersons, numSurprisings, minReqScore)<<endl;
   }
}



int getResult(struct Person** aPersons, int numPersons, int numSurprisings, int minReqScore)
{
   int theResult = 0;
   for (int i=0; i<numPersons; i++)
   {
	if (!aPersons[i]->isSurpriseReq && aPersons[i]->myMaxScore >= minReqScore)
	{
		theResult++;
	}
	else if (aPersons[i]->isSurpriseReq && aPersons[i]->myMinScore >= minReqScore)
	{
		theResult++;
	}
	else if (aPersons[i]->isSurpriseReq && aPersons[i]->myMaxScore >= minReqScore && numSurprisings > 0)
	{
		theResult++;
		numSurprisings--;
	}
   }
   return theResult;
}

void getMinMaxScores(struct Person* aPerson)
{
   int theTotalScore = aPerson->myTotalScore;
   int theRemainder = theTotalScore%3;
   int theQuotent = theTotalScore/3;

   if (theRemainder == 0)
   {
	if (theTotalScore == 0)
	{
		aPerson->myMinScore = 0;
		aPerson->myMaxScore = 0;
		aPerson->isSurpriseReq = false;
	}
	else
	{
		aPerson->myMinScore = theQuotent;
		aPerson->myMaxScore = theQuotent + 1;
		aPerson->isSurpriseReq = true;
	}	
   }
   else if (theRemainder == 1)
   {
	if (theTotalScore == 1)
	{
		aPerson->myMinScore = 1;
		aPerson->myMaxScore = 1;
		aPerson->isSurpriseReq = false;
	}
	else
	{
		aPerson->myMinScore = theQuotent+1;
		aPerson->myMaxScore = theQuotent+1;
		aPerson->isSurpriseReq = false;
	}
   }
   else
   {
	if (theTotalScore == 2)
	{
		aPerson->myMinScore = 1;
		aPerson->myMaxScore = 2;
		aPerson->isSurpriseReq = true;
	}
	else
	{
		aPerson->myMinScore = theQuotent+1;
		aPerson->myMaxScore = theQuotent+2;
		aPerson->isSurpriseReq = true;
	}
   }
}





