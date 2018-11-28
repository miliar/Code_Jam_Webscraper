#include <iostream>
#include <cmath>
#include <cstring>
#include <string>

using namespace std;

int main()
{
    
	unsigned long long int limit = 1000000007;
    int NoOfInputs;
    cin >> NoOfInputs;
    int temp = 0;
    for( int i = 0; i < NoOfInputs; i++ )
    {
	long long int n, m, X, Y, Z;
	long long int *A;
	long long int *speed_list;
	unsigned long long int *count_list;
   
	cin >> n >> m >> X >> Y >> Z;
	A = new long long int[m];
	speed_list =  new long long int[n];
	count_list = new unsigned long long int[n];

	for( long long int j = 0; j < m; j++ )
	{
	    cin >> A[j];
	}

	for( long long int j = 0; j < n; j++ )
	{
	      speed_list[j] = A[ j % m ];
	      A[j % m] = (X * A[j % m] + Y * (j + 1)) % Z;
	}	    

	for( long long int j = 0; j < n; j++ )
	{
	    count_list[j] = 1;
	    for( long long int k = 0; k < j; k++ )
	    {
		if( speed_list[j] > speed_list[k] )
		{
		    count_list[j] += count_list[k];
		    count_list[j] %= limit;
		}
	    }
	}

	unsigned long long int count = 0;
	
	for( long long int j = 0; j < n; j++ )
	{
	    count += count_list[j];
	    count = count%limit;
	}
	
	cout << "Case #" <<i+1 << ": " << count << endl;
    }

    return 0;
}
