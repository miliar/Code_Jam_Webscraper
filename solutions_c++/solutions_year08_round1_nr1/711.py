#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>

#define DO(x) cout << #x": " << x << endl

using namespace std;

int main(){
	ifstream ifs("A-small-attempt0.in");
	vector<int> x, y;
	int cases;
	ifs >> cases;
	for(int i = 1; i <= cases; ++i){
		int num,tmp;
		ifs >> num;
		for(int j = 0; j < num; ++j){
			ifs >> tmp;
			x.push_back(tmp);
		}
		for(int j = 0; j < num; ++j){
			ifs >> tmp;
			y.push_back(tmp);
		}
		sort(x.begin(), x.end());
		sort(y.begin(), y.end());
		long long ret=0;
		for(int j = 0; j < num; ++j){
			ret += x[j] * y[num-j-1];
		}
		cout << "Case #" << i << ": " << ret << endl;
		x.clear(); y.clear();
	}
}
