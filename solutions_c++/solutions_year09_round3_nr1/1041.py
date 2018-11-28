#include <stdio.h>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

int nstr[100];

void replace(string &str, char c, int n){
	for(int i = 0; i < str.length(); i++)
		if(str[i] == c)
			nstr[i] = n;
}

int populate(string &str){
	int n = 1;
	bool zero = false;
	memset(nstr, -1, sizeof(nstr));
	for(int i = 0; i < str.length(); i++){
		if(nstr[i] != -1)
			continue;
		if(i == 0)
			replace(str, str[i], n++);
		else{
			if(!zero){
				replace(str, str[i], 0);
				zero = true;
			}
			else
				replace(str, str[i], n++);
		}
	}
	return n;
}

__int64 _pow(int x, int y){
	__int64 value = 1;
	while(y--)
		value *= (__int64)x;
	return value;
}

__int64 base_to_dec(int base, int length){
	__int64 value=0;
	for(int i=length-1,pos=0;i>=0;i--,pos++){
		if(nstr[i] > 0)
			value+=(__int64)nstr[i] * _pow(base, pos);
	}
	return value;
}

int main() {
    freopen("A-small.in", "r", stdin);
    freopen("A-small.txt", "w", stdout);

	int T;
	cin >> T;
    for (int t = 1; t <= T; t++) {
		string str;
		cin >> str;
		printf("Case #%d: %I64d\n", t, base_to_dec(populate(str), str.length()));
    }

    return 0;
}
