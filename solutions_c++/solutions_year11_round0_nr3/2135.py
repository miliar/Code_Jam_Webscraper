#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <string>
#include <queue>
#include <cmath>
#include <numeric>
#include <list>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <climits>
#include <set>
#include <memory.h>
#include <memory>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>
#include <map>
#include <cassert>
#include <time.h>
#define _USE_MATH_DEFINES
using namespace std;

typedef long long ll;
typedef pair<int, int> P;
typedef pair<int, P> PP;
typedef pair<string, int > Ps;
typedef vector<int> vec;
typedef vector<vec> mat;
const int INF = 1 << 30;
const double EPS = 1e-9;

int main(){
	
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	
	bool used[1001];
	int nums[1001];
	vector<int> digits[21];
	int counter[21];

	int T;
	int n;
	cin >> T;
	for(int t = 0; t < T; t++){
		cin >>n;
		for(int i = 0; i < n; i++){
			cin >> nums[i];
			used[i] = false;
		}
		memset(counter, 0, sizeof(counter));
		for(int i = 20; i >= 0; i--){
			digits[i].clear();
			for(int j = 0; j < n; j++){
				if(used[j]) continue;
				else{
					if((nums[j] >> i) & 1){
						digits[i].push_back(nums[j]);
						used[j] = true;
					}
				}
			}
		}
		bool ok = true;
		int res = 0;
		for(int i = 20; i >= 0; i--){
			if((digits[i].size() + counter[i]) % 2 != 0){
				ok = false;
				break;
			}
			for(int j = 0; j < (int)digits[i].size(); j++){
				for(int k = i - 1; k >= 0; k--){
					if((digits[i][j] >> k) & 1) {
						counter[k]++;
					}
				}
			}
		}
		cout << "Case #" << t + 1 << ": ";
		if(!ok) cout << "NO" << endl;
		else{
			cout << accumulate(nums, nums + n, 0) - *min_element(nums, nums + n) << endl;
		}
	}
	
	cin.close();
	cout.close();
	
	return 0;
}