#include <iostream>
using namespace std;
int main(void) {
	int N,n,A,B,C,D,x0,y0,M;
	cin >> N;
	for (int testcase=1;testcase<=N;testcase++) {
		int r=0;
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		int x[n],y[n];
		x[0] = x0;
		y[0] = y0;
		for (int i=1;i<n;i++) {
			x[i] = (x0 = ((long long)A*x0+B)%M)%3;
			y[i] = (y0 = ((long long)C*y0+D)%M)%3;
		}
		for (int i=0;i<n;i++) {
			for (int j=i+1;j<n;j++) {
				for (int k=j+1;k<n;k++) {
					if ((x[i]+x[j]+x[k])%3==0 && (y[i]+y[j]+y[k])%3==0) {
						r++;
					}
				}
			}
		}
		cout << "Case #" << testcase << ": " << r << endl;
	}
}
