#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <cstring>
using namespace std;


int main() {
	int T;
	cin >> T;
	for (int tt=1; tt<=T; ++tt) {
		int C;
		char A[255][255];
		memset(A, 0, sizeof(A));
		cin >> C; 
		for (int i=0; i<C; ++i) {
			string tmp;
			cin >> tmp;
			A[ tmp[0] ][ tmp[1] ] = tmp[2];
			A[ tmp[1] ][ tmp[0] ] = tmp[2];
		}

		int D;
		vector<char> B[255];
		cin >> D;
		for (int i=0; i<D; ++i) {
			string tmp;
			cin >> tmp;
			B[tmp[0]].push_back(tmp[1]);
			B[tmp[1]].push_back(tmp[0]);
		}

		string test, result="";
		int isSet[255];
		memset(isSet, 0, sizeof(isSet));
		
		int N;
		cin >> N;
		cin >> test;
		for (int i=0; i<test.length(); ++i) {
			if ( result.length() == 0 ) {
				result += test[i];
				isSet[test[i]] ++;
				continue;
			}
			if ( A[test[i]][result[result.length()-1]]!=0 ) {
				isSet[result[result.length()-1]] --;
				result[result.length()-1] = A[test[i]][result[result.length()-1]];
				continue;
			}
			bool flag = false;
			for (size_t j=0; j<B[test[i]].size() && !flag; ++j) {
				if ( isSet[B[test[i]][j]]>0 ) {
					result = "";
					memset(isSet, 0, sizeof(isSet));
					flag = true;
				}
			}
			if ( flag ) continue;
			result += test[i];
			isSet[test[i]] ++;
		}

		
		cout << "Case #" << tt << ": [";
		if ( result.length() > 0 )
			cout << result[0];
		for (int i=1; i<result.length(); ++i)
			cout << ", " << result[i];
		cout << "]" << endl;
	}
	return 0;
}
