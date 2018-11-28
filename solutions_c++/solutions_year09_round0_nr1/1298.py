#include<cstdio>
#include<iostream>
#include<string>
#include<set>
#define FOR(a, b, c) for(int a=b; a<=c; a++)

using namespace std;

set < string > Dict;
int L , D , N;
string input[16];
string str;

void pre(void){
	FOR(i, 1, D){
			string str;
			cin >> str;
			FOR(j, 1, L){
				string sstr = str.substr(0, j);
				Dict.insert(sstr);
			}
	}
}

void init(void){
	int l = str.size();
	FOR(i, 1, L){
		input[i] = "";
	}
	int offset = 0;
	FOR(i, 0, l - 1){
		offset++;
		if(str[i] == '('){
			i++;
			while(str[i] != ')'){
				input[offset].push_back(str[i]);
				i++;
			}
		} else{
			input[offset].push_back(str[i]);
		}
	}
}

int process(int i , string current){
	if(i == L + 1) return 1;
	int ret = 0;
	FOR(j, 0, input[i].size() - 1){
		char c = input[i][j];
		string ncurrent = current;
		ncurrent.push_back(c);
		if(Dict.find(ncurrent) != Dict.end()) {
			ret += process(i + 1, ncurrent);
		}
	}
	return ret;
}

int main(void){
	cin >> L >> D >> N;
	pre();
	FOR(i, 1, N){
		cin >> str;
		init();
		int ans = process(1, "");
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}
