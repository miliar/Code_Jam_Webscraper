//============================================================================
// Name        : AlienLanguage.cpp
// Author      : Peter
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {

	ifstream infile("A-large.in");
	ofstream outfile("A-large.out");

	int L, D, N;
	infile >> L >> D >> N;

//	cout << L << D << N << endl;

	vector <string> words;
	string s;
	for(int i=0;i<D;i++){
		infile>>s;
		words.push_back(s);
	}
//	sort(words.begin(),words.end());
/*	for(vector<string>::const_iterator iter=words.begin(); iter != words.end(); iter++){
		cout << *iter << endl;
	}*/

	vector <string> cases;

	for(int i=0;i<N;i++){
		infile>>s;
		cases.push_back(s);
	}
/*	for(vector<string>::const_iterator iter=cases.begin(); iter != cases.end(); iter++){
		cout << *iter << endl;
	}*/

	int case_index = 1;
	for(vector<string>::const_iterator iter=cases.begin(); iter != cases.end(); iter++){
		string s_case= *iter;
		vector <string> ca;
		//formulate cases
		for(string::iterator iter_letter=s_case.begin();iter_letter!=s_case.end();iter_letter++){
			if(*iter_letter=='('){
				string letter;
				for(iter_letter++;*iter_letter!=')';iter_letter++)
					letter += *iter_letter;
				ca.push_back(letter);
			}
			else{
				string letter;
				letter.insert(0,1,*iter_letter);
				ca.push_back(letter);
			}
		}
/*		for(vector<string>::const_iterator iter=ca.begin(); iter != ca.end(); iter++){
			cout << *iter << endl;
		}*/

		//check words for cases;
		int fit_count=0;
		for(vector<string>::const_iterator iter=words.begin(); iter != words.end(); iter++){
			const char *word = (*iter).c_str();
			bool isFit = true;
			for(int i=0;i<L;i++){
				if(ca[i].find(word[i])==string::npos){
					isFit = false;
					break;
				}
			}
			if(isFit){
				fit_count++;
			}
		}

		outfile << "Case #" << case_index << ": " << fit_count << endl;
		case_index++;
	}

	infile.close();
	outfile.close();
	return 0;
}
