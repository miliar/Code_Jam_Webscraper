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
#include <math.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forab(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)

int main()
{
	int TT[10000];
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
		//forn(m,10000)
		memset(TT,0,sizeof(TT));
		int A,B;
		in >> A;
		in >> B;
		int R = 0;

		printf("For: %d %d\n", A,B);

		forab(j, A, B) {
			int N = (int)(log10((float)j) + 1);
			if (N < 2) continue;
			int target = j;
			forn (k, N) {
				int right = target % 10;
				target /= 10;
				target += (powf(10,N-1)*right);
				if (target <= B && target > j) {
					R++; 
					if (TT[target]) printf(" {%d %d} - %d \n",j,target,TT[target]);
					TT[target] = 1;
				}
			}
		}

		printf("\nResult: %d\n",R);
		out << "Case #" << i+1 << ": " << R << "\n";
	}
	in.close();
	out.close();

	return 0;
}