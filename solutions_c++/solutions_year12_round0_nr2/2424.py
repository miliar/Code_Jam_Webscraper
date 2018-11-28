#include <iostream>
#include <list>
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <algorithm>
using namespace std;


int main(int argc, char* argv[])
{
	string line;
	int T;
	cin >> T;
	getline(cin, line);


	for (int t=0; t < T; t++) {
		cout << "Case #" << (t+1) << ": ";

        int N, S, p;
        int totals[100];

        cin >> N >> S >> p;


        for (int i=0; i < N; ++i) {
            cin >> totals[i];
        }


        vector<int> possible;
        vector<int> surprising;


        for (int i=p; i <= 10; ++i) {
            for (int j=(i-2); j <= (i + 2); ++j) {
                for (int k=(i-2); k <= (i+2); ++k) {

                    if ((j >= 0) && (j <= 10) && (k >= 0) && (k <= 10)) {

                        if ((abs(i-j) == 2) || (abs(i-k) == 2) || (abs(j-k) == 2)) {
                            surprising.push_back(i+j+k);
                        } else {
                            possible.push_back(i+j+k);
                        }
                    }
                }
            }
        }

        int pc = 0;
        int sc = 0;


        for (int i=0; i < N; ++i) {

            bool found = false;

            for (int j=0; j < possible.size(); ++j) {
                if (totals[i] >= possible[j]) {
                    pc++;
                    found = true;
                    break;
                }
            }

            if (!found) {
                for (int j=0; j < surprising.size(); ++j) {
                    if (totals[i] >= surprising[j] && (sc < S)) {
                        sc++;
                        break;
                    }
                }
            }
        }


        cout << (pc + sc) << endl;

	}


    return 0;
}


