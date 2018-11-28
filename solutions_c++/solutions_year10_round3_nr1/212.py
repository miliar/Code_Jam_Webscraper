#include <numeric>
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
#include <cctype>
#include <stdio.h>
#include <cstdlib>
#include <memory.h>

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

int a[1100], b[1100];
int t, n, ans;

bool prov(int b1, int b2, int c1, int c2) {
	return ((b1 < c1 && b2 > c2) || (b2 < c2 && b1 > c1));	
}

int main()            
{
	in >> t;
	for (int tt = 0; tt < t; ++tt) {
		in >> n;
		for (int i = 0; i < n; ++i) in >> a[i] >> b[i];
		ans = 0;
		for (int i = 0; i < n - 1; ++i)
			for (int j = i + 1; j < n; ++j)
				if (prov(a[i], b[i], a[j], b[j]) || prov(a[j], b[j], a[i], b[i])) ans++; 
		out << "Case #" << tt + 1 << ": " << ans << endl;
	}

	return 0;
}
