#include <iostream>
#include <cmath>
using namespace std;

const double eps = 0.0005;

struct Vertex {
		double x,y;
		Vertex(double x, double y): x(x), y(y) {}
};

double dist(Vertex p1, Vertex p2) {
		return sqrt((p1.x-p2.x)*(p1.x-p2.x)+(p1.y-p2.y)*(p1.y-p2.y));

}

double triangle_area(double a, double b, double c) {
		double p = (a+b+c)/2;
			return sqrt(p*(p-a)*(p-b)*(p-c));

}



int main() {
	int C;
	cin>>C;
	for(int cs=1;cs<=C;cs++) {
		int n, m, a;
		cin>>n>>m>>a;

		printf("Case #%d: ", cs);
		bool found = false;
		for(int x2=0;x2<=n&&!found;x2++) for(int y2=0;y2<=m&&!found;y2++) {
			for(int x3=0;x3<=n&&!found;x3++) for(int y3=0;y3<=m&&!found;y3++) {
				double area = triangle_area(
					dist(Vertex(x2,y2), Vertex(x3,y3)),
					dist(Vertex(0,0), Vertex(x3,y3)),
					dist(Vertex(x2,y2), Vertex(0,0)));
				if(abs(2*area-a)<=eps) {
					found = true;
					printf("%d %d %d %d %d %d\n",
						0,0, x2,y2, x3,y3);
				}
			}
		}

		if(!found) {
			printf("IMPOSSIBLE\n");
		}

	}
	return 0;
}

/*
 * 00  01
 * 10  11
 * 2   21  22  23
 * 3
 * 4
 * 5           53  54  55  56  57  58
*/
