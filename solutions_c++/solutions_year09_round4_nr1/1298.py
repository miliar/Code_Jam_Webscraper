#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#define INF 9999999
using namespace std;

int swaps (vector < string > mat, vector < string > n_mat) {
	int c = 0;
	map <int,bool> done;
	vector <int> v(mat.size());
	for (int i = 0; i < mat.size(); i++) {
		for (int j = 0; j < n_mat.size(); j++) {
			if (n_mat[j] == mat[i] && !done[j]) {
				v[i] = j;
				done[j] = true;
				break;
			}
		}
	}
	int mi;
	for (int k = 0; k < v.size(); k++) {
	for (int i = 0; i < v.size()-1; i++) {
		mi = v[i];
		if (mi > v[i+1]) {
			swap(v[i],v[i+1]);
			c++;
		}
	}
	}
	return c;
}

bool yesi (vector < string > mat) {
	int n = mat.size();
	for (int i = 0; i < n; i++) {
		for (int j = i+1; j < n; j++) {
			if (mat[i][j] == '1') return false;
		}
	}
	return true;
}

int main () {

	ifstream fin("in.txt");
	ofstream fout("out1.txt");
	int t;
	fin >> t;
	
	for (int T = 1; T <= t; T++) {
	
		int n;
		fin >> n;
		
		vector < string > mat(n);
		vector < string > n_mat;
		for (int i = 0; i < n; i++) {
			fin >> mat[i];
		}
		n_mat = mat;
		sort(n_mat.begin(),n_mat.end());
		int mi = INF;
		do {
			if (yesi(n_mat)) {
				int c = swaps(mat,n_mat);
				if (mi > c) mi = c;
			}
		} while (next_permutation(n_mat.begin(),n_mat.end()));
		
		fout << "Case #" << T << ": " << mi << "\n";
	}
	return 0;
}