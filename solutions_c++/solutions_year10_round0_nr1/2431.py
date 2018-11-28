/*
 *	E-Mail : khaled.samy@fci-cu.edu.eg
 *	TopCoder Handle : Khaled91
 *	Another buggy code by Khaled Samy ;)
 */
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
using namespace std;
#define PB                      push_back
#define MP                      make_pair
#define ALL(v)                  v.begin(),v.end()
#define CLR(v, d)               memset(v, d, sizeof(v))
#define loop(i,n) 		        for(int i=0;i<(int)n;i++)
#define loop2(i,n,m)            for(int i=n;i<(int)(m);i++)

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef long long ll;
typedef stringstream SS;
typedef pair<int, int> pii;
typedef vector<pii> vpii;

const int OO = (int) 1e9;
const double PI = 2 * acos(0);
const double EPS = 1e-9;

int dcmp(double a, double b) {
	return fabs(a - b) <= EPS ? 0 : a > b ? 1 : 2;
}

int DI[] = { -1, 0, 1, 0, 1, -1, -1, 1 };
int DJ[] = { 0, 1, 0, -1, 1, -1, 1, -1 };

int main() {
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int T, N, K;
	cin >> T;

	loop2(i,1,T+1) {
		cin >> N >> K;
		cout << "Case #" << i << ": ";
		char *res;
		res = itoa(K, res, 2);
		bool f = true;
		int j = strlen(res);
		if (j < N)
			f = false;
		else {
			for (int x = 0; x < N; x++)
				if (res[j - x - 1] == '0')
					f = false;
		}
		if (f)
			cout << "ON\n";
		else
			cout << "OFF\n";
	}

	return 0;
}
