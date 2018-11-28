#include <iostream>
#include <cstring>
#include <vector>
#include <map>

#define MAX_N 500

using namespace std;

int input[MAX_N];

map<int, vector<int> > sums;
bool inSet[MAX_N];
bool found;

void generateSubsets(int start, int end, vector<int> numbers, int sum) {
	if (sums.find(sum) != sums.end()) {
		for(size_t i = 0; i < numbers.size(); i++) {
			cout << numbers[i] << " ";
		}
		cout << endl;
		
		vector<int> otherSubset = sums[sum];
		for(size_t i = 0; i < otherSubset.size(); i++) {
			cout << otherSubset[i] << " ";
		}
		cout << endl;
		
		found = true;
		return;
	}
	
	if (start == end) {
		sums[sum] = numbers;
	} else {
		if (!found) {
			generateSubsets(start + 1, end, numbers, sum);
		}
		
		if (!found) {
			numbers.push_back(input[start]);
			generateSubsets(start + 1, end, numbers, sum + input[start]);
			numbers.pop_back();
		}
	}
}

/*void bt(int start, int end, int sum) {
	if (sums.find(sum) != sums.end()) {
		for(int i = 0; i < end; i++) {
			if(inSet[i]) cout << numbers[i] << " ";
		}
		cout << endl;
		
		vector<int> otherSubset = sums[sum];
		for(size_t i = 0; i < otherSubset.size(); i++) {
			cout << otherSubset[i] << " ";
		}
		cout << endl;
		
		found = true;
	} else if (start < end) {
		vector<int> subset;
		
		for(int i = 0; i < end; i++) {
			if(inSet[i]) {
				subset.push_back(numbers[i]);
			}
		}
		
		for(int i = start; i < end && !found; i++) {
			if (start == 0) {
				cout << "bt to " << i << endl;
			}
		
			bt(i + 1, end, sum);
			inSet[i] = true;
			bt(i + 1, end, sum + numbers[i]);
			inSet[i] = false;
		}
	}
}*/

int main(void) {
	int t, n;
	
	cin >> t;
	for(int numCase = 1; numCase <= t; numCase++) {
		sums.clear();
		
		cin >> n;
		for(int i = 0; i < n; i++) cin >> input[i];
		
		vector<int> numbers;
		found = false;
		
		cout << "Case #" << numCase << ":" << endl;
		generateSubsets(0, n, numbers, 0);
	}
}
