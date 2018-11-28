#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
using namespace std;
static const double EPS = 1e-10;
typedef long long ll;

string solve(vector<int> A){
	int n = 0, sum=0, min_v=INT_MAX;
	for(int i = 0; i < A.size(); i++){
		n ^= A[i];
		sum += A[i];
		min_v = min(min_v, A[i]);
	}
	if(n != 0) return "NO";
	sum -= min_v;
	stringstream ss;
	ss << sum;
	return ss.str();
}

int main(){
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		int n;
		cin >> n;
		vector<int> C;
		for(int i = 0; i < n; i++){
			int a;
			cin >> a;
			C.push_back(a);
		}
		cout << "Case #" << t << ": " << solve(C) << endl;
	}
	return 0;
}
