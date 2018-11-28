#include<math.h>
#include<iostream>
#include<fstream>


using namespace std;

void main()
{
	int testO[1000];
	int testB[1000];
	int T = 0;
	int N = 0;
	int nStepsO = 0, nStepsB = 0;
	int numTests = 0;
	int numPush = 0;
	char tmp;
	char sequence[10000];
	int numS = 0;
	cin>>numTests;
	int res = 0;	
	int maxSteps;
	for(int nTests = 0; nTests < numTests; ++nTests )
	{
		res= 0;
		numS = 0;
		numPush = 0;
		cin>>numPush;
		T = 0;
		N = 0;
		for(int nPush= 0 ;nPush < numPush; ++nPush)
		{
			cin>>sequence[numS];
			++numS;
			if(sequence[numS - 1]=='O')
			{
				cin>>testO[T];
				++T;
			}
			else
			{
				cin>>testB[N];
				++N;
			}
		}
		int curO = 1, curB = 1;
		int i = 0; int j = 0;
		maxSteps = 0;
		for(int ins = 0; ins < numS; ++ins)
		{
			int distO = abs(testO[i] - curO);
			int distB = abs(testB[j] - curB);
			if(sequence[ins]=='O')
			{
				maxSteps += distO + 1;
				curO = testO[i];
				if(i < ( T - 1) )
					++i;
				if(distO > distB)
				{
					curB = testB[j];
				}
				else
				{
					if(curB < testB[j])
					{
						curB += min(distB,  distO + 1 );
					}
					else if (curB > testB[j])
					{
						curB -= min(distB,  distO + 1 );
					}
				}
			}
			else
			{
				maxSteps += distB + 1;	
				curB = testB[j];
				if(j < (N - 1))
					++j;
				if(distO < distB)
				{	
					curO = testO[i];
				}
				else
				{
					if(curO < testO[i])
					{
						curO += min(distO,  distB + 1 );
					}
					else if(curO > testO[i])
					{
						curO -= min(distO,  distB + 1 );
					}
				}
			}
		}
		cout<<"Case #"<<nTests +1 <<": "<<maxSteps<<endl;
	}
}