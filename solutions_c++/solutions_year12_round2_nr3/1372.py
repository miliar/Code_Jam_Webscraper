#include <iostream>
#include <fstream>
using namespace std;

	ofstream fout("C-small-attempt1.out");

int place[500];

bool find(int data[], int begin, int diff, int length) {
	if (begin >= length)
		return false;
	if (diff == data[begin]) {
		place[begin] = 2;
		return true;
	}
	else if (-diff == data[begin]) {
		place[begin] = 1; 
		return true;
	}
	else {
		if (find(data, begin+1, diff, length)) {
			return true;
		}
		else if (find(data, begin+1, diff + data[begin], length)) {
			place[begin] =1;
			return true;
		}
		else if (find(data, begin+1, diff - data[begin], length)) {
			place[begin] = 2;
			return true;
		}
	}
	return false;
}

int main() {
	int T;
	ifstream fin("C-small-attempt1.in");
	fin >> T;
	for (int i = 1; i <= T; i++) {
		int cnt;
		fin >> cnt;
		int *data = new int[cnt];
		for (int j = 0; j < cnt; j++) {
			fin >> data[j];
		}
		for (int j = 0; j < 500; j++) {
			place[j] = 0;
		}
		fout << "Case #" << i << ": " << endl;
		if (!find(data, 0, 0, cnt)) {
			fout << "Impossible";
		}
		else {
			for (int k = 0; k < cnt; k++) {
				if (place[k] == 1)
					fout << data[k] << " ";
			}
			fout << endl;
			for (int k = 0; k < cnt; k++) {
				if (place[k] == 2)
					fout << data[k] << " ";
			}

		}
		delete [] data;
		fout << endl;
	}
}