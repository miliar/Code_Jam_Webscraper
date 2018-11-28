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
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> pii;

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


int main() {
	//freopen("input.txt", "rt", stdin);
	//freopen("output.txt", "wt", stdout);

	int N;
	scanf("%d", &N);
	For(test, 1, N) {
		int P, K, L;
		int64 result = 0;
		bool possible = true;
		scanf("%d %d %d", &P, &K, &L);

		//printf("DEBUG: %d %d %d\n", P, K, L);

		vi feq(L);
		vi keys(K);

		Rep(i, K)
		{
			keys[i] = 0;
		}
		
		Rep(i, L)
		{
			int tmp;
			scanf("%d", &tmp);
			feq[i] = tmp;
		}
		
		sort(All(feq));

		for (int i((L)-1); i >= 0; --i)
		{
			int minFeq = 100000;
			int keySelected = -1;
			Rep(j, K)
			{
				if (keys[j] < minFeq)
				{
					if(keys[j] < P)
					{
						keySelected = j;
						minFeq = keys[j];
					}
				}
			}

			if(keySelected != -1)
			{
				keys[keySelected]++;
				result += feq[i]*keys[keySelected];
				possible = true;
			}
			else
			{
				possible = false;
				break;
			}			
		}

		if(possible)
			printf("Case #%d: %lld\n", test, result);
		else
			printf("Case #%d: IMPOSSIBLE\n", test);
	}

	exit(0);
}
