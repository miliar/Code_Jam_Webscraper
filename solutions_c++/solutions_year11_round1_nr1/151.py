#include <vector>
#include <list>
#include <set>
#include <stack>
#include <map>
#include <string>
#include <algorithm>
#include <numeric>
#include <utility>
#include <iostream>
#include <sstream>
#include <cmath>

using namespace std;


long long N;
int Pd, Pg;

bool solve(){
	cin >> N >> Pd >> Pg;
	if(Pd != 0 && Pg == 0) return false;
	if(Pd == 100 && Pg == 0) return false;
	if(Pd != 100 && Pg == 100) return false;
	if(N < 100) {
		bool fail = true;
		for(int i = 1; i <= N; ++i) {
			if (Pd * i %  100 == 0) {
				fail = false;
				break;
			}
		}
		if (fail) return false;
	}
	return true;
}

int main()
{
	int T;
	cin >> T;
	for(int i = 0;  i < T; ++i) {
		cout << "Case #" << (i+1) << ": " << (solve() ? "Possible" : "Broken") << endl;	
	
	}
	return 0;
}

