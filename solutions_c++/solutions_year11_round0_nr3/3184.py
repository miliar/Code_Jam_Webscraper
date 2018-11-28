#include <iostream>
#include "math.h"
#define MAX_CANDIES 1000

using namespace std;

int main()
{
	int ncases, ccase = 0;
	cin >> ncases;
	while (ccase++ < ncases)
	{
		int ncandies, sumCandies = 0;
		cin >> ncandies;
		int candies[MAX_CANDIES];
		for (int i=0; i<ncandies; i++)
		{
			cin >> candies[i];
			sumCandies += candies[i];
		}
		int maxn = (int)pow(2, ncandies) - 1;
		int maxSum = 0;
		for (int i=1; i<maxn; i++)
		{
			int n = i;
			int seanSum = 0, patrickSum1 = 0, patrickSum2 = 0;
			//cout << endl << endl << "testando caso " << i << endl;
			for (int j=1; j<=ncandies; j++)
			{
				if (n & 1)
				{
					//cout << "patrick 1 somou " << patrickSum1 << " e " << candies[j-1] << ", obtendo " << (patrickSum1 xor candies[j-1]) << endl;
					patrickSum1 = patrickSum1 xor candies[j-1];
					seanSum += candies[j-1];
					//cout << "sean tem " << seanSum << " de " << sumCandies << endl;
				}
				else
				{
					//cout << "patrick 2 somou " << patrickSum2 << " e " << candies[j-1] << ", obtendo " << (patrickSum2 xor candies[j-1]) << endl;
					patrickSum2 = patrickSum2 xor candies[j-1];
				}
				n = n >> 1;
			}
			
			//cout << "patrick 1 " << patrickSum1 << " 2 " << patrickSum2 << endl;
			if (patrickSum1 == patrickSum2)
			{
				//cout << "patrick somou igual. sean: " << seanSum << "/" << sumCandies << endl;
				if (seanSum > maxSum)
				{
					maxSum = seanSum;
				}
				else if (sumCandies - seanSum > maxSum)
				{
					maxSum = sumCandies - seanSum;
				}
				//cout << "sean quer " << maxSum << endl;
			}
		}
		
		cout << "Case #" << ccase << ": ";
		if (maxSum > 0)
			cout << maxSum;
		else
			cout << "NO";
		cout << endl;
	}
}
