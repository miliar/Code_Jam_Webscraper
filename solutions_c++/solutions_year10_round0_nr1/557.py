//============================================================================
// Name        : A.cpp
// Author      : Artem A. Khizha
// Description : Problem A from Qualification round. Google Code Jam 2010
//============================================================================

#include <iostream>

using namespace std;

int main() {
    int tnum;
	cin >> tnum;
	for (int ti = 1; ti <= tnum; ti++)    {
	    long n, k;
	    cin >> n >> k;
	    bool state = true;
	    for (int i = 0; i < n; i++)    {
	        state &= (k%2);
	        k /= 2;
	    }
	    if (state)
	        cout << "Case #" << ti << ": ON" << endl;
	    else
	        cout << "Case #" << ti << ": OFF" << endl;
	}
	return 0;
}
