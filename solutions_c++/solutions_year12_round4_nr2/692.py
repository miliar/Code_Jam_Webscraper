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


int main() {
	int T;
	scanf("%d\n", &T);

	srand(time(NULL));

	int N;
	double W, L, r[16], x[16], y[16];

	Rep(iT, T) {
		scanf("%d%lf%lf", &N, &W, &L);
		Rep(i, N) {
			scanf("%lf", &r[i]);
		}

		int n = 0, cnt = 0;
		while (n < N) {
			x[n] = W * rand() / RAND_MAX;
			y[n] = L * rand() / RAND_MAX;
			bool ok = true;
			Rep(i, n) {
				if ((x[n]-x[i])*(x[n]-x[i])+(y[n]-y[i])*(y[n]-y[i])
						< (r[n]+r[i])*(r[n]+r[i])) {
					ok = false;
					break;
				}
			}
			if (ok) {
				n++;
			} else {
				cnt++;
				if (cnt > 1000) {
					n = 0;
				}
			}
		}

		printf("Case #%d:", iT+1);
		Rep(i, N) {
			printf(" %lf %lf", x[i], y[i]);
		}
		printf("\n");
	}
	return 0;
}
