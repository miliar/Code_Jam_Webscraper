// C. Theme Park
// author: vlad.rubtsov@gmail.com


#include <iostream>
#include <queue>

using namespace std;



int main()
{
	unsigned int nTestCase = 0; // (T = 1-50)
	
	cin >> nTestCase;
	
	for (unsigned int iTestCase = 1;
			iTestCase <= nTestCase;
			++iTestCase)
	{
		unsigned int result = 0;
		
		int nRunTimes = 1; // (R = 1-10^8)
		int nPeople = 1; // (k = 1-10^9) holds
		int nGroup = 1; // (N = 1-1000)
		
		cin >> nRunTimes;
		cin >> nPeople;
		cin >> nGroup;
		
		queue<int> q;
		for (int i = 0; i < nGroup; ++i)
		{
			int p = 0;
			cin >> p;
			q.push(p);
		}
		
		int sum = 0;
		
		for (int i = 0; i < nRunTimes; ++i)
		{
			int inTrain = 0;
			for (int j = 0; j < nGroup; ++j)
			{
				int t = q.front();
				
				if (inTrain + t <= nPeople)
				{
					//cout << t << " ";
					inTrain += t;
					q.pop();
					q.push(t);
				}
				else
				{
					//cout << endl;
					break;
				}
				
			}
			sum += inTrain; // 1e
		}
		
		//cout << "sum = " << sum << endl;
		
		result = sum;
		
		cout << "Case #" << iTestCase << ": " << result << endl;
		
		//cout << nGroup << endl;
	}
	
	return 0;
}
