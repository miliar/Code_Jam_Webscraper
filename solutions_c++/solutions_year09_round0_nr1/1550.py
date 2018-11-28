#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

struct Exp {
	set<char> cs;

	bool match(char c){
		return cs.find(c) != cs.end();
	}
};

vector<Exp> stringToExp(string s){
	vector<Exp> ret;
	for(int i = 0; i < s.size(); i++){
		Exp e;
		if(s[i] == '('){
			while(i++, s[i] != ')'){
				e.cs.insert(s[i]);
			}
		} else {
			e.cs.insert(s[i]);
		}
		ret.push_back(e);
	}
	return ret;
}

int main(){
	int L, D, N;
	vector<string> dict;
	cin >> L >> D >> N;

	for(int i = 0; i < D ; i++){
		string s;
		cin >> s;
		dict.push_back(s);
	}

	for(int i = 0; i < N; i++){
		string s;
		cin >> s;

		vector<Exp> exp = stringToExp(s);

		int cnt = 0;

		for(int l = 0; l < D; l++){
			bool flag = false;
			for(int j = 0; j < L; j++){
				if(!exp[j].match(dict[l][j])){
					flag = true;
					break;
				}
			}
			if(!flag) cnt++;
		}

		cout << "Case #" << (i + 1) << ": " << cnt << endl;
	}
}
