#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)

typedef long long int64;
typedef pair <int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;
const string task = "";

template <class T> T sqr (T x) {return x * x;}

const int nmax = 550;

int s[nmax][nmax];
char a[nmax][nmax];
int n,m,d;

bool check(int i, int j, int k){
	if (k % 2 == 0){
		int up = s[i+k/2][j+k]+s[i][j] - s[i+k/2][j] - s[i][j+k];
		up -= a[i][j] - '0';
		up -= a[i][j + k-1] - '0';
		int down = s[i+k][j+k]+s[i+k/2][j] - s[i+k][j] - s[i+k/2][j+k];
		down -= a[i+k-1][j] - '0';
		down -= a[i+k-1][j + k-1] - '0';
		if (up != down)
			return 0;
		
		int left = s[i+k][j+k/2]+s[i][j] - s[i][j+k/2] - s[i+k][j];
		left -= a[i][j] - '0';
		left -= a[i+k-1][j] - '0';
		int rgt = s[i+k][j+k]+s[i][j+k/2] - s[i][j+k] - s[i+k][j+k/2];
		rgt -= a[i][j+k-1] - '0';
		rgt -= a[i+k-1][j + k-1] - '0';
		if (left != rgt)
			return 0;
		return 1;
	}else{
		int up = s[i+k/2][j+k]+s[i][j] - s[i+k/2][j] - s[i][j+k];
		up -= a[i][j] - '0';
		up -= a[i][j + k-1] - '0';
		int down = s[i+k][j+k]+s[i+k/2+1][j] - s[i+k][j] - s[i+k/2+1][j+k];
		down -= a[i+k-1][j] - '0';
		down -= a[i+k-1][j + k-1] - '0';
		if (up != down)
			return 0;
		
		int left = s[i+k][j+k/2]+s[i][j] - s[i][j+k/2] - s[i+k][j];
		left -= a[i][j] - '0';
		left -= a[i+k-1][j] - '0';
		int rgt = s[i+k][j+k]+s[i][j+k/2+1] - s[i][j+k] - s[i+k][j+k/2+1];
		rgt -= a[i][j+k-1] - '0';
		rgt -= a[i+k-1][j + k-1] - '0';
		if (left != rgt)
			return 0;
		return 1;
		return 0;
	}
}

int solve(){
	cin >> n >> m >> d;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			scanf(" %c", &a[i][j]);
	s[0][0] = 0;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			s[i+1][j+1] = s[i][j+1] + s[i+1][j] - s[i][j] + a[i][j] - '0';
	int res = 0;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			for (int k = 3; i + k <= n && j + k <= m; k++)
				if (check(i, j, k))
					res = max(res, k);
	if (res == 0)
		puts("IMPOSSIBLE");
	else
		cout << res << endl;	

}	        

int main ()
{
	int tst;
	cin >> tst;
	forn(i, tst){
		printf("Case #%d: ", i + 1);
		solve();
	}

	
	return 0;
}
