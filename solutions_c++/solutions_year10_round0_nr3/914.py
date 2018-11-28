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
	int T, N, index, sindex;
	long long R, k, ppls, euros;
	bool end_reached; 
	cin >> T;
	for (int i = 0; i < T; i++) {
		vector<long long> gs; 
		cin >> R >> k >> N;	
		read_line(gs);
		index = 0;
		euros = 0; 
		while (R > 0) {
			ppls = 0; 
			end_reached = false; 
			sindex = index; 
			while (ppls + gs[index] <= k && (!end_reached || index < sindex)) {
				ppls += gs[index++];
				if (index == gs.size()) {
					end_reached = true; 
					index = 0;
				}
			}
			euros += ppls; 	
			R--;
		}
		cout << "Case #" << i+1 << ": " << euros << endl; 
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
void dump_line(const vector<T>& vec) 
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
