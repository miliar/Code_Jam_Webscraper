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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;
 
#define RP(a,h) for(a=0; a<(h); a++)
#define FR(a,l,h) for(a=(l); a<=(h); a++)
#define GMAX(X, Y) ((X) > (Y) ? (X) : (Y))
#define GMIN(X, Y) ((X) < (Y) ? (X) : (Y))
#define SZ(a) (LL)a.size()
#define ALL(a) a.begin(), a.end()
#define pb push_back
typedef vector <int> VI;
typedef vector <string> VS;
typedef pair<int, int> PII;
#define LL long long

const int INF = 100000000;
const string pattern = "welcome to code jam";
const int MAX = 600;
const int MOD = 10000;

int d[MAX][20];
int leng;

string getstr(int num)
{
	ostringstream oss; oss << num; string str = oss.str();
	while (SZ(str)<4) str = "0"+str;
	return str;
}
 
int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int tc, testcase, i, j;
	char cc[MAX];

	cin >> tc;
	cin.getline(cc, MAX);

	RP(testcase, tc)
	{
		cin.getline(cc, MAX);
		memset(d, 0, sizeof(d));
		leng = strlen(cc);
		d[leng][19]=1;
		for (i=leng-1; i>=0; i--)
		{
			RP(j, 20) d[i][j] = d[i+1][j];
			RP(j, 19) if (cc[i]==pattern[j]) d[i][j] = (d[i][j]+d[i+1][j+1]) % MOD;
		}
		cout << "Case #" << (testcase+1) << ": " << getstr(d[0][0]) << endl;
	}

	return 0;
}
