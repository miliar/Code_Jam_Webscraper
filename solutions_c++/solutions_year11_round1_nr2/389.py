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

void show(vector<string> A){
	cout << "------show-------" << endl;
	for(int i = 0; i < A.size(); i++){
		cout << A[i] << " ";
	}
	cout << endl;
	cout << "------end-------" << endl;
}

string getRes(vector<string> D, string list){
	int max_v = -1;
	string res = "";
	for(int i = 0; i < D.size(); i++){
		string choose = D[i];
		int n = choose.size();
		
		vector<string> A;
		for(int j = 0; j < D.size(); j++){
			if(D[j].size() == n) A.push_back(D[j]);
		}
		int B[26] = {};
		for(int j = 0; j < A.size(); j++){
			for(int k = 0; k < A[j].size(); k++){
				B[A[j][k]-'a'] += 1;
			}
		}
		
		int C[26] = {};
		for(int j = 0; j < choose.size(); j++){
			C[choose[j]-'a']++;
		}
		
		int v = 0;
		for(int j = 0; j < list.size(); j++){
			if(B[list[j]-'a'] > 0){
				if(C[list[j]-'a'] > 0){
					vector<string> tmp;
					for(int k = 0; k < A.size(); k++){
						bool ok = true;
						for(int l = 0; l < A[k].size(); l++){
							if(choose[l] == list[j]){
								if(A[k][l] == list[j]);
								else ok = false;
							}
							else if(A[k][l] == list[j]) ok = false;
						}
						if(ok) tmp.push_back(A[k]);
					}
					A = tmp;
					fill(B, B+26, 0);
					for(int k = 0; k < A.size(); k++){
						for(int l = 0; l < A[k].size(); l++){
							B[A[k][l]-'a'] += 1;
						}
					}
				}
				else{
					v++;
					vector<string> tmp;
					for(int k = 0; k < A.size(); k++){
						bool ok = true;
						for(int l = 0; l < A[k].size(); l++){
							if(A[k][l] == list[j]) ok = false;
						}
						if(ok) tmp.push_back(A[k]);
					}
					A = tmp;
					fill(B, B+26, 0);
					for(int k = 0; k < A.size(); k++){
						for(int l = 0; l < A[k].size(); l++){
							B[A[k][l]-'a'] += 1;
						}
					}
				}
			}
		}
		if(max_v < v){
			max_v = v;
			res = D[i];
		}
	}
	return res;
}

string solve(vector<string> D, vector<string> L){
	string result = "";
	for(int i = 0; i < L.size(); i++){
		result += getRes(D, L[i]);
		if(i != L.size()-1) result += " ";
	}
	return result;
}

int main(){
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++){
		int n, m;
		cin >> n >> m;
		vector<string> D;
		for(int j = 0; j < n; j++){
			string str;
			cin >> str;
			D.push_back(str);
		}
		vector<string> L;
		for(int j = 0; j < m; j++){
			string str;
			cin >> str;
			L.push_back(str);
		}
		cout << "Case #" << i << ": " << solve(D, L) << endl;
	}
	return 0;
}
