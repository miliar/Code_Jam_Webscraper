#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <cstdio>
#include <map>
#include <set>
#include <sstream>
#include <strstream>
#include <queue>
#include <stack>
#include <set>

using namespace std;

ifstream in("large.in");
ofstream out("large.out");

int main()
{
	long long n,k,mek = 1;
	int test;
	in >> test;
	for (int t = 1; t <= test; t++)
	{
		in >> n >> k;
		if ((k % (mek << n)) == ((mek << n) - 1))
			out << "Case #" << t << ": " << "ON" << endl;
		else
			out << "Case #" << t << ": " << "OFF" << endl;
	}
	return 0;
}