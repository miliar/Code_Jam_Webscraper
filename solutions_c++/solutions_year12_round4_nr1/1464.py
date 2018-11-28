#include <assert.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

/*
int ElapsedTime(const vector<int>& vecButtons, int index) {
	return abs(vecButtons[index] - vecButtons[index - 1]);
}
*/

vector<int> d, l;
int dn = 0, endp = 0;

bool IsPossible(int ln, int pln) {
    if (ln <= dn) {
        int min = d[ln] - d[pln]; 
        if (min > l[ln]) min = l[ln];

        int distance = min + d[ln]; 

        if (distance >= endp) {
            return true;
        }

        int j = ln + 1;
        while ((j <= dn) && (d[j] <= distance))
            j++;

        j--;
        for (; j>ln; j--)
        {
            if (IsPossible(j, ln))
                return true;
        }
    }
    return false;
}

int main(int argc, char* argv[]) {
    
	if (argc != 2) {
		cerr << "wrong number of parameter" << endl;
		return -1;
	}

	ifstream inf(argv[1]);
	if (!inf) {
		cerr << "cannot open file " << argv[1] << endl;
		return -1;
	}

	string ln;  
    inf >> ln;

    int number = atoi(ln.c_str());
    
	for (int cases=0; cases<number; cases++) 
    {
        dn = 0;
        endp = 0; 

        inf >> ln; dn = atoi(ln.c_str()); // how many points
        
        d.clear(); l.clear();
        
        d.push_back(0); l.push_back(0);
        for (int k=0; k<dn; k++) {
            int i; 
            inf >> ln; i = atoi(ln.c_str()); d.push_back(i); 
            inf >> ln; i = atoi(ln.c_str()); l.push_back(i);
        }
        inf >> ln; endp = atoi(ln.c_str());
        
        // find solution
        bool possible = IsPossible(1, 0);
        

        if (possible)
            cout << "Case #" << cases+1 << ": " << "YES" << endl;
        else
            cout << "Case #" << cases+1 << ": " << "NO" << endl;
        
	}

	return 0;
}

