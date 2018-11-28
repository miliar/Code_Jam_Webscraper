#include <iostream>
#include <queue>

using namespace std;

int main()
{
	queue<unsigned int> waitingGroups;
	queue<unsigned int> ridingGroups;
	unsigned int numberOfTestCases, runTime, rollerCapacity, numberOfGroups, temp;
	unsigned int currentPeopleNumber, eurosMade;
	unsigned int i ,j;
	
	cin >> numberOfTestCases;
	
	for(i = 0; i < numberOfTestCases; i++)
	{
		cin >> runTime >> rollerCapacity >> numberOfGroups;
		eurosMade = 0;
		
		while(!waitingGroups.empty())
			waitingGroups.pop();
		
		while(!ridingGroups.empty())
			ridingGroups.pop();
		
		for(j = 0; j < numberOfGroups; j++)
		{
			cin >> temp;
			waitingGroups.push(temp);
		}
		
		for(j = 0; j < runTime; j++)
		{
			currentPeopleNumber = 0;
			temp = waitingGroups.front();
			
			while(!waitingGroups.empty() && ((currentPeopleNumber + temp) <= rollerCapacity))
			{
				currentPeopleNumber += temp;
				ridingGroups.push(temp);
				waitingGroups.pop();
				
				if(!waitingGroups.empty())
					temp = waitingGroups.front();
			}
			
			while(!ridingGroups.empty())
			{
				waitingGroups.push(ridingGroups.front());
				ridingGroups.pop();
			}
			
			eurosMade += currentPeopleNumber;
		}
		
		cout << "Case #" << i+1 << ": " << eurosMade << endl;
	}
	
	return 0;
}
