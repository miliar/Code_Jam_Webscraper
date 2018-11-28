#include <iostream>
#include <map>
#include <vector>

using namespace std;

void read_engines(int nofengines,map<string, bool> &engines);
void read_queries(int nofqueries,vector<string> &queries);
void clear_engines(map<string, bool> &engines);
bool exist_engine(map<string, bool> engines);
int eat_list(vector<string> queries, map<string, bool> engines);

int main() {
	string noinp;
	cin >> noinp;

	// Az inputok szamaszor megcsinalja amit kell...
	for (int i=0; i < atoi(noinp.c_str()); ++i) {
		string str;
		cin >> str;
		map<string,bool> engines;
		read_engines(atoi(str.c_str()), engines);

		cin >> str;
		vector<string> queries;
		read_queries(atoi(str.c_str()), queries);

		//Johet a lenyeg:



		//Az eredmeny kiiratasa:
		cout << "Case #" << i+1 << ": " << eat_list(queries,engines) << endl;

		//Kiiratjuk a beolvasott adatokat:
		/*
		for (map<string,bool>::iterator it = engines.begin(); it != engines.end(); ++it) {
			cout << (*it).first << endl;
		}
		for (int j = 0; j < queries.size(); ++j) {
			cout << queries[j] << endl;
		}
		*/
	}
	return 0;
}

bool exist_engine(map<string, bool> engines) {
	for (map<string,bool>::iterator it = engines.begin(); it != engines.end(); ++it) {
		if ( (*it).second == false ) {
			return true;
		}
	}
	return false;
}

void clear_engines(map<string, bool> &engines) {
	for (map<string,bool>::iterator it = engines.begin(); it != engines.end(); ++it) {
		(*it).second = false;
	}
}

int eat_list(vector<string> queries, map<string, bool> engines) {
	int num = 0;
	for (int i = 0; i < queries.size(); ++i) {
		engines[queries[i]] = true;
		if ( !exist_engine(engines) ) {
			++num;
			clear_engines(engines);
			engines[queries[i]] = true;
		}
	}
	return num;
}

void read_queries(int nofqueries,vector<string> &queries) {
	string str;
	getline(cin, str);
	for (int i = 0; i < nofqueries; ++i) {
		getline(cin, str);
		queries.push_back(str);
	}
}

void read_engines(int nofengines,map<string, bool> &engines) {
	string str;
	getline(cin, str);
	for (int i = 0; i < nofengines; ++i) {
		getline(cin, str);
		engines.insert(pair<string,bool>(str, false));
	}
}

