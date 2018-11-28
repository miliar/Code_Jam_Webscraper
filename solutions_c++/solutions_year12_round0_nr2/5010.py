#include <assert.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>

using namespace std;

/*
int ElapsedTime(const vector<int>& vecButtons, int index) {
	return abs(vecButtons[index] - vecButtons[index - 1]);
}
*/



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
    char buf[200] = {0};
    inf.getline(buf, 200);

    int n = atoi(buf);
    
	for (int i=0; i<n; i++) 
    {
        int qn = 0; 
        int nn = 0, s = 0, p = 0;
        string buf;
        inf >> buf; nn = atoi(buf.c_str());
        inf >> buf; s = atoi(buf.c_str());
        inf >> buf; p = atoi(buf.c_str());
        for (int j=0; j<nn; j++) {
            inf >> buf; int points = atoi(buf.c_str());
            int means = points / 3;
            if (means >= p) qn++;
            else if ((means + 1) == p) {
                if (means * 3 < points) {
                    qn++;
                }
                else {
                    if ((s > 0) && (means > 0)) {
                        s--;
                        qn++;
                    }
                }
            }
            else if ((means + 2) == p) {
                int left = points - means * 3;
                if ((s > 0) && (left == 2)) {
                    s--;
                    qn++;
                }
            }
        }

		// find solution
		cout << "Case #" << i+1 << ": " << qn << endl;
	}

	return 0;
}

