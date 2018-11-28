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

#define DIM 100

bool grid1[DIM][DIM]; 
bool grid2[DIM][DIM]; 

void zero_grids() {
	for (int i = 0; i < DIM; i++) {
		for (int j = 0; j < DIM; j++) {
			grid1[i][j] = 0;
			grid2[i][j] = 0;
		}
	}
}

void grid2_to_grid1() {
	for (int i = 0; i < DIM; i++) {
		for (int j = 0; j < DIM; j++) {
			grid1[i][j] = grid2[i][j];
		}
	}
}

void dump_grid1() {
	for (int i = 0; i < DIM; i++) {
		for (int j = 0; j < DIM; j++) {
			cout << grid1[j][i] << " ";
		}
		cout << endl;
	}
	cout << "-------------------" << endl;
}

int main() 
{
	int T, R, x1, y1, x2, y2; 
	cin >> T;
	for (int c = 0; c < T; c++) {
		zero_grids();
		cin >> R;
		for (int i = 0; i < R; i++) {
			cin >> x1 >> y1 >> x2 >> y2;
			for (int j = x1-1; j <= x2-1; j++) {
				for (int k = y1-1; k <= y2-1; k++) {
					grid1[j][k] = 1;
				}
			}
		}
		bool bact = 1;
		int secs = 0;
		while (bact) {
			//dump_grid1();
			bact = 0;
			for (int i = 1; i < DIM; i++) {
				for (int j = 1; j < DIM; j++) {
					if (grid1[i][j]) {
						if (!grid1[i-1][j] && !grid1[i][j-1]) {
							grid2[i][j] = 0;
						} else {
							grid2[i][j] = 1;
							bact = 1;
						}
					} else {
						if (grid1[i-1][j] && grid1[i][j-1]) {
							grid2[i][j] = 1;
							bact = 1;
						} else {
							grid2[i][j] = 0;
						}
					}
				}
			}
			grid2_to_grid1();
			secs++;
		}
		cout << "Case #" << c+1 << ": " << secs << endl; 
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
