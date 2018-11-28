#include<math.h>
#include<iostream>
#include<fstream>

using namespace std;

void Sort(int candy[], int n)
{
	int tmp;
	int i;
	int j;
	for(i = 0 ; i < n; ++i)
		for(j = i; j < n; ++j);
			if(candy[i] > candy[j])
			{
				tmp = candy[j]; 
				candy[j] = candy[i];
				candy[i] = tmp;
			}
}

void main()
{
	int candy[10000];
	int nCan = 0;
	int numTests = 0;
	cin>>numTests;
	int numCands;
	for(int nTests = 0; nTests < numTests; ++nTests )
	{
		cin>>numCands;
		nCan = 0;
		for(int i = 0 ;i < numCands; ++i)
		{
			cin>>candy[nCan];
			++nCan;
		}
		int maxSum = -1;
		int k = 0;
		bool flag = true;
		int p = (2<<nCan) - 1;
		int patrick = 0;
		int sean = 0;
		int seanReal = 0;
		for(int caseP = 1; caseP < (p - 1) ; ++caseP)
		if(caseP != (p - 2<<(nCan - 1))){
			sean = 0;
			patrick = 0;
			seanReal = 0;
			for(int i = 0; i < nCan; ++i )
			{
				if((caseP & (2<<i)) > 0)
				{
					sean ^= candy[i];
					seanReal += candy[i];
				}
				else
				{
					patrick ^= candy[i];
				}
			}
			if(patrick==sean)
				if (seanReal > maxSum)
				{
					maxSum = seanReal;
				}
		}
		if(maxSum < 0)
		{
			cout<<"Case #"<<nTests +1 <<": NO"<<endl;
		}
		else
		{
			cout<<"Case #"<<nTests +1 <<": "<<maxSum<<endl;
		}
	}
}