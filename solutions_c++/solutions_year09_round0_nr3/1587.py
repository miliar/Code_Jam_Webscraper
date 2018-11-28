#include <iostream>
#include <stdio.h>
#include <map>
#include <vector>
#include <algorithm>
#include <string>


using namespace std;

const string S="welcome to code jam";
const int LL = S.size();

int count(const string &s, int l, int L) {
	int ct=0;
	if (LL-L > s.size()-l) return 0;
	if (L == LL-1){
		for(; l<s.size(); l++) {
			if(s[l]=='m') ct++;
		}
		return ct;
	}
	for(; l< s.size(); l++) {
		if(s[l]==S[L]) {
			ct += count(s, l+1, L+1);
			ct%=10000;
		}
	}
	return ct;
}

main(){
	int N;
	cin >> N;
	string s;
	getline(cin, s);
	for(int n=0; n<N; n++){
		getline(cin, s);
		printf("Case #%d: %04d\n", n+1, count(s,0,0));
	}
}
