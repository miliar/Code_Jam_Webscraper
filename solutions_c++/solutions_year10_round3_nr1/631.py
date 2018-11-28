#include "stdio.h"
#include "math.h"
#include "map"
#include "string"
#include "vector"
#include "algorithm"
#include "float.h"


struct Cable {
	int a, b;
	Cable(int a_, int b_) {
		a = a_;
		b = b_;
	}

	bool operator<(const Cable &other) {
		return a < other.a;
	}
};

int main() {
	

	freopen("inputA.in", "r", stdin);
	//freopen("outsmall.txt", "w", stdout);
	freopen("outlarge.txt", "w", stdout);
	int numCases;
	scanf("%d", &numCases);
	for(int caseNum=0; caseNum<numCases; ++caseNum) {
		int n;
		scanf("%d", &n);

		std::vector<Cable> wires;

		for(int i=0; i<n; ++i) {
			int a, b;
			scanf("%d %d", &a, &b);
			wires.push_back(Cable(a,b));
		}

		std::sort(wires.begin(), wires.end());

		int crossings = 0;
		for(int i=0; i<n; ++i) {
			for(int j=i+1; j<n; ++j) {
				if(wires[i].b > wires[j].b) ++crossings;
			}
		}

		printf("Case #%d: %d\n", caseNum + 1, crossings);

	}
	return 0;
}

