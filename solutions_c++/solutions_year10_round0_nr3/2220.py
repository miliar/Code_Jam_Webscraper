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

int r, k, n;
long long int cash = 0;


int main(int argc, char *argv[])
{
	int testcases;
	cin >> testcases;
	 
	for (int caseId = 1; caseId <=testcases; caseId++)
	{
		cash = 0;
		cin >> r >> k >> n;
		int groups[n];
		for (int i = 0; i < n; i++){
			cin >> groups[i];
		}
		
		int pointer = 0;
		for (int j = 0; j < r; j++){
			int in = 0;
			int tempPoint = pointer;
			while (in < k){
				in += groups[tempPoint];
				if (in > k) break;
				cash += groups[tempPoint];
				++tempPoint;
				if (tempPoint == n) tempPoint = 0;
				if (tempPoint == pointer) break;
			}
			pointer = tempPoint;
		}
		
		cout << "Case #" << caseId << ": " << cash << "\n";
	}
}
