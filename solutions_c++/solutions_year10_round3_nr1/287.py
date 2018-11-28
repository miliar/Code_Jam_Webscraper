#include <iostream>
#include <vector>
#include <iterator>
#include <sstream>
#include <algorithm>
#include <map>
#include <set>
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
void split(const string &s, char delim, vector<string> &elems); 
template<class T>
void get_index(vector<T>& vec, const T& key); 

int main() 
{
	int T, N, a, b, cnt; 
	vector<pair<int, int> > wires;
	cin >> T;
	for (int c = 0; c < T; c++) {
		cin >> N;
		cnt = 0;
		for (int i = 0; i < N; i++) {
			cin >> a >> b;
			for (int j = 0; j < wires.size(); j++) {
				if ((a < wires[j].first && b > wires[j].second) ||
						(a > wires[j].first && b < wires[j].second))
					cnt++; 
			}
			wires.push_back(pair<int, int> (a, b)); 
		}
		cout << "Case #" << c+1 << ": " << cnt << endl; 
		wires.clear();
	}
	return 0;
}

void split(const string &s, char delim, vector<string> &elems) 
{
    stringstream ss(s);
    string item;
    while (getline(ss, item, delim)) {
        if (item.size() > 0) 
			  elems.push_back(item);
    }
}

template<class T>
void get_index(vector<T>& vec, const T& key) 
{
	for (int i = 0; i < vec.size(); i++) {
		if (vec[i] == key)
			return i; 
	}
	return vec.size(); 
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
