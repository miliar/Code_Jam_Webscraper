#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

typedef vector<string> StringVector;

int main() {
	ifstream fin ("A-small-attempt0.in");

	int l, d, n;
	fin >> l;
	fin >> d;
	fin >> n;

	//cout << "reading words" << endl;
	StringVector words;
	string word;
	getline(fin, word);
	for (int i = 0; i < d; i++) {
		getline(fin, word);
		words.push_back(word);
	}

	//cout << "spitting" << words.size() << endl;
	StringVector::iterator it = words.begin();
	while (it != words.end()) {
		//cout << "x" << (string)*it._Myptr << endl;
		++it;
	}

	char thischar;	
	char* charlist = (char*)malloc(l+1);
	for (int testcase = 1; testcase <= n; testcase++) {
		StringVector* caseWords = new StringVector(words);
		for (int letter = 0; letter < l; letter++) {
			fin >> thischar;
			if (thischar == '(') {		
				fin >> thischar;				
				int lencharlist = 0;
				while(thischar != ')') {
					charlist[lencharlist] = thischar;
					lencharlist++;					
					fin >> thischar;
				}
				StringVector::iterator it = caseWords->begin();
				while (it != caseWords->end()) {
					bool fail = true;
					for (int i = 0; i < lencharlist; i++) {
						if (it->c_str()[letter] == charlist[i]) {
							fail = false;
						}
					}
					if (fail) {
						it = caseWords->erase(it);
					} else {
						++it;
					}
				}
			} else {
				StringVector::iterator it = caseWords->begin();
				while (it != caseWords->end()) {
					if (it->c_str()[letter] == thischar) {
						++it;
					} else {
						it = caseWords->erase(it);
					}
				}
			}
		}
		cout << "Case #" << testcase << ": " << caseWords->size() << endl;
	}

	char bah;
	cin >> bah;
}