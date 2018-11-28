#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;


int numberofTestCases;

struct TestCase
{
	int NnumberOfGooglers;
	int SnumberOfSurprisingTripletsOfScores;
	int PminimumNeededNumbers;
	int* TotalPointsOfGooglers;
};
struct GooglerScore
{
	int Score1,Score2,Score3;
};
void readFromFile(ifstream &inp,TestCase** testCases)
{
	inp>>numberofTestCases;
	*testCases=new TestCase[numberofTestCases];
	for(int i=0;i<numberofTestCases;i++)
	{
		inp>>(*testCases)[i].NnumberOfGooglers;
		inp>>(*testCases)[i].SnumberOfSurprisingTripletsOfScores;
		inp>>(*testCases)[i].PminimumNeededNumbers;
		(*testCases)[i].TotalPointsOfGooglers=new int[(*testCases)[i].NnumberOfGooglers];
		for(int j=0;j<(*testCases)[i].NnumberOfGooglers;j++)
			inp>>(*testCases)[i].TotalPointsOfGooglers[j];
	}
}
void sortGooglers(int* GooglersTotal,int numberOfGooglers,int PminimumNeededNumbers)
{
	int min;
	int temp;
	
	for(int i = 0 ; i < numberOfGooglers ; i++)
	{
		min = i;
		for(int j = i ; j < numberOfGooglers ; j++)
		{
			if((GooglersTotal[j]+1)%3==0 && ((GooglersTotal[j]+1)/3)+1==PminimumNeededNumbers)
			{
				min = j;
			}
			else if((GooglersTotal[j])%3==0 && ((GooglersTotal[j])/3)+1==PminimumNeededNumbers)
			{
				min = j;
			}
		}
			temp = GooglersTotal[min];
			GooglersTotal[min]=GooglersTotal[i];
			GooglersTotal[i] = temp;
		/*else
			swap( processes[i],processes[min] );
	*/	
	}
}

void main()
{

	ifstream inp("B-large.in");
	ofstream outp("output.txt");
	TestCase* testCases=new TestCase;

	readFromFile(inp,&testCases);
	for(int i=0;i<numberofTestCases;i++)
	{
		GooglerScore* Googlers=new GooglerScore[testCases[i].NnumberOfGooglers];
		int neededOutput=0;
		for(int j=0;j<testCases[i].NnumberOfGooglers;j++){
			Googlers[j].Score1=0;Googlers[j].Score2=0;Googlers[j].Score3=0;}
		int numberOfSurprisingFound=0;
		sortGooglers(testCases[i].TotalPointsOfGooglers,testCases[i].NnumberOfGooglers,testCases[i].PminimumNeededNumbers);
		for(int j=0;j<testCases[i].NnumberOfGooglers;j++)
		{
			if(numberOfSurprisingFound!=testCases[i].SnumberOfSurprisingTripletsOfScores)
			{
				while(testCases[i].TotalPointsOfGooglers[j]!=0)
				{
					if(testCases[i].TotalPointsOfGooglers[j]>3)
					{
						Googlers[j].Score1++;
						testCases[i].TotalPointsOfGooglers[j]--;
					}
					else
					{
						testCases[i].TotalPointsOfGooglers[j]=0;
						if(Googlers[j].Score1==9){
							Googlers[j].Score1++;Googlers[j].Score2++;Googlers[j].Score2++;}
						else{
							Googlers[j].Score1++;Googlers[j].Score2++;Googlers[j].Score2++;}
						continue;
					}
					if(testCases[i].TotalPointsOfGooglers[j]>3)
					{
						Googlers[j].Score2++;
						testCases[i].TotalPointsOfGooglers[j]--;
					}
					else
					{
						testCases[i].TotalPointsOfGooglers[j]=0;
						
						if(Googlers[j].Score1==9){
							Googlers[j].Score1++;Googlers[j].Score2++;Googlers[j].Score2++;}
						else{
							Googlers[j].Score1++;Googlers[j].Score2++;Googlers[j].Score2++;
						}
						continue;
					}
					if(testCases[i].TotalPointsOfGooglers[j]>3)
					{
						Googlers[j].Score3++;
						testCases[i].TotalPointsOfGooglers[j]--;
					}
					else
					{
						testCases[i].TotalPointsOfGooglers[j]=0;
						if(Googlers[j].Score2==9){
							Googlers[j].Score1++;Googlers[j].Score2++;Googlers[j].Score3++;numberOfSurprisingFound--;}
						else{
						Googlers[j].Score3++;Googlers[j].Score1++;Googlers[j].Score1++;
						}
						continue;
					}

				}
				numberOfSurprisingFound++;
			}
			else
			{
				while(testCases[i].TotalPointsOfGooglers[j]!=0)
				{
					if(testCases[i].TotalPointsOfGooglers[j]!=0)
					{
						Googlers[j].Score1++;
						testCases[i].TotalPointsOfGooglers[j]--;
					}
					if(testCases[i].TotalPointsOfGooglers[j]!=0)
					{
						Googlers[j].Score2++;
						testCases[i].TotalPointsOfGooglers[j]--;
					}
					if(testCases[i].TotalPointsOfGooglers[j]!=0)
					{
						Googlers[j].Score3++;
						testCases[i].TotalPointsOfGooglers[j]--;
					}
				}
			}
			if(Googlers[j].Score1>=testCases[i].PminimumNeededNumbers||Googlers[j].Score2>=testCases[i].PminimumNeededNumbers||Googlers[j].Score3>=testCases[i].PminimumNeededNumbers)
				neededOutput++;
				
		}
		outp<<"Case #"<<i+1<<": "<<neededOutput;
		if(i<100)
			outp<<endl;
	}
}