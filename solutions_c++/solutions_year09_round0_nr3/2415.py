//#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>

using namespace std;

typedef vector<string> StringVector;

const char original[20] = "welcome to code jam";
const int ocount = 19;

/*int forkString(char* string, int strlen, int o_start) {
	int win = o_start;
	char winchar;	
	char nextchar;
	bool last = false;
	bool lastfound = false;
	
	winchar = original[win];
	if (win < 20) {
		nextchar = original[win+1];
	} else {
		last = true;
	}
	int maincount = 1;
	int letter_subcount[20];
	letter_subcount
	for(i = 0; i < strlen; i++) {
		if (string[i] == winchar) {
			if (last) lastfound = true;
			letter_subcount++;
		} else if (string[i] == nextchar) {

			letter_subcount = 0;
			win++;
			winchar = original[win];
			if (win < 20) {
				nextchar = original[win+1];
			} else {
				last = true;
			}
		}
	}
	if (lastfound == false) { return 0; } else { return count; }
	for(int i = o_start; i < ocount; i++) {
		
	}
}*/

typedef list<int> intList;
intList* letters[ocount];
int cache[19][503];

int paths(int letterid, int position) {
	if (cache[letterid][position] != -1) { return cache[letterid][position]; }
	if (letterid == ocount - 1) { return 1; }
	int count = 0;
	intList* next = letters[letterid+1];
	intList::iterator it = next->begin();
	while (it != next->end()) {
		if(*it > position) {
			count += paths(letterid+1, *it);
		}
		++it;
	}
	if (count > 10000) {
		count %= 10000;
	}
	return count;
}

int main() {
	ifstream fin ("C-small-attempt0.in");
	ofstream fout ("C-small-attempt0.out");

	int N;
	fin >> N;	
	char line[503];
	fin.getline(line, 503);
	for (int caseNum = 1; caseNum <= N; caseNum++) {
		for (int i = 0; i < ocount; i++) {
			letters[i] = new intList();
		}
		memset( (void *) cache, -1, sizeof(int) * 19 * 503);

		fin.getline(line, 503);
		//strcpy_s(line, strchr(line, original[0])); //get rid of everything before first w.
		//*(strrchr(line, original[ocount-1])+1) = '\0';
		//cout << line << endl;
		for(int let = 0; let < ocount; let++) {
			for (int i = 0; i < strlen(line); i++) {
				if (original[let] == line[i]) {
					letters[let]->push_back(i);
				}
			}
		}
		int count = 0;
		intList::iterator it = letters[0]->begin();
		while (it != letters[0]->end()) {
			count += paths(0, *it);
			++it;
		}
		if (count < 10) {
			fout << "Case #" << caseNum << ": 000" << count << endl;
		} else if (count < 100) {
			fout << "Case #" << caseNum << ": 00" << count << endl;
		} else if (count < 1000) {
			fout << "Case #" << caseNum << ": 0" << count << endl;
		} else {
			fout << "Case #" << caseNum << ": " << count << endl;
		}
	}

	//char bah;
	//cin >> bah;
}