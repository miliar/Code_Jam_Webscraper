#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cctype>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>

using namespace std;

#define MAX_CHARS 200
#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forab(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)

int main()
{
	ifstream in("C:\\input.txt");
	ofstream out("C:\\output.txt");

	if (!in)  {
		cout << "C' file" << endl;
		return 0;
	}
	if (!out) {
		cout << "c' file" << endl;
		return 0;
	}

	int n = 0;
	in >> n;
	forn(i, n) {
		int N, S, p;
		in >> N;
		in >> S;
		in >> p;
		int R = 0;

		printf("For: %d %d %d\n", N, S, p);

		forn(j, N) {
			int t;
			in >> t;
			printf("===This is : %d ",t);
			printf(" %f %f %f ",(((float)p)-1),((float)t) / 3.0 ,(((float)p)-1.5)   );
			if (((float)t / 3.0) > ((float)p-1)) {
				R++;
				printf(" = Not Surprising Point! \n");
				
			} else if (((float)t) / 3.0 >   ((((float)p)-1.5) >= 0 ? (((float)p)-1.5) : 0)  ) {
				if (S > 0) {
					S--;
					R++;
					printf(" = Surprising Point! \n");
				} else {
					printf(" = Surprising Point! But Not Accepted \n");
				}
			} else {
				printf(" = Not Accepted \n");
			}
		}

		printf("Result: %d\n",R);

		out << "Case #" << i+1 << ": " << R << "\n";
	}
	in.close();
	out.close();

	return 0;
}