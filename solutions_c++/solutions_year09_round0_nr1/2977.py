#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

bool match(const string & token,vector<string> & pattern)
{
	size_t i = 0;
	typedef vector<string>::const_iterator iter;
	for (iter it = pattern.begin(); it != pattern.end(); ++it){
		if(it->find(token[i++]) == -1)
			return false;
	}
	return true;
}

int WordsMatchPattern(string & pattern, vector<string> & tokens)
{
	int count = 0;
	typedef vector<string>::const_iterator iter;
	vector<string> pattern_tokens;
	size_t i = 0;
	size_t j = 0;

	while (i != pattern.size())
		if(pattern[i] != '(')
		{
			string s (1, pattern[i++]);
			pattern_tokens.push_back(s);
		}
		else 
		{
			j = pattern.find(")",i++);
			string s (pattern, i, j-i);
			pattern_tokens.push_back(s);
			i = ++j;
		}

	for (iter it = tokens.begin(); it != tokens.end(); ++it)
		if (match((*it), pattern_tokens))
			count++;
	return count;
}

int main(){
	string ifile;
	cout << "enter the filename: ";
	cin >> ifile;

	ifstream infile(ifile.c_str());
	ofstream outfile((ifile.substr(0,ifile.length()-2)+"out").c_str());
	// check that the open succeeded
	if (!infile) {
		cerr << "error: unable to open input file: "
			<< ifile << endl;
		return -1;
	}
	if (!outfile) {
		cerr << "error: unable to create output file: "
			<< ifile.substr(0,ifile.length()-2)+"out" << endl;
		return -1;
	}

	int count = 1;
	int L, D, N;
	infile >> L >> D >> N;
	vector<string> tokens;

	while(D--){
		string token;
		infile >> token;
		tokens.push_back(token);
	}

	while(N--){
		string test_case;
		infile >> test_case;
		outfile << "Case #" << count++ << ": " << WordsMatchPattern(test_case, tokens) << endl;
	}
	infile.close();
	outfile.close();
	return 0;
}