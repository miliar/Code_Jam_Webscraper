#include "iostream"
#include "sstream"
#include "fstream"
#include "vector"
#include "algorithm"
#include "ios"
#include "math.h"
#include "limits"

using namespace std;

ifstream in("A-small-attempt0.in");
ofstream out("out.txt");

struct Point{
	Point(long long x, long long y): x(x), y(y) {}
	long long x;
	long long y;
};

int main(){
	int N = 0;
	in >> N;
	for(int i = 0; i < N; i++){
		long long result = 0;
		long long n, A, B, C, D, x0, y0, M;
		in >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		long long X = x0, Y = y0;
		vector<Point> trees;
		trees.push_back(Point(X, Y));
		for(int i = 1; i < n; i++){
			X = (A*X + B) % M;
			Y = (C*Y + D) % M;
			trees.push_back(Point(X, Y));
		}

		//Process
		for(int i = 0; i < n; i++){
			for(int j = i+1; j < n; j++){
				for(int k = j+1; k < n; k++){
					result += ((trees[i].x + trees[j].x + trees[k].x)%3 == 0) && ((trees[i].y + trees[j].y + trees[k].y)%3 == 0);
				}
			}
		}

		//Output
		out << "Case #" << i+1 << ": " << result << endl;
	}
}