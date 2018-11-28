#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <complex>


using namespace std;


int
main (void)
{
    int step;
    cin >> step;
    for(int i = 0; i<step; i++)
    {
	int N, S, P, nbres = 0;
	cin >> N >> S >> P;
	
	for(int ggler = 0; ggler < N; ggler++)
	{
	    int sum, val, reste;
	    cin >> sum;
	    val = sum/3;
	    reste = sum - val*3;

	    if(val >= P)
	    {
		nbres++;
		continue;
	    }

	    if(val == P-1)
	    {
		if(reste == 0 && S > 0 && val > 0)
		{
		    // Surprising here
		    nbres++;
		    S--;
		    continue;
		}
		if(reste >= 1)
		{
		    nbres++;
		    continue;
		}
	    }

	    if(val == P-2 && reste == 2 && S > 0)
	    {
		// Surprising here
		nbres++;
		S--;
		continue;
	    }
	}

	
	cout << "Case #" << i+1 << ": " << nbres << endl;
	
    }

    return 0;
}
