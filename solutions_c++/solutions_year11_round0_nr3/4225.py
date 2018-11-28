#include <vector>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <iostream>

using namespace std;

#define SZ(x) ((int)(x).size())
#define MP make_pair
#define PB push_back
#define ALL(x) (x).begin(), (x).end()
#define ZERO(a) memset(a, 0, sizeof(a))
#define FOR(i,a,b) for(int i = (a); i < (b); ++i)
#define FORE(i,a,b) for(int i = (a); i <= (b); ++i)
#define RFOR(i,b,a) for(int i = (b); i >= (a); --i)

typedef long long LL;

typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;

int A[1000];

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large-attempt0.txt", "w", stdout);

	int T, N;
	cin >> T; 
	FORE(cas, 1, T)
	{
		cin >> N;
		int xorVal = 0, minVal = 10000007, sum = 0;
		FOR(i, 0, N) {
			cin >> A[i];
			xorVal ^= A[i];
			if (minVal > A[i]) minVal = A[i];
			sum += A[i];
		}
		if (xorVal == 0)
			cout << "Case #" << cas << ": " << sum - minVal << endl;
		else
			cout << "Case #" << cas << ": " << "NO" << endl;
	}

    return 0;
}