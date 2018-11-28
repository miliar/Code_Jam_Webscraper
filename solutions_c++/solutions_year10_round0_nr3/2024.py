#include <iostream>
using namespace std;

int main() {

	int numIter;
	cin >> numIter;
	
	for(int i=1; i <= numIter; i++)
	{
		long long R;
		long long k;
		int N;
		cin >> R;
		cin >> k;
		cin >> N;
		
		long long * groups = new long long[N];
		for(int j=0; j < N; j++) cin >> groups[j];
		
		//this array stores the # of euros when we begin an iteration at a particular group 
		long long * cycleEuros = new long long[N];
		for(int j=0; j < N; j++) cycleEuros[j] = -1;
		
		//this array stores the iteration # when we begin an iteration at a particular group, used to find the length of the cycle 
		long long * cycleStart = new long long[N];
		for(int j=0; j < N; j++) cycleStart[j] = -1;
		
		//stores the current iteration, should always be <= R
		long long currentIter = 0;
		//stores the group that is first in line
		long long startIndex = 0;
		long long totalEuros = 0;
		bool cycle = false;
		int cycleLength = -1;
		
		//load the roller coaster x times until we find a cycle
		while(currentIter < R)
		{
			long long groupCount = 0;
			long long numberOnCoaster = 0;
			
			cycleEuros[startIndex] = totalEuros;
			cycleStart[startIndex] = currentIter;
			
			while(groupCount < N)
			{
				if(numberOnCoaster + groups[startIndex] > k)
					break;
				
				groupCount++;
				numberOnCoaster += groups[startIndex];
				startIndex = (startIndex + 1) % N;
			}
			
			totalEuros += numberOnCoaster;
			numberOnCoaster = 0;
			currentIter++;
			
			//check for cycle here
			if(cycleEuros[startIndex] != -1 && !cycle)
			{
				cycle = true;
				long long cycleValue = totalEuros - cycleEuros[startIndex];
				long long cycleLength = currentIter - cycleStart[startIndex];
			
				while(1)
				{
					if(currentIter + cycleLength >= R)
						break;
					
					currentIter += cycleLength;
					totalEuros += cycleValue;
				}
			}
		}		
		
		delete [] groups;
		delete [] cycleEuros;
		delete [] cycleStart;
		
		cout << "Case #" << i << ": " << totalEuros << endl;
	}
}

