#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<deque>
#include<string>
#include<cctype>
#include<cmath>
#include<sstream>
#include<numeric>
#include<complex>
#include<queue>
using namespace std;

int N, M;

int main(){

	//freopen("1.in", "rt", stdin);
	//freopen("1.out", "wt", stdout);
	freopen("D-small-attempt0.in", "rt", stdin);
	freopen("D-small-attempt0.out", "wt", stdout);
	//freopen("D-large.in", "rt", stdin);
	//freopen("D-large.out", "wt", stdout);

	int tt; cin >> tt;
	for(int t = 0 ; t < tt ; t++){

		cout << "Case #" << t+1 << ":";

		cin >> N >> M;
		int ax, ay, bx, by;
		cin >> ax >> ay >> bx >> by;
		for(int i = 0 ; i < M ; i++){
			int x, y; cin >> x >> y;

			double r0 = hypot(ax-x, ay-y);
			double r1 = hypot(bx-x, by-y);

			double c = hypot(ax-bx, ay-by);

			double CBA = acos((r1*r1+ c*c - r0*r0) / (2*r1*c));
			double CBD = 2*CBA;

			double CAB = acos((r0*r0+ c*c - r1*r1) / (2*r0*c));
			double CAD = 2*CAB;

			double area = CBD*r1*r1 - r1*r1*sin(CBD) + CAD*r0*r0 - r0*r0*sin(CAD);
       		area /= 2;

 			printf(" %.7lf", area);
		}
		printf("\n");

	}

	return 0;
}
