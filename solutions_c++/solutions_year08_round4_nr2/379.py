#include <iostream>
#include <vector>

using namespace std;


vector<long long> norm(vector<long long> x) {
	//cout << "NORM "<< x[0] << ","<<x[1]<<","<<x[2]<<endl;
	for(int i=0; i<x.size(); i++) {
		if (x[i] < 0) {
			long long shift = x[i];
			for(int j=0; j<x.size(); j++) x[j] -= shift;
		}
	}
	return x;
}

long long myabs(long long x) { return x<0 ? -x : x; }

int main() {
	int cases;
	cin >> cases;
	for(int c=0; c<cases; c++) {
		long long area, maxX, maxY;
		cin >> maxX >> maxY >> area;

		cout << "Case #"<<(c+1)<< ":";
		bool found = false;
		for(long long x1=0; x1<=maxX; x1++) 
		for(long long y1=0; y1<=maxY; y1++) 
		for(long long x2=-maxX; x2<=maxX; x2++) 
		for(long long y2=-maxY; y2<=maxY; y2++) 
		{
			if (found) break;
			if (x1 - x2 > maxX) continue;
			if (y1 - y2 > maxY) continue;

			long long myAreaDb = myabs(x1 * y2 - x2 * y1);
			if (myAreaDb == area) {
				//cout << "TRY " << x1<<","<<y1<< "  "<<x2<<","<<y2<<endl;
				//cout << "MyAreaDb ="<<myAreaDb<<endl;
				vector<long long> xs(3), ys(3);
				xs[0] = 0; ys[0] = 0;
				xs[1] = x1; ys[1] = y1;
				xs[2] = x2; ys[2] = y2;

				xs = norm(xs);
				ys = norm(ys);
				for(int i=0; i<3; i++) cout << " " << xs[i] << " " << ys[i];
				cout << endl;
				found = true;
			}
		}

		if (!found) cout << " IMPOSSIBLE"<<endl;

	}

}
