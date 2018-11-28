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
	ifstream fin ("A-large.in");
	ofstream fout ("out.txt");
	int i, t;
	int n, k;
	long j;
	fin >> t;
	for ( i = 0; i < t; i++ ){
		fin >> n >> k;
		cout << n << " " << k << endl;
		j = 1;
		j = j << n;
		cout << j << endl;
		fout << "Case #" << i + 1 << ": ";
		if (k == 0)
			fout << "OFF" << endl;
		else if ((k + 1) % j)
			fout << "OFF" << endl;
		else
			fout << "ON" << endl;
	}
	return 0;
}