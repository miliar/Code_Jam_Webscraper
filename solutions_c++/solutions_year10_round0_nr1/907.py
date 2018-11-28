#include <iostream>
#include <vector>
#include <iterator>
#include <sstream>
#include <algorithm>
#include <map>
#include <queue>
#include <cmath>

using namespace std;

template<class T>
void read_line(vector<T>& vec); 
template<class T>
void read_table(vector<vector<T> >& table, const int nlines); 
template<class T>
void dump_line(const vector<T>& vec); 
template<class T>
void dump_table(const vector<vector<T> >& table); 

int main() 
{
	int N, i = 0, ncases; 
	long long K, tmp, power;
	cin >> ncases;
	for (int i = 0; i < ncases; i++) {
		cin >> N >> K; 
		cout << "Case #" << i+1 << ": "; 
		power = (long long) pow(2, N); 
		//cout << endl << power << endl; //debug
		tmp = K - power + 1; 
		//cout << endl << tmp << endl; //debug
		if (tmp % power == 0)
			cout << "ON" << endl; 
		else
			cout << "OFF" << endl; 
	}
	return 0;
}

template<class T>
void read_line(vector<T>& vec) 
{
	string s; 
	do {
		getline(cin, s);
	} while (cin.good() && s.size() == 0); 
	stringstream stream(s); 
	copy(istream_iterator<T> (stream), istream_iterator<T> (), back_inserter(vec));
}

template<class T>
void dump_vec(const vector<T>& vec) 
{
	for (int i = 0; i < vec.size(); i++) {
		cout << vec[i] << " "; 
	}
	cout << endl; 
}

template<class T>
void read_table(vector<vector<T> >& table, const int nlines) {
	for (int i = 0; i < nlines; i++) {
		vector<T> vec;
		read_line(vec);
		table.push_back(vec); 
	}
}

template<class T>
void dump_table(const vector<vector<T> >& table) {
	for (int i = 0; i < table.size(); i++) {
		for (int j = 0; j < table[i].size(); j++) {
			cout << table[i][j] << " ";
		}
		cout << endl; 
	}
}
