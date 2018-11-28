#include <iostream>
#include <algorithm>
#include <sstream>
#include <cstdio>
#include <vector>
#include <string>


using namespace std;

#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define repd(i,n,m) for(int i=n;i<(int)(m);i++)
#define repvi(v,i) for(vector<int>::iterator i = v.begin(); i < v.end();i++)
#define repvs(v,i) for(vector<string>::iterator i = v.begin(); i < v.end();i++)
int patrikSum(vector<int>& candies) {
	int size = candies.size();
	if (size == 0)
		return 0;
	if (size == 1)
		return candies[0];
	if (size == 2)
		return candies[0] ^ candies[1];
	vector<int> temp(candies.begin() +1, candies.end());
	return (candies[0] ^ patrikSum(temp));
}

int sum(vector<int>& numbers) {
	int size = numbers.size(), total = 0;
	rep(i, size) {
		total += numbers[i];
	}
	return total;
}

int main() {
	freopen("c.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int cases, candies, candy, C, total =0 ;
	cin >> cases;
	repd(nn, 1, cases+1) {
		total = 0;
		cout << "Case #" << nn << ": ";
		cin >> C;
		vector<int> candies;
		rep(i, C) {
			cin >> candy;
			total += candy;
			candies.push_back(candy);
		}
		sort(candies.begin(), candies.end());
		reverse(candies.begin(), candies.end());
		bool printed = false;
		repd(i,1, total) {
			int val = total-1;
			//cout << "Val " << val << endl;
			vector<int> pile1, pile2;
			rep(j, C) {
				int pos = j;
				if (candies[pos] <= val ) {
					pile1.push_back(candies[pos]);
					val -= candies[pos];
				}else 
					pile2.push_back(candies[pos]);

			}
			if (patrikSum(pile1) == patrikSum(pile2) && !pile2.empty() && !pile1.empty()) {
				int sum1 = sum(pile1);
				int sum2 = sum(pile2);
				cout << max(sum1, sum2) << endl;
				printed = true;
				break;
			}	

		}
		if (!printed) {
			cout << "NO" << endl;
		}
	}	
	
	return 0;
}
