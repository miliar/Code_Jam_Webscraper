#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

struct tree {
	long long x, y;
};

float myabs(float f){
	if (f < 0) return -f; return f;
}

int main(){
	int N; cin >> N;
	for (int tc = 0; tc < N; tc++){
		long long n, A, B, C, D, x0, y0, M; cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		long long X = x0; int Y = y0;
		vector<tree> trees;
		tree t; t.x = X; t.y = Y;
		trees.push_back(t);
		for (long long i = 1; i < n; i++) {
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			tree t; t.x = X; t.y = Y;
			trees.push_back(t);
		}
		
		int count = 0;
		
		for (unsigned int t1 = 0; t1 < trees.size(); t1++) {
			for (unsigned int t2 = t1 + 1; t2 < trees.size() ; t2++) {
				for (unsigned int t3 = t2 + 1; t3 < trees.size(); t3++) {
					if ((trees[t1].x + trees[t2].x + trees[t3].x) % 3 != 0) continue;
					if ((trees[t1].y + trees[t2].y + trees[t3].y) % 3 != 0) continue;
					count++;
				}
			}
		}
		
		cout << "Case #" << (tc+1) << ": " << count << endl;
	}
	
	return 0;
}