#include <iostream>
#include <fstream>
#include <vector>

using namespace std;
typedef unsigned int uint;
int badAdd(int a, int b) {
	uint r = 0;
	for (int i = 0; i < 32; ++i) {
		uint m = 1 << i;
		if ((a & m && !(b & m)) || (!(a & m) && (b & m))) {
			r |= m;
		}
	}
	return r;
}

int best(vector<int> candies, vector<int> a, vector<int> b)
{
	int d = 0, f = 0, g = 0;
	if (candies.empty()){
		if (a.empty() || b.empty())
			return -1;
		for (uint i = 0; i < a.size(); ++i){
			d = badAdd(d, a[i]);
		}
		for (uint i = 0; i < b.size(); ++i){
			f = badAdd(f, b[i]);
			g += b[i];
		}
		if (f == d)
			return g;
		else
			return -1;
	} else {
		int c = candies[0];

		candies.erase(candies.begin());
		a.push_back(c);
		d = best(candies, a, b);
		a.pop_back();
		b.push_back(c);
		f = best(candies, a, b);
		return max(f, d);
	}

}

int main() {
	fstream file("c.in");
	if (!file.is_open()) {
		cout<<"nofile";
		return 0;
	}
	int numcases = 0;
	file >> numcases;
	for (int i = 0; i < numcases; ++i) {
		int result = 0;
		int numCandies = 0;
		file >> numCandies;
		vector<int> candies;
		for (int x = 0; x < numCandies; ++x) {
			int candy = 0;
			file >> candy;
			candies.push_back(candy);
		}
		result = best(candies, vector<int>(), vector<int>());

		cout << "Case #"<<i+1<<": ";
		if (result == -1)
			cout << "NO";
		else
			cout << result;
		cout << endl;
	}
}