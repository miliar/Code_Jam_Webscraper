#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

ifstream IN("A-large.in");
ofstream OUT("A-large.out");

vector< vector<bool> > get_word(int size, string s){
	vector< vector<bool> > word(size, vector<bool>(26, false));
	int p = -1;
	bool open = false;
	for (int i = 0; i < s.size(); i++){
		if (s[i] >= 'a' && s[i] <= 'z'){
			if (!open) p++;
			word[p][s[i] - 'a'] = true;
		}
		else {
			open = !open;
			if (open) p++;
		}
	}
	return word;
}

bool match(const vector< vector<bool> > &word, char *s, int L){
	for (int i = 0; i < L; i++){
		if (!word[i][s[i]-'a']) return false;
	}
	return true;
}


int main(){
	int L, D, N;
	IN >> L >> D >> N;
	char dict[D][L+1];
	IN.get();
	for (int i = 0; i < D; i++){
		IN.getline(dict[i], L+1);
	}
	for (int i = 1; i <= N; i++){
		string pattern;
		IN >> pattern;
		vector< vector<bool> > word = get_word(L, pattern);
		int K = 0;
		for (int j = 0; j < D; j++){
			if (match(word, dict[j], L)) K++;
		}
		OUT << "Case #" << i << ": "<<K<< endl;
	}
}


/*
for (int p = 0; p < L; p++){
			OUT << "(";
			for (int c = 0; c < 26; c ++){
				if (word[p][c]) OUT << (char)('a'+c);
			}
			OUT << ")";
		}
		OUT << endl;
*/
