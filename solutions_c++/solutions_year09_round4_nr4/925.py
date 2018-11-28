#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <math.h>
#include <algorithm>
#define fori(n) for (int i = 0; i < n; i++)
#define forj(n) for (int j = 0; j < n; j++)
#define fork(n) for (int k = 0; k < n; k++)

using namespace std;

int C,N,X,Y,R;
double ans;

double dist(int x1, int y1, int x2, int y2) {
	int dx = x2-x1;
	int dy = y2-y1;
	return sqrt(dx*dx + dy*dy);
}

int main() {
	ifstream in("watering.in");
	FILE* out = fopen("watering.out","w");
	in >> C;
	for (int c = 0; c < C; c++) {
		in >> N;
		if (N == 1) {
			in >> X >> Y >> R;
			ans = R;
		}
		if (N == 2) {
			int X1,Y1,R1;
			in >> X >> Y >> R;
			in >> X1 >> Y1 >> R1;

			if (R1 > R) ans = R1;
			else ans = R;
		}
		if (N == 3) {
			int x[3],y[3],r[3];
			for (int i = 0; i < 3; i++) {
				in >> x[i] >> y[i] >> r[i];
				//cout << x[i] << y[i] << r[i] << endl;
			}

			int maxr = 0;
			maxr = max(max(r[0],r[1]),r[2]);

			double mind = min(
				min(
					dist(x[0],y[0],x[1],y[1])+r[0]+r[1],
					dist(x[1],y[1],x[2],y[2])+r[1]+r[2]
				),
				dist(x[0],y[0],x[2],y[2])+r[0]+r[2]
			);
			mind /= 2;

			//printf("Dist from a to b: %.6f\n",dist(x[0],y[0],x[1],y[1]));

			ans = max(double(maxr),mind);
		}

		printf("Case #%d: %.6f\n",c+1,ans);
		fprintf(out,"Case #%d: %.6f\n",c+1,ans);
	}
	return 0;
}
