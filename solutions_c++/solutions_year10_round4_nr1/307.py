#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

bool check(const vector< vector<int> > & a) {
	const int N = a.size();
	vector< vector<int> > b(2*N-1, vector<int>(2*N-1, -1));
	for (int i = 0; i < N; ++ i) {
		for (int j = 0; j < N; ++ j) {
 			b[i+j][N-1-i+j] = a[i][j];
		}
	}
	//for (int i = 0; i < 2*N-1; ++ i) {
	//	for (int j = 0; j < 2*N-1; ++ j) {
	//		if (b[i][j] < 0) cerr << " ";
	//		else cerr << b[i][j];
	//	}
	//	cerr << endl;
	//}
	for (int i = 0; i < N-1; ++ i) {
		int i2 = 2*N-2-i;
		for (int j = 0; j < 2*N-1; ++ j) {
			if (b[i][j] >= 0 && b[i2][j] >= 0 && b[i][j] != b[i2][j]) return false;
		}
	}
	for (int i = 0; i < N-1; ++ i) {
		int i2 = 2*N-2-i;
		for (int j = 0; j < 2*N-1; ++ j) {
			if (b[j][i] >= 0 && b[j][i2] >= 0 && b[j][i] != b[j][i2]) return false;
		}
	}
	return true;
}

int func(const int k, const vector<string>& input) {
	vector< vector<int> > a(k, vector<int>(k));
	for (int j = 0; j < (int)input.size(); ++ j) {
		int i = 0;
		istringstream in(input[j]);
		int n;
		while (in >> n) {
			if (j < k) {
				a[i][k-1-j+i] = n;
			} else {
				a[j+1-k+i][i] = n;
			}
			++ i;
		}
	}
	//for (int i = 0; i < (int)a.size(); ++ i) {
	//	for (int j = 0; j < (int)a[i].size(); ++ j) {
	//		cerr << a[i][j] << " ";
	//	}
	//	cerr << endl;
	//}
	//if (check(a)) {
	//	cerr << "ok" << endl;
	//} else {
	//	cerr << "ng" << endl;
	//}
	//cerr << endl;
	for (int i = 0; ; ++ i) {
		for (int j = 0; j <= i; ++ j) {
			for (int k = 0; k <= i; ++ k) {
				vector< vector<int> > b(a.size()+i, vector<int>(a.size()+i, -1));
				for (unsigned l = 0; l < a.size(); ++ l) {
					for (unsigned m = 0; m < a.size(); ++ m) {
						b[j+l][k+m] = a[l][m];
					}
				}
				if (check(b)) return 2*i*a.size() + i*i;
			}
		}
	}
}

int main() {
	string buf;
	getline(cin, buf);
	int N = atoi(buf.c_str());
	for (int i = 1; i <= N; ++ i) {
		getline(cin,buf);
		int k = atoi(buf.c_str());
		vector<string> input(2*k-1);
		for (unsigned j = 0; j < input.size(); ++ j) {
			getline(cin, input[j]);
		}
		cout << "Case #" << i << ": " << func(k, input) << endl;
	}
}
