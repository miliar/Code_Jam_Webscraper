#include<iostream>
#include<queue>
using namespace std;

int profit(int R, int k, queue<int> passed)
{
	queue<int> curRun;
	int runsLeft = R;
	int peopleAllowed = k;
	int total = 0;
	
	while(runsLeft != 0)
	{
		int sizeOfCurRun = 0;
		
		
		
		while((sizeOfCurRun < peopleAllowed) && passed.size() != 0)
		{
		
			int seatsRemain = peopleAllowed - sizeOfCurRun;	
			if(passed.front() <= seatsRemain)
			{
				int temp = passed.front();
				passed.pop();
				curRun.push(temp);
					
				sizeOfCurRun += temp;	
			}else{
				break;
			}
		}
		
		while(curRun.size() != 0)
		{
			passed.push(curRun.front());
			curRun.pop();
		}
		
		total += sizeOfCurRun;
		sizeOfCurRun == 0;
		runsLeft--;
	}
	
	return total;
}


int main()
{
	int T, R, N, k;
	
	cin >> T;
	
	for(int i=0; i<T; i++)
	{
		queue<int> curQueue;
		cin >> R;
		cin >> k;
		cin >> N;
		
		for(int j=0; j<N; j++)
		{
			int temp;
			cin >> temp;
			curQueue.push(temp);
		}
		
		cout << "Case #" << (i+1) << ": " << profit(R, k, curQueue) << endl;
	}
	
	return 0;
}
