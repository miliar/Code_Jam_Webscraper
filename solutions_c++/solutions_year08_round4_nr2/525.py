#include <iostream>
#include <vector>
#include <map>
using namespace std;
#define fu(i,m,n) for(i64 i=m; i<n; i++)
typedef long long i64;

i64 abs(i64 x) {
	return x<0?-x:x;
}

int main(void) {
	int C;
	cin >> C;
	fu(ts,1,C+1) {
		cout << "Case #" << ts << ":";
		i64 N,M,A;
		cin >> N >> M >> A;
		//cout << N << " " << M << " " << A << endl;
		fu(bx,0,N+1) fu(by,0,M+1) fu(cx,0,N+1) fu(cy,0,M+1) {
			if(abs(bx*cy-cx*by)==A) {
				cout << " 0 0 " << bx << " " << by << " " << cx << " " << cy << endl;
				goto done;
			}
		}
		cout << " IMPOSSIBLE" << endl;
done:;
	}
}
