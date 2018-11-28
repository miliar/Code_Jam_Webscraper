#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

struct Line {
	int left;
	int right;
};

struct LineLeftLess : public binary_function<bool, Line, Line> {
	bool operator()(const Line& a, const Line& b) {
		return a.left < b.left;
	}
};

int main() {
	int cases;
	cin >> cases;
	for(int c = 1; c <= cases; c++) {
		int n;
		cin >> n;

		vector<Line> lines(n);
		for(int i = 0; i < n; i++) 
			cin >> lines[i].left >> lines[i].right;

		sort(lines.begin(), lines.end(), LineLeftLess());
		
		int count = 0;
		for(int i = 0; i < n - 1; i++) {
			for(int j = i + 1; j < n; j++) {
				if(lines[i].right > lines[j].right) {
					count++;
				}
			}
		}

		cout << "Case #" << c << ": " << count << endl;
	}
	return 0;
}
