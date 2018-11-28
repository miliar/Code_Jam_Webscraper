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
#include <limits.h>


#define S(X) ((int)(X).size())
#define FOR(I, N) for (int I=0; I<N;++I)
#define fori(N) FOR(i,N)
#define forj(N) FOR(j,N)
#define fork(N) FOR(k,N)
#define LOOP(N) FOR(_i_, N)
#define P(a,b) make_pair((a),(b))

typedef long long LL;
typedef unsigned long long ULL;

const double eps = 1e-11;
const double pi=acos(-1.0);

template<typename T, typename U> U cast(T arg){
    ostringstream oss;
    oss << arg;
    istringstream iss(oss.str());
    U rv;
    iss >> rv;
    return rv;
}

template <typename T>
T gcd(T a, T b) {
	if (b == 0) return a;
	return gcd(b, a % b);
}

template <typename T>
T lcm(T a, T b) {
	return a * b / gcd(a,b);
}

using namespace std;

int arr[50][50];
int arr2[50][50];

int main(int argc, char * argv[]) 
{
	int testcase; // problem size
	cin >> testcase;

	LOOP(testcase) {
		int N, K;
		cin >> N >> K;

		char c;
		fori(N)forj(N) cin >> c, arr[i][j] = c;
		
		fori(N) {
			int j = N - 1;

			int k = N - 1;
			for(int k = N-1; k>= 0 ; k --) {
				if (arr[i][k] != '.') {
					arr[i][j] = arr[i][k];

					if (j != k) arr[i][k] = '.';
					j--;
				}
			}
			
		}

		bool red = false;
		bool black = false;

		fori(N)forj(N) {
			if (arr[i][j] == 'R') {
				int dx[] = {1, 0, 1, 1};
				int dy[] = {0, 1, -1, 1};

				fork(4) {
					int x = i;
					int y = j;
					int n = 1;
					while(true) {
						x += dx[k];
						y += dy[k];
						if (x >= 0 && x < N && y >= 0 && y < N) {
							if (arr[x][y] == 'R') n ++;
							else break;
						} else break;
					}
					if (n >= K) red = true;
				}
			}

			if (arr[i][j] == 'B') {
				int dx[] = {1, 0, 1, 1};
				int dy[] = {0, 1, -1, 1};

				fork(4) {
					int x = i;
					int y = j;
					int n = 1;
					while(true) {
						x += dx[k];
						y += dy[k];
						if (x >= 0 && x < N && y >= 0 && y < N) {
							if (arr[x][y] == 'B') n ++;
							else break;
						} else break;
					}
					if (n >= K) black = true;
				}
			}

		}


		cout << "Case #" << (_i_ + 1) << ": ";
		if (red && black) cout << "Both";
		else if (!red && !black) cout << "Neither";
		else if (red) cout << "Red";
		else cout << "Blue";
		cout << endl;
	}
	return 0;
}

