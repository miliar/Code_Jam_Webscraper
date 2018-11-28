#include <iostream>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

vector<string> vvc;

void make_vector(string s){
	vvc = vector<string>();

	string at;
	bool par = false;
	char buf[2];
	buf[1] = 0;

	for(int i = 0; i < s.size(); i++){
		if(s[i] == '('){
			at = "";
			par=true;
		} else if(s[i] == ')'){
			vvc.push_back(at);
			at = "";
			par=false;
		} else {
			if(par){
				at = at + s[i];
			} else {
				buf[0] = s[i];
				vvc.push_back(string(buf));
			}
		}
	}
/*
	printf("vector for %s: ", s.c_str());
	for(int i = 0; i < vvc.size(); i++){
		cout << vvc[i] << endl;
	}
	*/

}

bool verify(string & s){
	bool match = true;
	for(int i = 0; i < s.size(); i++){
		bool let = false;

		for(int j = 0; j < vvc[i].size(); j++) if(vvc[i][j] == s[i]) let = true;
		match &= let;
	}
	//if(match) cout << s << " matches" << endl;
	//else cout << s << "do not matche" << endl;

	return match;
}

int main(void){
	int L, D, N;

	cin >> L >> D >> N;
	vector<string> vs;

	for(int i = 0; i < D; i++){
		string s;
		cin >> s;
		vs.push_back(s);
	}
	for(int i = 0; i < N; i++){
		string s;
		cin >> s;
		make_vector(s);
		int qt = 0;
		for(int j = 0; j < vs.size(); j++) qt += verify(vs[j]);

		printf("Case #%d: %d\n",i+1, qt);
	}

	return 0;

}
