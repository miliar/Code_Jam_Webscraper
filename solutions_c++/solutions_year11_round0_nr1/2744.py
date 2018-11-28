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

#define pb push_back
#define mp make_pair
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()
#define f(i,a,b) for(int i=(a);i<(b);++i)
#define fr(i,a,b) for(int i=(a);i>(b);--i)
#define fe(i,a,b) for(int i=(a);i<=(b);++i)
#define fre(i,a,b) for(int i=(a);i>=(b);--i)
string itoa(int i) { stringstream ss; ss<<i; return ss.str(); }
#define same(a,b) (fabs((a)-(b))<0.0000001)
#define even(a) ((a)%2==0) 
#define odd(a)  ((a)%2==1)
#define present(c,x) ((c).find(x) !=(c).end())
#define cpresent(c,x) (find(all(c),x)) 

int main() {
	int T, N, P;
	char R;

	ifstream infile;
	ofstream outfile;
	infile.open("A-large.in");
	outfile.open("A-out-large.in");
	infile >> T;

	fe(t, 1, T) {
		infile >> N;
		int o = 1, b = 1, oa = 0, ba = 0;
		int res = 0, cost;
		f(i, 0, N) {
			infile >> R >> P;
			switch(R) {
			case 'O':
				cost = max(abs(o - P) - oa, 0);
				res += cost + 1;
				o = P;
				ba += cost + 1; oa = 0;
				break;
			case 'B':
				cost = max(abs(b - P) - ba, 0);
				res += cost + 1; b = P; oa += cost + 1; ba = 0;
				break;
			}
		}
		outfile << "Case #" << t << ": " << res << endl;
	}

	return 0;
}