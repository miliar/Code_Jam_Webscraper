/**
 * Codejam template
 * - daftmutt
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <complex>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <new>
#include <memory>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

#define FOR(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define FOR2(i, m, n) for((i)=(int) (m);(i)<(int) (n); (i)++
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

using namespace std;

const int MAXN = 50 + 5;

int TC;

int N, K, B, T;
int X[MAXN], V[MAXN], R[MAXN];
int i, j;

int main()
{
	
	cin >> TC;
	 
	for (int C = 1; C <=TC; C++)
	{
		cout << "Case #" << C << ": ";
		memset(X, 0, sizeof(X));
		memset(V, 0, sizeof(V));
		memset(R, 0, sizeof(R));
		
		cin >> N >> K >> B >> T;
		
		FOR(i, N){
			cin >> X[i];
		}
		FOR(i, N){
			cin >> V[i];
		}
		
		int count = 0;
		
		FOR(i, N){
			if (X[i] + V[i] * T >= B){
				++count;
				R[i] = 1;
			}
		}
		
		if (count < K) cout << "IMPOSSIBLE";
		else {
			int switches = 0;
			count = 0;
			for (i = N - 1; i >= 0; i--){
				if (R[i] == 1){
					for (j = i + 1; j < N; j++){
						if (R[j] == 0) ++switches;
					}
					++count;
					if (count == K) break;
				}
			}
			cout << switches;
		}
		cout << "\n";
	}
}
