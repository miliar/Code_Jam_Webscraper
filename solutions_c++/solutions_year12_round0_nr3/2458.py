#include <iostream>
#include <vector>
#include <map>
#include <list>

using namespace std;

// 1 <= A <= B <= 2000000.
// 2 000 000

int getValue(int* d, int n, int r)
{
 	int result = 0;

	for(int i = 0; i < n; i++)
	 result = result * 10 + d[n - (i + r) % n - 1];

	return result;
}

void processCase()
{
	int A, B;
	int counter = 0;

	cin >> A;
	cin >> B;

	for(int n = A; n <= B; n++)
	{
		// pairs must be distict so ensure that m > n
		int d[7], nk = n, ni = 0;

		while(nk != 0) 
		{ 
			d[ni] = nk % 10; 
			ni++; 
			nk /= 10; 
		};

		// ni - number of digits. ni - 1  - maximum rotation numbers
	
		int uniq[7], uniqIndex;
		uniqIndex = 0;

		for(int i = 1; i < ni; i++)
		{
			bool uniqValue = true;

			int m = getValue(d, ni, i);
			if( (m > n) && (m >=A) && (m <=B)) 
			{
				for(int j = 0; j < uniqIndex; j++)
					if(uniq[j] == m) 
					{
						uniqValue = false;
						break;
					}
				
				if(uniqValue) 
				{   
					uniq[uniqIndex] = m; 
					uniqIndex++;
				}

			}

		}

		counter += uniqIndex;
	}

	cout << counter;
}

int main(int argc, const char * argv[])
{

	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		printf("Case #%d: ", i + 1);
			processCase();
		printf("\n");
	}
	
    return 0;
}
