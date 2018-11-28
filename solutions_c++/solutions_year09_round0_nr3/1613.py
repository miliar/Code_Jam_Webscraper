#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

const string dic("welcome to code jam");

int solve(int iod, int ios, string &s){
	int sum = 0;

	if(iod == dic.size()) return 1;

	while(ios < s.size() && iod < s.size()){
		if(dic[iod] == s[ios]){
			sum += solve(iod + 1, ios + 1, s);
		}
		ios++;
	}
	return sum;
}

int main(){
	int t;
	cin >> t;
	string s;
	getline(cin, s);
	for(int i = 0; i < t; i++){
		getline(cin, s);
		cout << "Case #" << (i+1) << ": ";
		cout << setw(4) << setfill('0') << solve(0, 0, s) << endl;
	}
}
