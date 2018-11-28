/*
 * in the name of god
 *
 *
 *
 *
 *
 *
 *
 *
 */

#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <complex>
#include <ctime>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <utility>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef complex<double> point;
typedef long double ldb;

const int maxN = 1000 + 10;
const int inf  = 1000000000;

int T,n;
int a[maxN],b[maxN];

int main(){

	cin >> T;

	for (int o=1; o<=T; o++){
		
		cin >> n;
		for (int i=1; i<=n; i++)
			cin >> a[i] >> b[i];

		int cur = 0;
		int ans = 0;

		while (true){

			bool f = false;

			for (int i=1; i<=n; i++) if (b[i]<=cur){
				ans++;
				cur+=2;
				a[i] = b[i] = inf;
				f = true;
			}

			if (f)
				continue;

			int pos = -1;

			for (int i=1; i<=n; i++) if (a[i]<=cur){
				if (pos==-1)
					pos = i;
				else if (b[i]>b[pos])
					pos = i;
			}

			if (pos==-1)
				break;

			ans++;
			cur++;
			a[pos] = b[pos]; b[pos] = inf;
		}

		cout << "Case #" << o << ": ";

		if (cur == 2 * n)
			cout << ans << endl;
		else
			cout << "Too Bad" << endl;
	}

	return 0;
}
