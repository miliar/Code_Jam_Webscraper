#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
	ifstream in("B-large.in");
	ofstream out("output.txt");	
	int T;
	in >> T;
	for (int k=0; k<T; k++) {
		int N, S, p;
		in >> N >> S >> p;
		vector<int> t(N);
		for(int i=0; i<N; i++)
			in >> t[i];		

		int c = 0;
		for (int i=0; i<N; i++) {
			if (t[i] >= p) {
				if (t[i] >= 3*p-2) c++;
				else if ((S > 0) && (t[i] >= 3*p-4)) {
					c++;
					S--;
				}
			}
		}

		//cout << "Case #" << (k+1) << ": " << c << endl;
		out << "Case #" << (k+1) << ": " << c << endl;
	}

	in.close();
	out.close();
	return 0;
}



