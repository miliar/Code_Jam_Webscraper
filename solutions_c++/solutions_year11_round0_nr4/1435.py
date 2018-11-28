#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define for0(i,n) for(int i = 0; i < (n); i ++)

int n;

int nums[1005];

int sortedNums[1005];

long factorial(long num) {
	return num == 0 ? 1 : num * factorial(num-1);
}


double avgHits(vector<int> nums, double factor) {
	if (nums.size() <= 1) return 0;
	if (nums.size() == 2) return 2;
	if (factor < 0.0000001) return 1;
	long fac = factorial(nums.size());
	double numHits = 0;
	sort(nums.begin(), nums.end());
	
	vector<int> sortedNums;
	for0(i, nums.size()) sortedNums.push_back(nums[i]);
	do {
		vector<int> children;
		for0(i, nums.size()) if (nums[i] != sortedNums[i]) children.push_back(nums[i]);
		numHits += avgHits(children, factor / fac);
	} while (next_permutation(nums.begin(), nums.end()));
	numHits /= fac;
	return 1 + numHits;
}

int main() {
	int kases; cin >> kases;
	
	for0(kase, kases) {
		cin >> n;
		for0(i,n) cin >> nums[i];
		for0(i,n) sortedNums[i] = nums[i];
		sort(sortedNums, sortedNums+n);
		
		vector<int> xs;
		
		for0(i, n) {
			if (sortedNums[i] != nums[i]) xs.push_back(nums[i]);
		}
		
		cout << "Case #" << (kase+1) << ": ";
		
		cout << xs.size() << ".000000" << endl;
		// printf("%.6f", avgHits(xs, 1));
		// printf("%.6f", avgHits(xs, 1));
		// cout << endl;
	}
}