#include<iostream>
#include<limits.h>
using namespace std;

int main()
{
	int cases;
	cin >> cases;
	
	for(int i = 1; i <= cases; i++)
	{
		int numCandies = 0;
		cin >> numCandies;
		
		int smallestValue = INT_MAX;
		long sumSean = 0;
		int xorValue = 0;
		for(int j = 0; j < numCandies; j++)
		{
			int candyValue = 0;
			cin >> candyValue;
			xorValue ^= candyValue;
			sumSean += candyValue;
			if(smallestValue > candyValue)
				smallestValue = candyValue;
		}
		if(xorValue == 0)
		{
			sumSean -= (long)smallestValue;
			cout << "Case #" << i << ": " << sumSean << endl;
		}
		else
		{
			cout << "Case #" << i << ": " << "NO" << endl;
		}
	}
	
	return 0;
}