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

bool check(stack<char> &A, map<string, bool> &D){
	vector<int> B;
	while(!A.empty()){
		B.push_back(A.top());
		A.pop();
	}
	
	for(int i = 0; i < B.size(); i++){
		for(int j = i+1; j < B.size(); j++){
			string s1 = "", s2 = "";
			s1 += B[i];
			s1 += B[j];
			s2 += B[j];
			s2 += B[i];
			if(D[s1] || D[s2]) return true;
		}
	}
	return false;
}

string solve(){
	int C;
	map<string, char> Combine;
	cin >> C;
	for(int i = 0; i < C; i++){
		string s;
		cin >> s;
		string str1 = "";
		str1+=s[1];
		str1+=s[0];
		string str2 = "";
		str2+=s[0];
		str2+=s[1];
		Combine[str1] = Combine[str2] = s[2];
	}
	
	int D;
	cin >> D;
	map<string, bool> Delete;
	for(int i = 0; i < D; i++){
		string s;
		cin >> s;
		string s2 = "";
		s2 += s[1];
		s2 += s[0];
		Delete[s] = Delete[s2] = true;
	}
	
	int N;
	cin >> N;
	stack<char> A;
	for(int i = 0; i < N; i++){
		char c;
		cin >> c;
		A.push(c);
		bool loop = 1, ok=0;
		while(loop){
			loop = 0;
			if(A.size() >= 2){
				stack<char> tmp = A;
				string s = "";
				s += A.top();
				A.pop();
				s += A.top();
				A.pop();
				if(Combine[s] != 0){
					A.push(Combine[s]);
					loop = 1;
					ok = 1;
				}
				else{
					A.push(s[1]);
					A.push(s[0]);
				}
				
				if(ok == 0 && check(tmp, Delete)){
					A = stack<char>();
				}
			}
		}
	}
	
	string result = "]";
	while(!A.empty()){
		result += A.top();
		A.pop();
		if(!A.empty()) result += " ,";
	}
	result += "[";
	reverse(result.begin(), result.end());

	return result;
}

int main(){
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ": " << solve() << endl;
	}
	return 0;
}
