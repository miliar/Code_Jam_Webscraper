#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
#include <utility>
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

const double pi = 2*acos(0.0);

int main() 
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int t;
	int cbutton;
	int hallway, button;
	int distance;
	int currentbutton[2];
	int currenttime[2];
	char aux;

	scanf("%d", &t);
	For(test, 1, t) 
	{
		currentbutton[0] = 1;
		currentbutton[1] = 1;
		Fill (currenttime, 0);
		scanf("%d", &cbutton);
		For(i, 1, cbutton) 
		{
			scanf("%c", &aux);
			scanf("%c", &aux);
			hallway = aux=='O' ? 0 : 1;
			scanf("%d", &button);
			
			distance = abs(button - currentbutton[hallway]) + 1;	// add press button
			if (currenttime[hallway] + distance > currenttime[!hallway])
				currenttime[hallway] += distance;
			else
				currenttime[hallway] = currenttime[!hallway] + 1;
			currentbutton[hallway] = button;
		}

		printf("Case #%d: %d\n", test, currenttime[hallway]);
	}

	fclose (stdin);
	fclose (stdout);

	exit(0);
}
