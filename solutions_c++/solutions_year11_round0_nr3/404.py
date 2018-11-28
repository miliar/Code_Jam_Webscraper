#include <iostream>
#include <fstream>

using namespace std;


int  search(int n, int* c, bool* selected, int p /* next candy*/);
int quick(int n, int* c);

int main() {
	ifstream fin("C-large.in");
	ofstream fout("C-large.out");
	int t;// test cases
	fin >> t;
	int n;
	int c[1000];
	bool selected[1000];
	for (int i = 0 ; i < t; i++) {
		fin >> n;
		
		int acl = 0;
		for (int j = 0 ; j < n; j++) {
			fin >> c[j];
			selected[j] = false;
			acl += c[j];
		}
		//int res = search(n, c, selected, 0);
		
		int res = quick(n, c);
		if (res > 0) {
			fout << "Case #" << i+1 << ": " << res << endl;
		}
		else {
			fout << "Case #" << i+1 << ": NO" << endl;
		}
		
	}
	fin.close();
	fout.close();
	return 0;
}

int  search(int n, int* c, bool* selected, int p /* next candy*/) {
	if ( p >= n) {
		int selectCount = 0, unselectCount = 0, count = 0, un_count = 0;
		for (int i = 0; i < n; i++) {
			if ( selected[i] ) {
				selectCount ^= c[i];
				count += c[i];
			}
			else {
				unselectCount ^= c[i];
				un_count += c[i];
			}
		}
		if (selectCount != unselectCount || count == 0 || un_count == 0) 
			count = -1;
		return count;
	}
	selected[p] = true;
	int res_s = search(n, c, selected, p + 1);
	selected[p] = false;
	int res_uns = search(n, c, selected, p + 1);
	return max( res_s, res_uns);
}

int quick(int n, int* c) {
	int s = 0, sum = 0;
	for (int i = 0 ; i < n; i++) {
		s ^= c[i];
		sum += c[i];
	}
	if ( s == 0) {
		int min = c[0];
		for (int i = 1 ; i < n; i++) 
			if (c[i] < min) 
				min = c[i];
		return sum - min;
	}
	else 
		return -1;
}


