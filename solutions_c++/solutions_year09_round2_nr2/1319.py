#include <iostream>
#include <list>
#include <iterator>
#include <algorithm>
using namespace std;

int main(void)
{
	int numCases, number;
	list<int> digits;
	
	cin >> numCases;
	for(int numCase = 1; numCase <= numCases; numCase++, digits.clear())
	{
		cin >> number;
		
		while(number)
		{
			digits.push_front(number % 10);
			number /= 10;
		}
		
		cout << "Case #" << numCase << ": ";
		
		if(next_permutation(digits.begin(), digits.end()))
		{
			copy(digits.begin(), digits.end(), ostream_iterator<int>(cout));
		}
		else
		{
			digits.sort();
			
			list<int>::iterator it = digits.begin(), end = digits.end();
			int numZeros = 0;
			
			while(*it == 0)
			{
				numZeros++;
				it++;
			}
			
			cout << *it++ << 0;
			while(numZeros--) cout << 0;
			while(it != end) cout << *it++;
		}
		
		cout << endl;
	}
}
