#include <string>
#include <vector>
#include <set>
#include <iostream>
#include <fstream>
using namespace std;

int main(){
	
	filebuf ifb;
	ifb.open ("A-large.in",ios::in);
	//ifb.open ("A-test.in",ios::in);
	istream min(&ifb);

	filebuf ofb;
	ofb.open ("A-large.out.txt",ios::out);
	//ofb.open ("A-large.out.txt",ios::out);
	ostream mout(&ofb);

	int i;
	int l, d, n;
	min >> l >> d >> n;
	vector<string> token(d);
	for(i = 0; i < d; i++){
		min >> token[i];
	}
	for(i = 0; i < n; i++){
		int j, k;
		//first deal with each word
		string line;
		min >> line;
		vector< set<char> > cas(l, set<char>());
		int curr_pos = 0;
		bool in_bracket = false;
		for(j = 0; j < line.size(); j++){
			if(line[j] == ')'){
				curr_pos++;
				in_bracket = false;
			}
			else if (line[j] == '(') {
				in_bracket = true;
			}
			else {
				if (in_bracket == false) {
					cas[curr_pos].insert(line[j]);
					curr_pos++;
				}
				else {//in a brace
					cas[curr_pos].insert(line[j]);
				}
			}
		}//for each character
// 		for(j = 0; j < l; j++){
// 			mout << j << " characters :";
// 			for(set<char>::iterator it = cas[j].begin(); it != cas[j].end(); it++){
// 				mout << " " << *it;
// 			}
// 			mout << endl;
// 		}
		int match = 0;
		for(k = 0; k < d; k++){
// 			mout << "token: " << token[k] << endl;
			for(j = 0; j < l; j++){
				if (cas[j].count(token[k][j]) == 0)
					break;
// 				else
// 					mout << "find " << token[k][j] << " at " << j << endl;
			}
			if(j == l)
				match++;
		}//for each token
		mout << "Case #" << i+1 << ": " << match << endl;
	}//for each case
	ifb.close();
	ofb.close();
	return 0;
}
