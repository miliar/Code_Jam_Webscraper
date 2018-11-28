#include <fstream>
#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cctype>
#include <stdio.h>
#include <cstdlib>

using namespace std;

ifstream in("1.in");
ofstream out("1.out");

//#define in cin
//#define out cout

int t;
string st;

int main()
{
	in >> t;
	getline(in, st);
	for (int tt = 0; tt < t; tt++) {
		out << "Case #" << tt + 1 << ": ";
		getline(in, st);
		if (!next_permutation(st.begin(), st.end())) {
			int k = 0;
			for (int i = 0; i < st.size(); i++)
				if (st[i] == '0') {
					st[i] = 'x';
					k++;
				}
			sort(st.begin(), st.end());
			out << st[0];
			for (int i = 0; i <= k; i++) out << 0;
			for (int i = 1; i < st.length(); i++) 
				if (st[i] != 'x') out << st[i];
			out << endl;
		}
		else out << st << endl;
	}

	return 0;
}
