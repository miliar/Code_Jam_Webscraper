#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

int isPossible(int score, int best)
{
	int rest = score-best;
	if (rest<0)
	{
		return 0;
	}
	int small = rest/2;
	int big = rest - small;
	if (small<=best)
	{
		if (abs(best-small)<=1) return 1;
		else if(abs(best-small)<=2) return 2;
		else return 0;
	}
	else
	{
		if (abs(big-best)<=1) return 1;
		else if(abs(big-best)<=2) return 2;
		else return 0;
	}

}

int main()
{
	int numCases;
	cin>>numCases;
	for(int i=0;i<numCases;i++) 
	{
		int numGooglers,numSurprising, minBest;
		cin>>numGooglers>>numSurprising>>minBest;
		int googlers[numGooglers];
		memset(googlers, 0, sizeof(int)*numGooglers);
		for (int j=0;j<numGooglers;j++) 
		{
			cin>>googlers[j];
		}
		int numPossible = 0;
		for (int j=0;j<numGooglers;j++) 
		{
			int possibility = 0;
			for (int k=minBest;k<=10;k++)
			{
				int newPossibility = isPossible(googlers[j], k);
				if (newPossibility==1) 
				{
					possibility = newPossibility;
					break;
				}
				else if(newPossibility==2)
				{
					possibility = newPossibility;
					continue;
				}
			}
			if (possibility==2 && numSurprising) {
				numSurprising--;
				numPossible++;
			}
			else if (possibility==1) {
				numPossible++;
			}
		}
		cout<<"Case #"<<i+1<<": "<<numPossible<<endl;
	}
}
