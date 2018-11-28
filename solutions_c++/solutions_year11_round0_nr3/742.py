#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <numeric>

using namespace std;

int solve( vector<int>& candies) 
{
	int ret = 0;
	for (int i = 0; i < candies.size(); ++i)
	{
		ret ^= candies[i];
	}
	if (ret != 0) {
		return -1;
	}
	sort(candies.begin(), candies.end());
	ret = accumulate(++candies.begin(), candies.end(), 0);
	return ret;
}

int main(int argc, char* argv[]) {
	int numOfCases;
	int curCase = 1;
	cin >> numOfCases;
	for (;curCase <= numOfCases; ++curCase) {
		int numOfSeq;
		cin >>numOfSeq;
		vector<int> candies;
		for (int i = 0; i < numOfSeq; ++i) {
			int candy;
			cin >> candy;
			candies.push_back(candy);
		} // for (int i = 0; i < numOfSeq; ++i)
		int result = solve(candies);
		if (result >= 0) {
			cout << "Case #" <<curCase << ": " << result <<endl;
		}
		else { 
			cout << "Case #" <<curCase << ": " << "NO" <<endl;
		}
	}
}