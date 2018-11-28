#include <fstream>
#include <iostream>
#include <strstream>
#include <string>
#include <vector>

using namespace std;

void eol(istream &is) {
	string str;
	getline(is, str);
}

template <typename T>
T GetOneInALine(istream &inStream) {
	T toReturn;
	inStream >> toReturn;
	eol(inStream);
	return toReturn;
}

template <typename T>
vector<T> GetAllInALine(istream &inStream) {
	string line;
	getline(inStream, line);
	istrstream lineStream(line.c_str());
	vector<T> toReturn;
	T toAdd;
	while (!lineStream.eof()) {
		lineStream >> toAdd;
		toReturn.push_back(toAdd);
	}
	return toReturn;
}

struct Letter{
	char n;
	char vec[26];
};

void ProcessLetterVec(istream &inStream, Letter *let) {
	let->n = 0;
	char c;
	do {
		inStream >> c;
		if (c == ')')
			return;
		let->vec[(let->n)++] = c;
	} while (1);
}

int Calc(void **dict, Letter *l, int len) {
	if (len == 0)
		return (int)dict;
	int sum = 0;
	for (int i=0; i<l->n; ++i) {
		if (dict[l->vec[i]-'a'])
			sum += Calc((void**)dict[l->vec[i]-'a'], l+1, len-1);
	}
	return sum;
}

int ProcessWord(istream &inStream, void **dict, int len) {
	Letter word[26];
	for (int i=0; i<len; ++i) {
		char c;
		inStream >> c;
		if (c == '(')
			ProcessLetterVec(inStream, &word[i]);
		else {
			word[i].n = 1;
			word[i].vec[0] = c;
		}
	}
	eol(inStream);
	return Calc(dict, word, len);
}

void NewDictEnt(void ***dict) {
	*dict = (void**)malloc(26*sizeof(void*));
	for (int i=0; i<26; ++i)
		(*dict)[i] = (void*)0;
}

void ReadWord(istream &inStream, int L, void **dict) {
	char c;
	inStream >> c;
	if (L>1) {
		if (!dict[c-'a'])
			NewDictEnt((void***)&dict[c-'a']);
		ReadWord(inStream, L-1, (void**)(dict[c-'a']));
	} else {
		eol(inStream);
		dict[c-'a'] = (void*)1;
	}
}

int Run(istream &inStream) {
	int L, D, N;
	inStream >> L >> D >> N;
	eol(inStream);
	void **dict = NULL;
	NewDictEnt(&dict);
	for (int i=0; i<D; ++i) {
		ReadWord(inStream, L, dict);
	}
	for (int j=0; j<N; ++j) {
		cout << "Case #" << j+1 << ": " << ProcessWord(inStream, dict, L) << "\n";
	}

	return 0;
}

int main(int argc, char* argv[])
{
	if (argc < 2)
		return Run(cin);
	else {
		ifstream inStream(argv[1]);
		return Run(inStream);
	}
}
