#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int solve(vector<int> input, int N, int S, int p){
	int n = 0;
	sort(input.begin(), input.end());
	reverse(input.begin(), input.end());
	int min = (p == 0) ? (0) : (3 * p - 2);
	int minmin;
	if(p == 0)
		minmin = 0;
	else if(p == 1)
		minmin = 1;
	else
		minmin = (3 * p - 4);
	int i;
	for(i = 0; i < N && input[i] >= min; ++i) ++n;
	for(; i < N && S > 0 && input[i] >= minmin; ++i, --S) ++n; 
	return n;
}

int main(){
	ifstream in("B-large.in");
	ofstream out("B-large.out");
	int T, N, S, p, x;
	in >> T;
	for(int i = 1; i <= T; ++i){
		vector<int> input;
		in >> N >> S >> p;
		for(int j = 0; j < N; ++j){
			in >> x;
			input.push_back(x); 
		}
	 	int ret = solve(input, N, S, p);
		out << "Case #" << i << ": " << ret << endl;
	}
	return 0;
}
