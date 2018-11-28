#include <map>
#include <set>
#include <cmath>
#include <string>
#include <cstdio>
#include <cstring>
#include <utility>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++){
		int C, D, N;
		map<pair<char, char>, char> Combine;
		map<pair<char, char>, char>::iterator ccc;
		map<pair<char, char>, bool> Oppose;
		map<pair<char, char>, bool>::iterator ccb;
		cin >> C;
		while( C-- ){
			string str;
			cin >> str;
			Combine[make_pair(min(str[0], str[1]), max(str[0], str[1]))] = str[2];
		}
		cin >> D;
		while( D-- ){
			string str;
			cin >> str;
			Oppose[make_pair(min(str[0], str[1]), max(str[0], str[1]))] = true;
		}
		cin >> N;
		string S, A = "";
		cin >> S;
		for (int i = 0; i < N; i++){
			int L = A.length();
			if ( L > 0 ){
				pair<char, char> p = make_pair(min(S[i], A[L - 1]), max(S[i], A[L - 1]));
				ccc = Combine.find(p);
				if( ccc != Combine.end() ){
					A[L - 1] = (*ccc).second;
					continue;
				}
			}
			bool flush = false;
			for (int j = 0; j < L; j++){
				pair<char, char> P = make_pair(min(A[j], S[i]), max(A[j], S[i]));
				ccb = Oppose.find(P);
				if( ccb != Oppose.end() ){
					flush = true;
					break;
				}
			}
			if( !flush )
				A += S[i];
			else
				A = "";
		}
		cout << "Case #" << t << ": [";
		int L = A.length();
		for (int i = 0; i < L; i++){
			cout << A[i];
			if( i < L - 1 )
				cout << ", ";
		}
		cout << "]\n";
	}
	return 0;
}
