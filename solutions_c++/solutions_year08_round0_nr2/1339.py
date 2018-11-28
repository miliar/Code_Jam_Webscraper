#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>

// For each i from 0 to n
#define fe(i, n) for(int i = 0; i < n; i++)
// For each i from n to 0 inclusive
#define fd(i, n) for(int i = n; i >= 0; i--)
// Size as an integer
#define sz(n) (int)(n).size()
// For each i from 0 to size of n exclusive
#define fs(i, n) for(int i = 0; i < sz(n); i++)
// Traverse a STL container
#define tr(i, n) for((typeof((n).begin())) i = (n).begin(); i != (n).end(); i++)
// Macro for pointers to the begin and end of a STL container
#define all(n) (n).begin(),(n).end()

using namespace std;

typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<vi> vvi;
typedef vector<ii> vii;

int main()
{
	ifstream fin ("b.in");
	ofstream fout("b.out");
	int Cases;
	fin >> Cases;
	fe(k, Cases)
	{
		fout << "Case #" << k+1 << ": ";
		int T, NA, NB;
		fin >> T >> NA >> NB;
		vi A(1440), B(1440);
		fe(j, NA)
		{
			string a, b;
			fin >> a >> b;
			int c, d, e, f;
			a[2] = ' '; b[2] = ' ';
			istringstream ISS1(a), ISS2(b);
			ISS1 >> c >> d; ISS2 >> e >> f;
			int g = c*60+d, h = e*60+f;
			A[g]++;
			if (h+T < 1440)
				B[h+T]--;
		}
		fe(j, NB)
		{
			string a, b;
			fin >> a >> b;
			int c, d, e, f;
			a[2] = ' '; b[2] = ' ';
			istringstream ISS1(a), ISS2(b);
			ISS1 >> c >> d; ISS2 >> e >> f;
			int g = c*60+d, h = e*60+f;
			B[g]++;
			if (h+T < 1440)
				A[h+T]--;
		}
		int r1 = 0, r2 = 0;
		int c = 0;
		fs(i, A) {
			c += A[i];
			r1 = max (c, r1);
		}
		c = 0;
		fs(i, B) {
			c += B[i];
			r2 = max (c, r2);
		}
		fout << r1 << " " << r2 << endl;
	}
	return 0;
}
