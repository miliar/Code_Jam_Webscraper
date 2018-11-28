#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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

typedef vector<int> Vi;
typedef vector<string> Vs;
typedef vector<double> Vd;
typedef pair<int,int> Pii;

#define Mp(x, y) make_pair((x), (y))
#define Pb push_back
#define All(v) (v).begin(), (v).end()

int main()
{
	int cases;
	cin >> cases;
	for (int cas = 0; cas < cases; cas++){
		long long ans = 0;
		long long P, K, L;
		cin>>P>>K>>L;
		long long pad[K];
		for( int i=0; i<K; i++ ){
			pad[i] = 1;
		}

		long long Fr[L+1];
		for( int i=0; i<L; i++ ){
			cin>>Fr[i];
		}

		sort( &Fr[0], &Fr[L], greater<long long>() );

		int c = 0;
		for( int i=0; i<L; i++ ){
			ans += pad[c] * Fr[i];
			++pad[c];
			c = (++c) % K;
		}



		cout << "Case #" << cas + 1 << ": " << ans << "\n";
	}
	return 0;
}
