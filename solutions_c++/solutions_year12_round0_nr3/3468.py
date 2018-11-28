#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <math.h>

using namespace std;

int solve();
int rotate(int n);

int main()
{

    int T;
    cin >> T;
    for(int i=0; i<T; ++i)
	{
	    cout << "Case #" << i+1 << ": " << solve() << endl;
	}

    return 0;
}


int solve()
{
    int A,B;
    cin >> A >> B;

    int counter = 0;
    for(int n=A; n<B; ++n)
	{
	    int m = rotate(n);
	    while(m != n)
		{
		    if(m > A && m <= B && n < m)
			counter++;

		    m = rotate(m);
		}	    
	}
    
    return counter;
}


int rotate(int n)
{
    if(n <= 10)
	return n;

    int j = 1;
    int ncopy = n;
    while((ncopy % 10) == 0)
	{
	    ncopy /= 10;
	    j++;
	}

    int m = n;
    m = n / (int)pow(10,j);
    
    int last = n % (int)pow(10,j);

    int i = 1;
    ncopy = n;
    while((ncopy/= 10) >= pow(10,j))
	i++;

    if(n / pow(10,j-1) < 10)
	return n;

    m += pow(10,i)*(last);

    return m;
}

