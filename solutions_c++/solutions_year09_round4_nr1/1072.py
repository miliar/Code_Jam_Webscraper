#include <fstream>
#include <iostream>
#include <strstream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <iterator>

using namespace std;

void eol(istream &is) {
	string str;
	getline(is, str);
}

int swap(int *v, int i, int j) {
	int tmp = v[j];
	for (int l=j; l>i; --l)
		v[l] = v[l-1];
	v[i] = tmp;
	return j-i;
}

int Process(istream &inStream) {
	int N, i, j;
	inStream >> N;
	eol(inStream);
	int *v = new int[N];
	for (i=0; i<N; ++i) {
		int max=-1;
		for (j=0; j<N; ++j) {
			char c;
			inStream >> c;
			if (c=='1')
				max = j;
		}
		v[i]=max;
		eol(inStream);
	}
	int pts=0;
	for (i=0; i<N; ++i) {
		if (v[i]>i) {
			for (j=i+1; j<N; ++j) {
				if (v[j] <= i) {
					pts += swap(v, i, j);
					break;
				}
			}
		}
	}
	delete v;
	return pts;
}

int Run(istream &inStream) {
	int T;
	inStream >> T;
	// eol(inStream);
	for (int j=0; j<T; ++j) {
		cerr << "Case #" << j+1 << "\n";
		cout << "Case #" << j+1 << ": " << Process(inStream) << "\n";
	}

	return 0;
}

int main(int argc, char* argv[])
{
	if (argc < 2)
		return Run(cin);
	else {
		ifstream inStream(argv[1]);
		return Run(inStream);
	}
}
