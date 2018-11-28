#include <iostream>
#include <cmath>
#include <cstring>
#include <string>

using namespace std;
struct number
{
    long long int high;
    long long int low;
};

void add(number *a, number *b)
{
    
}

int main()
{
    
	unsigned long long int limit = 1000000007;
    int NoOfInputs;
    cin >> NoOfInputs;
//    cout << NoOfInputs << endl;
    int temp = 0;
    for( int i = 0; i < NoOfInputs; i++ )
    {
	long long int n, m, X, Y, Z;
	long long int *A;
	long long int *sList;
	unsigned long long int *cList;
   
	cin >> n >> m >> X >> Y >> Z;
	A = new long long int[m];
	sList =  new long long int[n];
	cList = new unsigned long long int[n];

	for( long long int j = 0; j < m; j++ )
	{
	    cin >> A[j];
	}

	for( long long int j = 0; j < n; j++ )
	{
	      sList[j] = A[ j % m ];
	      A[j % m] = (X * A[j % m] + Y * (j + 1)) % Z;
	     // cout << sList[j] << "\t";
	}	    
	//cout << endl;

	for( long long int j = 0; j < n; j++ )
	{
	    cList[j] = 1;
	    for( long long int k = 0; k < j; k++ )
	    {
		if( sList[j] > sList[k] )
		{
		    cList[j] += cList[k];
		    cList[j] %= limit;
		}
	    }
	}

	unsigned long long int count = 0;
	
	for( long long int j = 0; j < n; j++ )
	{
	    count += cList[j];
	    count = count%limit;
	}
	
	cout << "Case #" <<i+1 << ": " << count << endl;
    }

    return 0;
}
