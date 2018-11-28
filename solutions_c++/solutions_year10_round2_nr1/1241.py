#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <map>
#include <list>
#include <vector>
using namespace std;

struct Dir{
	map<string, Dir*> mMap;
};
void Parse(string line, list<string>*strs) {
	istringstream iss(line);
	iss.get();	// read first delim.
	while (!iss.eof()) {
		char word[100];
		iss.getline(word, 100, '/');
		strs->push_back(string(word));
	}
}
int mkdir(list<string>::iterator lst, list<string>::iterator end, Dir &dir) {
	if (lst == end)
		return 0;
	string seg = *lst;
	Dir *src = dir.mMap[seg];
	int toReturn = 0;
	if (!src) {
		src = new Dir;
		dir.mMap[seg] = src;
		toReturn++;
	}
	return toReturn + mkdir(++lst, end, *src);
}
void dealloc(Dir &dir) {
	for (map<string,Dir*>::iterator it = dir.mMap.begin(); it!=dir.mMap.end(); ++it)
		delete (*it).second;
}

int Process(istream &in) {
	int N, M;
	in >> N >> M;
	int i;
	string line;
	Dir root;
	for (i=0; i<N; ++i) {
		in >> line;
		list<string> dir;
		Parse(line, &dir);
		mkdir(dir.begin(), dir.end(), root);
	}
	int toReturn=0;
	for (i=0; i<M; ++i) {
		in >> line;
		list<string> dir;
		Parse(line, &dir);
		toReturn += mkdir(dir.begin(), dir.end(), root);
	}
	dealloc(root);
	return toReturn;
}

void main(int argc, char *argv[]) {
	int t;
	istream *in;
	if (argc==1)
		in=&cin;
	else
		in = new ifstream(argv[1]);
	*in >> t;
	for (int i=1; i<=t; ++i) {
		cerr << "Case #" << i << " of " << t << "\n";
		cout << "Case #" << i << ": " << Process(*in) << "\n";
	}
}