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
#include  <list>
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
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		list<int> l;
		int R, K, N, tmp, ret = 0;
		cin >> R >> K >> N;

		loop(j,N) {
			cin >> tmp;
			l.push_back(tmp);
		}

		while (R--) {
			int sum = 0;
			int count = 0;
			while (sum + l.front() <= K && count < N) {
				sum += l.front();
				l.push_back(l.front());
				l.pop_front();
				count++;
			}
			ret += sum;
		}
		cout << "Case #" << i << ": " << ret << endl;
	}
	return 0;
}
