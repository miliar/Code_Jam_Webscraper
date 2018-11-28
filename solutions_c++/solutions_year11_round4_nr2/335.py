#include <iostream>
#include <vector>
#include <cmath>
#include <string>
using namespace std;


void tc(int tcn) {
	int r,c,d;
	cin>>r>>c>>d;
	vector<string> diffs(r);
	for (int i=0;i<r;i++)
		cin>>diffs[i];

	for (int M=10;M>=3;M--) {
		for (int sx = 0; sx + M <= c; sx++) {
			for (int sy = 0; sy + M <= r; sy++) {				
				double cx = sx + (M - 1.0)/2.0;
				double cy = sy + (M - 1.0)/2.0;				
				double wx = 0.0;
				double wy = 0.0;
				for (int i=0;i<M;i++) {
					for (int j=0;j<M;j++) {
						if (((i==0)||(i==(M-1))) &&
							((j==0)||(j==(M-1)))) {
							continue;
						}
						double wt = diffs[j+sy][i+sx] - '0' + d;
						wx += wt * (i+sx-cx);
						wy += wt * (j+sy-cy);
//						cout <<"---" <<  i << " " << j << " " << wx << " " << wy << endl;
					}
				}
				if ((abs(wx) < 0.0001) && (abs(wy) < 0.0001)) {
					cout << "Case #" << tcn << ": " << M << endl;
					return;
				}
			}
		}
	}
	cout << "Case #" << tcn << ": " << "IMPOSSIBLE" << endl;
				
}
int main() {
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
		tc(i+1);

}