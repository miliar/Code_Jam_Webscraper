#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;
struct Range {
	double cost, left, right;
};

int main(){
	int T;
	cin >> T;
	cout.precision(9);
	for(int caseNum = 1; caseNum <= T; ++caseNum){
		int C, D;
		cin >> C >> D;
		vector<Range> ranges;
		for(int i = 0; i < C; ++i){
			int P, V;
			cin >> P >> V;
			Range range;
			range.left = P - D * (V / 2);
			range.right = P + D * (V / 2);
			range.cost = D * (V / 2);
			if(V % 2 == 0){
				range.left += static_cast<double>(D) / 2;
				range.right -= static_cast<double>(D) / 2;
				range.cost -= static_cast<double>(D) / 2;
			}
			ranges.push_back(range);
		}
		bool merged = true;
		while(merged){
			merged = false;
			for(int i = 0; i < ranges.size() - 1; ++i){
				double overlap = ranges[i].right + D - ranges[i + 1].left;
				if(overlap > 0){
//					cout << "m: " << ranges[i].left << " " << ranges[i].right << "(" << ranges[i].cost << ")"
//						", " << ranges[i + 1].left << " " << ranges[i + 1].right << "(" << ranges[i + 1].cost << ")" << " -> ";
					Range r;
					if(ranges[i].cost + overlap <= ranges[i + 1].cost){
						r.cost = ranges[i + 1].cost;
						r.left = ranges[i].left - overlap;
						r.right = ranges[i + 1].right;
					}else if(ranges[i + 1].cost + overlap <= ranges[i].cost){
						r.cost = ranges[i].cost;
						r.left = ranges[i].left;
						r.right = ranges[i + 1].right + overlap;
					}else if(ranges[i].cost < ranges[i + 1].cost){
						double diff = ranges[i + 1].cost - ranges[i].cost;
						double rest = overlap - diff;
						r.cost = ranges[i + 1].cost + rest / 2;
						r.left = ranges[i].left - diff - rest / 2;
						r.right = ranges[i + 1].right + rest / 2;
					}else{
						double diff = ranges[i].cost - ranges[i + 1].cost;
						double rest = overlap - diff;
						r.cost = ranges[i].cost + rest / 2;
						r.left = ranges[i].left - rest / 2;
						r.right = ranges[i + 1].right + diff + rest / 2;
					}
					ranges[i + 1] = r;
//					cout << r.left << " " << r.right << "(" << r.cost << ")" << endl;
					ranges.erase(ranges.begin() + i);
					merged = true;
					break;
				}
			}
		}
		double answer = 0.0;
		for(int i = 0; i < ranges.size(); ++i){
//			cout << "s: " << ranges[i].cost << endl;
			answer = max(answer, ranges[i].cost);
		}
		cout << "Case #" << caseNum << ": " << answer << endl;
	}
	return 0;
}
