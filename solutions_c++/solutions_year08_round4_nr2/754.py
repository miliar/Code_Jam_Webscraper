#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <fstream>

using namespace std;

int main() {
	freopen("B-small.in","rt",stdin);
	freopen("B-small.out", "wt", stdout);
	int C,N,M,A;
	cin>>C;
	int x1,y1,x2,y2,x3,y3;
	for(int i = 1; i <= C; i++) {
		cin>>N>>M>>A;
		x1 = 0;
		y1 = 0;
		for(x2 = 0; x2 <= N;x2++) for(y2 = 0; y2 <= M; y2++)
			for(x3 = 0; x3 <= N; x3++) for(y3 = 0; y3 <= M; y3++) {
				int ji = x2*x3 + y2*y3;
				double a = sqrt(1.0 * x2 * x2 + y2*y2);
				double b = sqrt(1.0 * x3 * x3 + y3*y3);
				double c = 1.0*ji/a/b;
				double area = a*b*sqrt(1.0-c*c);
				if(abs(area-A) < 0.000000001){
					cout<<"Case #"<<i<<": "<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<" "<<x3<<" "<<y3<<" "<<endl;
					goto mark;
				}

			}
		cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
mark:;
	}
	return 0;
}