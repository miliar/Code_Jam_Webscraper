#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


struct line {
	int h1;
	int h2;
	vector<bool> mask;
};

bool sortbyh1(line *a, line *b) {
	return a->h1 < b->h1;
}

int main() {

	int T = 0;
	line ropes[1000];
	line* sortedh1[1000];

	cin >> T;
	
	for (int i = 1; i <= T; i++) {
	
		int N = 0;
		int ret = 0;
		cin >> N;
		
		for (int j = 0; j < N; j++) {
			cin >> ropes[j].h1 >> ropes[j].h2;
			ropes[j].mask.assign(N, false);
			sortedh1[j] = &ropes[j];
		}
		
		sort(sortedh1, sortedh1 + N, sortbyh1);

		
		for (int j = 0; j < N; j++) {
		
			if (sortedh1[j]->h1 > sortedh1[j]->h2) {
			
				for (int k = j-1; k >= 0; k--) {
					if (sortedh1[k]->h2 >= sortedh1[j]->h2 &&
					    !sortedh1[k]->mask[j]) {
						sortedh1[k]->mask[j] = true;
						sortedh1[j]->mask[k] = true;
						ret++;
					}
				}			
			
			}
			else {
				for (int k = j+1; k < N; k++) {
					if (sortedh1[k]->h2 <= sortedh1[j]->h2 &&
					    !sortedh1[k]->mask[j]) {
					    
						sortedh1[k]->mask[j] = true;
						sortedh1[j]->mask[k] = true;					
						ret++;
					}
				}			
			}

		}
		
		cout << "Case #" << i << ": " << ret << endl;
	}

}



