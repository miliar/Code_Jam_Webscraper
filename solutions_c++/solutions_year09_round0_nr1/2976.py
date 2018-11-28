//============================================================================
// Name        : CodeJam_A.cpp
// Author      : ranma96@gmail.com
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

#include <sstream>
#include <vector>
#include <iterator>
#include <algorithm>

void read_input_file(string input_file, vector<string>& word_list, vector<string>& case_list ) {
	  ifstream ifs(input_file.c_str());
	  string temp;
	  int L, D, N;

	  int i = 0;
	  while(getline(ifs, temp)) {
		  if (i == 0) {
			sscanf(temp.c_str(), "%d %d %d", &L, &D, &N);
			i++;
			continue;
		  }
		  if (i <= D) {
			  word_list.push_back(temp);
		  } else if ( i > D && i <= (D+N)){
			  case_list.push_back(temp);
		  }
		  i++;
	  }
}

void makeTokenList(vector<string> &token_list, string &word) {
	string token;
	bool isSamePos = false;
	for (int j = 0, n = word.length(); j < n; j++) {
		if (word[j] == '(') {
			isSamePos = true;
			continue;
		}
		if (word[j] == ')') {
			token_list.push_back(token);
		    token = "";
			isSamePos = false;
			continue;
		}
		token += word[j];
		if (!isSamePos) {
			token_list.push_back(token);
		    token = "";
		}
	}
}

int main(int argc, char *argv[]) {
	if (argc != 3) {
		return -1;
	}
	string input_file  = argv[1];
	string result_file = argv[2];

    vector<string> word_list;
    vector<string> case_list;
    read_input_file(input_file, word_list, case_list);

	ofstream result;
	result.open(result_file.c_str());

	int N = case_list.size();
	int D = word_list.size();

	for (int i = 0; i < N; i++) {
		string word    = case_list[i];
		int match_num  = 0;
		vector<string> token_list;
		makeTokenList(token_list, word);

		for (int j = 0; j < D; j++) {
			string word = word_list[j];
			bool find   = true;
			for (int k = 0, n = word.length(); k < n; k++) {
				string token = token_list[k];
				find = find && (token.find(word[k]) != string::npos);
				if (!find) {
					break;
				}
			}
			if (find) match_num++;
		}
		cout   << "Case #" << (i+1) << ": " << match_num << "\n";
		result << "Case #" << (i+1) << ": " << match_num << "\n";
	}
	result.close();
	return 0;
}
