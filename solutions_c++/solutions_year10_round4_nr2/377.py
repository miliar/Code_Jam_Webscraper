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
#include <queue> 
#include <cstring> 
using namespace std;

int P;
long long F[5000][20];
long long C[10000], M[10000], l, r;

long long solve(int k, int p){
	if (F[k][p] != -1) return F[k][p];
	if (r-l == 1){
		long long q = max(M[l-1], M[r-1]);
		if (q <= p) return F[k][p] = 0;
		if (q == p + 1) return F[k][p] = C[k];
		return F[k][p] = 1LL<<30;
	}else{
		long long tl = l, tr = r;
		long long mid = (tl+tr)/2;
		l = tl, r = mid;
		long long X1 = solve(k*2, p+1);
		l = mid+1, r = tr;
		long long X2 = solve(k*2+1, p+1) + C[k];
		l = tl, r = mid;
		long long Y1 = solve(k*2, p);
		l = mid+1, r = tr;
		long long Y2 = solve(k*2+1, p);
		l = tl, r = tr;
		return F[k][p] = min(X1+X2, Y1+Y2);
	}
}

int main(){
	int T, ca=0;
	scanf("%d", &T);
	while (T--){
		printf("Case #%d: ", ++ca);
		scanf("%d", &P);
		for (int i = 0 ; i < (1<<P); ++i)
			scanf("%lld", M+i), M[i] = P-M[i];
		memset(C, 0, sizeof(C));
		for (int i = P-1; i >= 0 ; --i)
			for (int j = 0 ; j < (1<<i); ++j)
				scanf("%lld", C+(1<<i)+j);
		memset(F, -1, sizeof(F));
		l = 1, r = 1<<P;
		printf("%lld\n", solve(1, 0));
	}
	return 0;
}
