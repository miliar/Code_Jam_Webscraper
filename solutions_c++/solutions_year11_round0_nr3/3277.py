#include <iostream>
#include <vector>
#include <set>
#include <cmath>

// note the 'trick' is, we use ^ instead of + for addition

using namespace std;

int maxi = -1;
//set<int> max_s;

// this is exponential but ok for small case
void evaluate(const vector<int> &candy, vector<int> sofar) {
	// base case: sofar is as long as candy
	if (candy.size() == sofar.size()) {
		// try adding, see if 0
		int pk[] = {0, 0};
		int pa[] = {0, 0};
		for (int i = 0; i < candy.size(); ++i) {
			pk[ sofar[i] ] ^= candy[i];
			pa[ sofar[i] ] += candy[i];
		}
		
		if (pk[0] == pk[1]) {
			// according to kids calculations, it works.
			if (pa[0] != 0 && pa[1] != 0) {
//				cout << pa[0] << " " << pa[1] << endl;
				int maxi_t = max(pa[0], pa[1]);
				if (maxi_t > maxi) {
					maxi = maxi_t;
				}
			}
		}
		
	} else {
		sofar.push_back(1);
		evaluate(candy, sofar);
		sofar.pop_back();
		sofar.push_back(0);
		evaluate(candy, sofar);
	}
}



int main() 
{
	int cases;
	cin >> cases;
	
	for (int i = 0; i < cases; ++i) {

		maxi = -1;
//		max_s.clear();

		int candies;
		cin >> candies;
		vector<int> candy;
		
		for (int c = 0; c < candies; ++c) {
			int t;
			cin >> t;
			candy.push_back(t);
		}
		
		vector<int> sofar;
		
		sofar.push_back(1);
		evaluate(candy, sofar);
		sofar.pop_back();
		sofar.push_back(0);
		evaluate(candy, sofar);
				
		cout << "Case #" << i+1 << ": ";
		if (maxi == -1) {
			cout << "NO";
		} else {
			cout << maxi;
		}
		cout << endl;

	}
		
}

