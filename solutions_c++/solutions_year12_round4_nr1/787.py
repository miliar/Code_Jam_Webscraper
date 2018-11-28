#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

#define For(i, a, b) for (int i = (a); i != b; i++)
#define Rep(i,n) For(i,0,n)
#define debug(x) cout<<#x<<": "<<x<<endl
#define Pb push_back
#define Mp make_pair

template<class T>void show(T a,int n) {Rep(i,n)cout<<a[i]<<' ';cout<<endl;}
template<class T>void show(T a,int n,int m) {Rep(i,n){Rep(j,m)cout<<a[i][j]<<' ';cout<<endl;}}

int N;
long long D, d[10005], l[10005], s[10005];

int main() {
	int T;
	scanf("%d\n", &T);

	Rep(iT, T) {

		scanf("%d", &N);
		Rep(i, N) {
			scanf("%lld%lld", &d[i], &l[i]);
			s[i] = 0LL;
		}
		scanf("%lld", &D);
		d[N] = D;
		bool ret = false;

		s[0] = d[0];
		For(i, 0, N) {
			for (int j = i+1;j < N && d[i]+s[i] >= d[j];j++) {
				long long tmp = min(d[j] - d[i], l[j]);
				s[j] = max(s[j], tmp);
			}
			if (d[i] + s[i] >= D) {
				ret = true;
				break;
			}
		}

		//show(d, N+1);
		//show(s, N);
		//show(l, N);
		
		printf("Case #%d: %s\n", iT+1, (ret?"YES":"NO"));
	}
	return 0;
}
