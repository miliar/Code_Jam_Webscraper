#include <iostream>
using namespace std;

typedef int num;
num t, n, m;
const num max_n = 100;
const num max_m = 100;
char paths1[100*max_n+1];
char paths2[100*max_m+1];

num mkdir(char * path) {
	//cout << path << endl;
	num index = 0;
	for (num i = 0; i < 100; i++) {
		if (path[i] == '/') {
			index = i;
		} else if (path[i] == '\0') {
			break;
		}
	}
	num res = 0;
	bool add = true;
	for (num i = 0; i < n; i++) {
		bool same = true;
		for (num j = 0; j < 100; j++) {
			if (paths1[i*100+j] != path[j]) {
				same = false;
				break;
			}
			if (path[j] == '\0' || paths1[i*100+j] == '\0') {
				break;
			}
		}
		if (same) {
			add = false;
			break;
		}
	}
	if (add) {
		//cout << "added\n";
		res++;
		num j;
		for (j = 0; j < 100 && path[j] != '\0'; j++) {
			paths1[n*100+j] = path[j];
		}
		paths1[n*100+j] = '\0';
		n++;
	}
	if (index > 0) {
		path[index] = '\0';
		res += mkdir(path);
	}
	return res;
}

num get_result() {
	num res = 0;
	for (num i = 0; i < m; i++) {
		res += mkdir(paths2+i*100);
	}
	return res;
}

int main() {
	cin >> t;
	for (num i = 0; i < t; i++) {
		cin >> n >> m;
		for (num j = 0; j < n; j++) {
			cin >> (paths1+j*100);
		}
		for (num k = 0; k < m; k++) {
			cin >> (paths2+k*100);
		}
		cout << "Case #" << (i+1) << ": " << get_result() << '\n';
	}
	cout.flush();
	return 0;
}
