#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std; 

#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define FOR2(i, a, b) for (int i = (a); i > (b); --i)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

const int INF = 1 << 29;
typedef long long ll;

/*class 
{
private:
	
public:
	
};*/

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=last_bit(n); return res; }

///////////////////////////////////////////////////////////////////////////////////////////////////////////////

ifstream fin("vstup.txt");
//FILE * fout = fopen("vystup.txt", "w");
ofstream fout("vystup.txt");

void solve(int T)
{
	string N;
	fin >> N;

	N = "0" + N;

	//najde kde konci vzostupna cast
	int ind = N.size()-1;
	while (ind && N[ind-1] >= N[ind]) --ind;

	--ind; //na indexe ind je to co sa bude menit
	//najde najblizsie vacsie cislo
	int next = ind+1;
	while (next+1 < N.size() && N[next+1] > N[ind]) ++next;

	swap(N[next], N[ind]);
	sort(N.begin()+ind+1, N.end());
	
	if (N[0] == '0') N = N.substr(1);

	fout << "Case #" << T << ": " << N << endl;
}

int main()
{
	int N;

	fin >> N;
	FOR(step, 0, N)
		solve(step+1);

	return 0;
}
