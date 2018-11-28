#include <functional>
#include <algorithm>
#include <iterator>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <utility>
#include <cstring>
#include <cstdlib>
#include <cstddef>
#include <vector>
#include <bitset>
#include <cstdio>
#include <cctype>
#include <deque>
#include <stack>
#include <queue>
#include <cmath>
#include <ctime>
#include <list>
#include <map>
#include <set>

using namespace std;

#define mp make_pair
#define pb push_back
#define mref mem_fun_ref
#define bid back_inserter
#define all(x) (x).begin(), (x).end()

typedef long long LL;
typedef pair<int,int> pint;
typedef istringstream iss;
typedef ostringstream oss;
template < class T > void OUT(T res) { cout << res << endl; exit(0); }

const double PI = 3.14159265358979323846264;
const int MAXN = 101;
int n;

char mas[MAXN][MAXN];
int played[MAXN];
int wins[MAXN];
double wp[MAXN];
double owp[MAXN];
double oowp[MAXN];
double rpi[MAXN];

void Solve()
{
	cin >> n;
	for (int i = 0; i < n; ++ i)
	{
		for (int j = 0; j < n; ++ j)
		{
			cin >> mas[i][j];
		}
	}

	for (int i = 0; i < n; ++ i)
	{
		played[i] = 0;
		wins[i] = 0;
		for (int j = 0; j < n; ++ j)
		{
			if (mas[i][j] != '.') ++ played[i];
			if (mas[i][j] == '1') ++ wins[i];
		}
		wp[i] = (double) wins[i] / played[i];
	}

	for (int i = 0; i < n; ++ i)
	{
		owp[i] = 0;
		for (int j = 0; j < n; ++ j)
		{
			if (mas[i][j] == '.') continue;
			owp[i] += double (wins[j] - (mas[j][i] == '1')) / (played[j] - 1);
		}
		owp[i] /= played[i];
	}

	for (int i = 0; i < n; ++ i)
	{
		oowp[i] = 0;
		for (int j = 0; j < n; ++ j)
		{
			if (mas[i][j] == '.') continue;
			oowp[i] += owp[j];
		}
		oowp[i] /= played[i];
		rpi[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
	
		printf("%.18lf\n", rpi[i]);

	}


}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int testCnt = 0;
	cin >> testCnt;

	for (int test = 0; test < testCnt; ++ test)
	{
		cout << "Case #" << test + 1 << ":" << endl;
		Solve();
	}

	return 0;
}
