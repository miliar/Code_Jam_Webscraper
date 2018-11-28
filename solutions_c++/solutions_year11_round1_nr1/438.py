//#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

//ifstream cin("A-small-attempt1.in"); ofstream cout("A-small-attempt1.out");
ifstream cin("A-large.in"); ofstream cout("A-large.out");

int main() {
	int T;
	cin >> T;
	for (int t=1; t<=T; t++) {
		cout << "Case #" << t << ": ";
		long long N, PD, PG;
		cin >> N >> PD >> PG;
		if ((PG == 0 && PD!=0) || (PG==100 && PD!=100))
			cout << "Broken" << endl;
		else if (N>(long long)100)
			cout << "Possible" << endl;	
		else {
			bool ok = false;
			for (int i=1; i<=(int)N; i++) {
				if ((PD*i)%100 == 0)
					ok = true;
			}
			if (ok)
				cout << "Possible" << endl;	
			else
				cout << "Broken" << endl;
		}
	}
	return 0;
}
