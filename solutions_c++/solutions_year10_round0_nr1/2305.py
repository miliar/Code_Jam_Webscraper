/**
 * Codejam template
 * - daftmutt
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <complex>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <new>
#include <memory>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

int main(int argc, char *argv[])
{
	int testcases;
	int n, k, clicks;
	string out;
	cin >> testcases;
	 
	for (int caseId = 1; caseId <=testcases; caseId++)
	{
		out = "OFF";
		cin >> n >> k;
		clicks = (int) pow(2.0, n);
		if (k != 0){
			++k;
			if (k % clicks == 0) out = "ON";
		}
		cout << "Case #" << caseId << ": " << out << "\n";
	}
}
