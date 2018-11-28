#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <list>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <fstream>
using namespace std;

int power(int x, int y)
{
    int s = 1;
    for (int i=0; i<y; i++)
        s = s * x;
    return s;    
}

int main()
{
	ifstream cin("A-large.in");
	ofstream cout("a.txt");
	int T, N, K;
	cin >> T;
	

	for(int q = 1; q <= T; q++)
	{
	    bool done = false;
		cin >> N;
		cin >> K;
		int test = power(2, N);
		//cout << "test=" << test << "  K=" << K << endl;
		if ((K+1)%test == 0)
		    {
             cout << "Case #" << q << ": " << "ON" << endl;  		
	        }
	    else 
		    {
             cout << "Case #" << q << ": " << "OFF" << endl;  		
	        }
	}
	return 0;
}
