#define FILENAME "A-large.in"

#include <fstream>
#include <iostream>
#include <vector>
#include <string>

using namespace std;
int L,D,N;
int TestCase(string &str, vector <string> &vec);
bool DoesItContain(string &str, char ch);
bool DoesItMatch(string &str, string &str2);
void parseString(string &str, vector <string> &vec);
 int main()
    {
        fstream file_op(FILENAME,ios::in);
	file_op >> L >> D >> N;
	vector <string> cases;
	vector <string> words;
	
	for(int i=0; i<D; i++) {
	  string str;
		file_op >> str;
		words.push_back(str);
	}
	for(int i=0; i<N; i++) {
	  string str;
		file_op >> str;
		cases.push_back(str);
	}
	
	file_op.close();
	
	for(int i=0; i<N; i++) {
	   string strd = cases.at(i);
	   cout << "Case #" << i+1 << ": " << TestCase(strd, words) << endl; 
	}

        return 0;
    }

  int TestCase(string &str, vector <string> &vec) {
    int numOfMatches = 0;
	for(int i=0; i<D; i++) {
		string str2 = vec.at(i);
		if(DoesItMatch(str, str2)) 
			numOfMatches += 1;
	}
	return numOfMatches;
    }

// str is the element of cases -- parantezli falan
// str2 is the element of words -- L uzunlugunda kelimeler
  bool DoesItMatch(string &str, string &str2) {
	vector <string> caseWord;
	parseString(str,caseWord);
	for(int i=0; i<L; i++) {
	  char ch = str2[i];
	   if(!DoesItContain(caseWord.at(i), ch))
		return false;
	}	
	return true;
  }
// returns true if the i`th element of the caseWord contains the character of the element of words
  bool DoesItContain(string &str, char ch) {
	int len = str.length();
	for(int i=0; i<len; i++) {
		if(str[i]==ch)
			return true;
	}	
	return false;
  }

//str is the element of cases -- parantezli falan
//vec is the vector that is the outcome of breaking that str to pieces
  void parseString(string &str, vector <string> &vec) {
	bool inParanthesis = false;
	string str_element = "";
	int len = str.length();
	for(int i=0; i<len; i++) {
	 char ch = str[i];
	 if(!inParanthesis && ch=='(') {
		inParanthesis = true;
		str_element = "";
	 }
	 else if(inParanthesis && ch != ')') {
		str_element += ch;
	 }
	 else if(inParanthesis && ch == ')') {
		inParanthesis = false;
		vec.push_back(str_element);
	 }
	 else {
		str_element = "";
		str_element += ch;
		vec.push_back(str_element);
	  }
	}

  }
