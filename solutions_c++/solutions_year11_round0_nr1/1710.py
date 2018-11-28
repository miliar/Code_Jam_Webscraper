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

int getNext(int pos, string c, vector<int> A, vector<string> B){
	for(int i = pos; i < A.size(); i++){
		if(B[i] == c) return A[i];
	}
	return -1;
}

int main(){
	int T, cnt=0;
	cin >> T;
	while(T--){
		cnt++;
		vector<int> A;
		vector<string> B;
		int n;
		cin >> n;
		for(int i = 0; i < n; i++){
			string x;
			int y;
			cin >> x >> y;
			A.push_back(y);
			B.push_back(x);
		}
		int a = 1, b = 1;
		int na = getNext(0,"O",A,B), nb=getNext(0,"B",A,B);
		int pos = 0;
		string t = B[pos];
		int result = 0, push=0;
		while(pos < A.size()){
			t = B[pos];
			push = 0;
			if(a == na){
				if(t == "O"){
					pos++;
					push = 1;
					na = getNext(pos, "O", A, B);
				}
			}
			else if(a < na) a++;
			else a--;
			
			if(b == nb){
				if(push == 0 && t == "B"){
					pos++;
					push = 1;
					nb = getNext(pos, "B", A, B);
				}
			}
			else if(b < nb) b++;
			else b--;
			
			result++;
		}
		
		cout << "Case #" << cnt << ": " << result << endl;
	}
	return 0;
}
