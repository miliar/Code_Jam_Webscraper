#include <iostream.h>
#include <fstream.h>
#include <list.h>


int main(void)
{
	int iCases;
	int iCaseCounter;
	int answer;
	list<int> freq;
	list<int>::iterator iter; 
	int i,j;
	
	int P,K,L;
	
	ifstream inFile;
	
	
	//inFile.open("A-test.in");
	inFile.open("A-small-attempt0.in");
	//inFile.open("A-large.in");
	if ( !inFile )
	{
		cout << "Error opening file!" << endl;
		exit(1);
	}
	
	inFile >> iCases;
	for (iCaseCounter=1;iCaseCounter<iCases+1;iCaseCounter++)
	{
		answer = 0;
		
		inFile >> P >> K >> L;
		freq.clear();
		for (i=0;i<L;i++)
		{
			inFile >> j;
			freq.push_back(j);
		}
		
		freq.sort();
		freq.reverse();
		i = 0;
		j = 1;
		for (iter=freq.begin();iter!=freq.end();iter++)
		{
			if ( i == K )
			{
				j++;
				i = 0;
			}
			answer = answer + *iter*j;
			
			i++;
		}
	
		
		cout << "Case #" << iCaseCounter << ": " << answer << endl;
	}
	
	

	
	inFile.close();
	return 0;
}