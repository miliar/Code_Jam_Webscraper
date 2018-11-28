
//#include <stdio.h>

#include <iostream>

using namespace std;

int main()
{
	unsigned int nTestCase = 0; // (1-10000)
	
	cin >> nTestCase;
	
	for (unsigned int iTestCase = 1;
			iTestCase <= nTestCase;
			++iTestCase)
	{
		bool result = true;
		
		unsigned int nSnappers = 1; // (1-30)
		unsigned int nFingerSnaps = 0; // (0-10 000 000)
		cin >> nSnappers;
		cin >> nFingerSnaps;
		
		int t = 1;
		for (int i = 1; i <= nSnappers; ++i)
		{
			t = nFingerSnaps & 0x1;
			nFingerSnaps >>= 1;
			if (t == 0)
			{
				result = false;
				break;
			}
			
		}
		
		
		cout << "Case #" << iTestCase << ": " << (result ? "ON" : "OFF") << endl;
	}
	
	return 0;
}
