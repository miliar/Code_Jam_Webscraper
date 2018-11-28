#include<iostream>
using namespace std;
#include<algorithm>
#include<queue>
#include<stack>
#include<functional>
#include<string>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<math.h>
#include<vector>
#include<deque>
#include<list>
#include<set>
#include<map>



int main() {
	//freopen("input.txt", "rt", stdin);
	//freopen("output.txt", "wt", stdout);
	int T, C, D, N, cases = 0;
	cin >> T;
	++T;
	char a, b, c;
	string temp;
	while( -- T ) {
		cin >> C;
		map<string, bool> opposed;
		map<string, char> combine;
		for(int i = 0 ; i < C ; ++i) {
			cin >> a >> b >> c;
			temp = "";
			temp += a;
			temp += b;
			combine[temp] = c;
			reverse(temp.begin(), temp.end());
			combine[temp] = c;
		}
		cin >> D;
		for(int i = 0 ; i < D ; ++i) {
			cin >> a >> b;
			temp = "";
			temp += a;
			temp += b;
			opposed[temp] = true;
			reverse(temp.begin(), temp.end());
			opposed[temp] = true;
		}
		cin >> N;
		string lista = "";
		for(int i = 0 ; i < N ; ++i) {
			cin >> a;
			lista += a;
			if( lista.size() > 1 ) {
				int indx = lista.size() - 2;
				temp = "";
				temp += a;
				temp += lista[indx];
				if( combine.count(temp) ) {
					lista.pop_back();
					lista.back() = combine[temp];
					continue;
				}
				reverse(temp.begin(), temp.end());
				if( combine.count(temp) ) {
					lista.pop_back();
					lista.back() = combine[temp];
					continue;
				}
				for(int j =  0 ; j < (int)lista.size() - 1 ; ++j) {
					temp = "";
					temp += lista[j];
					temp += a;
					if( opposed.count(temp) ) {
						lista.clear();
						break;
					}
					reverse(temp.begin(), temp.end());
					if( opposed.count(temp) ) {
						lista.clear();
						break;
					}
				}
			}
		//	cout << lista << endl;
		}
		if( lista.empty() ) {
			cout << "Case #" << ++cases << ": []" << endl;
			continue;
		}
		cout << "Case #" << ++cases << ": [";
		for(int i = 0 ; i < (int)lista.size() - 1; ++i) {
			cout << lista[i] << ", ";
		}
		cout << lista[lista.size() - 1] << "]" << endl;
	}
	return 0;
}