#include <iostream>
#include <list>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <math.h>
using namespace std;
typedef long long s64;
typedef unsigned long long u64;
typedef long s32;
typedef unsigned long long u32;




int main(int argc, char* argv[])
{
	string line;
	int T;
	cin >> T;
	getline(cin, line);


	for (int t=0; t < T; t++) {

		cout << "Case #" << (t+1) << ": ";

        int A, B;

        cin >> A >> B;

        int total = 0;

        for (int n=A; n <= B; ++n) {

            char strn[10];
            sprintf(strn, "%d", n);
            int lenn = strlen(strn);


            char temp[10];
            map<int, int> found;

            for (int i=0; i <= lenn; ++i) {
                int h = i;
                int t = lenn - i;

                if ((h > 0) && (t > 0)) {
                    memset(temp, 0, sizeof(temp));
                    strncpy(temp, &strn[i], t);
                    strncat(temp, strn, h);

                    int m = 0;
                    sscanf(temp, "%d", &m);

                    if ((m != n) && (m >= A) && (m <= B) && (found[m] == 0)) {
                        found[m] = 1;
                        total++;
                    }
                }
            }

        }

		cout << (total / 2) << endl;
	}


    return 0;
}


