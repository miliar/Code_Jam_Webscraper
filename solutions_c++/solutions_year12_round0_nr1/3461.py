#include <map>
#include <vector>
#include <string>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <set>
#include <cmath>
#include <iostream>

using namespace std;

set<int> primes;

void setup() {
	ifstream in("primes.dat");
	string line;
	while(getline(in, line)) {
		primes.insert(atoi(line.c_str()));
	}
}

bool isPrime(int n) {
	if(n == 2 || n == 3) return true;
	if(n < 2 || n % 2 == 0) return false;
	if(primes.find(n) != primes.end()) return true;
	for(auto it = primes.begin(); *it < int(sqrt(n)); it++) {
		if(n % *it == 0) return false;
	}
	for(int i = 3; i <= int(sqrt(n)); i += 2) {
		if(primes.find(i) != primes.end()) continue;
		if(n % i == 0) return false;
	}
	primes.insert(n);
	return true;
}

string itoa(int i) {
	stringstream ss("");
	ss << i;
	return ss.str();
}

template<class T> vector<vector<T> > all_perms(vector<T> in) {
	vector<vector<T> > ret;
	do {
		ret.push_back(in);
	} while(next_permutation(in.begin(), in.end()));
	return ret;
}

vector<string>& split(const string& s, char delim, vector<string>& elems) {
	stringstream ss(s);
	string item;
	while(getline(ss, item, delim)) {
		elems.push_back(item);
	}
	return elems;
}

vector<string> split(const string &s, char delim) {
	vector<string> elems;
	return split(s, delim, elems);
} 

vector<int> avtoiv(vector<string> in) {
	vector<int> ret;
	for(auto it = in.begin(); it != in.end(); it++) {
		ret.push_back(atoi(it->c_str()));
	}
	return ret;
}

template<class T> ostream& operator<<(ostream& str, vector<T> v) {
	for(auto it = v.begin(); it != v.end(); it++) {
		str << *it;
		if(it < v.end()-1) str << " ";
	}
	return str;
}

map<char, char> t;

void read() {
	t['a'] = 'y';
	t['o'] = 'e';
	t['z'] = 'q';
	t[' '] = ' ';
	ifstream in("translate.dat");
	string line;
	while(getline(in, line)) {
		t[split(line, ' ')[0][0]] = split(line, ' ')[1][0];
	}
}

int main(int argc, char* argv[]) {
	if(argc < 2) return -1;
	setup();
	read();
	ifstream data(argv[1]);
	if(!data.is_open()) return -2;
	string line;
	getline(data, line);
	int count = atoi(line.c_str());
	for(int i = 0; i < count; i++) {
		getline(data, line);
		for(int j = 0; j < line.length(); j++) {
			line[j] = t[line[j]];
		}
		cout << "Case #" << i+1 << ": " << line << endl;
	}
	return 0;
}
