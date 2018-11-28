#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <set>

typedef unsigned long long int lint;
using namespace std;

int next(int d){
	if(d == 0) return 2;
	return d+1;
}
char itoc(int c){
	if(0 <= c && c <= 9) return c + '0';
	return c - 10 + 'a';
}
int ctoi(char c){
	if('0' <= c && c <= '9') return c-'0';
	return c-'a' + 10;
}
lint conv(string code, int len, int d){
	lint ans = 0;
	lint f = 1;
	for(int i=len-1; i>=0; --i){
		ans += ctoi(code[i]) * f;
		f *= d;
	}
	return ans;
}
int main(){
	int n;
	cin >> n;
	for(int cn=1; cn<=n; ++cn){
		char used[256] = {""};
		string str;
		cin >> str;
		int len = str.size();
		char code[64] = "";
		char d = 0;

		code[0] = '1';
		used[str[0]] = '1';
		bool in = false;
		for(int i=1; i<len; ++i){
			if(used[str[i]]){
				code[i] = used[str[i]];
				continue;
			}
			code[i] = itoc(d);
			used[str[i]] = code[i];
			d = next(d);
			in = true;
		}
		if(!in) d = 2;
		lint ans = conv(code, len, d);
//		if(in) ans = 0;

	//	cout << "# " << code << endl;

		cout << "Case #" << cn << ": " << ans << endl;
	}
}
