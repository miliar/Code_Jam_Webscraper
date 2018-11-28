//#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <iomanip>
#include <string>
#include <set>
#include <fstream>
using namespace std;
ifstream cin("C-small-attempt0.in");
ofstream cout("C-small.out");

//ifstream cin("C-large.in");
//ofstream cout("C-large.out");
/*long long gcd(long long a, long long b)
{   if (b== 0)
       return a;
    else
       return gcd(b, a % b);
}*/
int main() {
int T;
int N,L,H;
cin >> T;
for (int i=1; i<=T; i++) {
	cin >> N >> L >> H;
	cout << "Case #"<<i<<": ";
	vector<int> inps;
	bool found = false;
	int LCM=1;
	for (int j=0; j<N; j++) { int inp; cin >> inp; inps.push_back(inp); }
		for (int k=L; k<= H; k++) {
		int s=0;
		for (; s<inps.size(); s++) {
			if (inps[s] % k == 0 || k%inps[s] == 0) continue;
			else break;
		}
		if (s==inps.size()) { LCM = k; found = true; break; }
	}
	if (found) cout << LCM; else cout << "NO";
	cout << endl;
}
return 0;
}
