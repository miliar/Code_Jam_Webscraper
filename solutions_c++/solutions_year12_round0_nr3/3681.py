#include <vector>
#include <string>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <set>
#include <map>
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

vector<string> split(const string &s, char delim=' ') {
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



//ofstream debug("Q3.debug");

map<int, vector<int> > rotmap;

class Pair {
	public:
	int a, b;
	Pair(int A, int B) : a(A), b(B) {}
};

bool operator==(Pair a, Pair b) {
	return (a.a == b.a) && (a.b == b.b);
}

bool operator<(Pair a, Pair b) {
	return a.a < b.b;
}

vector<int> rotations(int n) {
	string s = itoa(n);
	string orig = s;
	set<string> sv;
	//debug << orig << endl;
	sv.insert(orig);
	if(rotmap.find(n) != rotmap.end()) return rotmap[n];
	for(int i = 1; i < orig.length(); i++) {
		s = orig.substr(orig.length()-i) + orig.substr(0, orig.length()-i);
		//debug << "\t" << s << endl;
		sv.insert(s);
	}
	//debug << endl;
	vector<int> ret;
	for(auto it = sv.begin(); it != sv.end(); it++) {
		ret.push_back(atoi(it->c_str()));
	}
	rotmap[n] = ret;
	return ret;
}		

int main(int argc, char* argv[]) {
	ifstream data(argv[1]);
	string line;
	getline(data, line);
	int num = atoi(line.c_str());
	for(int i = 0; i < num; i++) {
		getline(data, line);
		int a = atoi(split(line)[0].c_str());
		int b = atoi(split(line)[1].c_str());
		set<Pair> pairs;
		for(int j = a; j <= b; j++) {
			vector<int> rots = rotations(j);
			for(auto it = rots.begin(); it != rots.end(); it++) {
				if(j < *it && *it <= b) pairs.insert(Pair(j, *it));
			}
		}
		cout << "Case #" << i+1 << ": " << pairs.size() << endl;
	}
	return 0;
}
		
