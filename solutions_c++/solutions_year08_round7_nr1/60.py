#include <cmath>
#include <string>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cstdlib>
//#include <hash_map>
using namespace std;

struct Node {
	string name;
	int len;
	int children[1000];
	string schild[1000];
};


int C;
int N;
int M;
int numNodes;

int answer[1000];

Node nodes[1000];

int compare(const void *a, const void * b) {
	return *((int*)a) - *((int*)b);
}

bool isNew(string s) {
	for (int i = 0; i < N; i++) {
		if (nodes[i].name == s) {
			return false;
		}
	}
	return true;
}

int findIndex(string s) {
	for (int i = 0; i < N; i++) {
		if (nodes[i].name == s) {
			return i;
		}
	}
	return -1;
}

int findAns(int x) {
	if (nodes[x].len == 0) {
		return 1;
	} else {
		int bowls[1000];
		for (int i = 0; i < nodes[x].len; i++) {
			bowls[i] = findAns(nodes[x].children[i]);
		}
		qsort(bowls,nodes[x].len,sizeof(bowls[0]),compare);
		int num = nodes[x].len;
		int max = bowls[num-1];
		for (int i = num-2; i >=0; i--) {
			if (num-1 - i + bowls[i] > max) {
				max = num - 1 - i + bowls[i];
			}
		}
		if (num + 1 > max) {
				max = num + 1;
			}
		return max;
	}

}

int main() {
	fstream in;
	fstream out;
	in.open("prob1.in", fstream::in);
	out.open("prob1.out",fstream::out);

	in >> C;
	for (int a = 0; a < C; a++) {
		in >> N;
		string n, temp;
		for (int b = 0; b < N; b++) {
			in >> n >> M;
			nodes[b].name = n;
			nodes[b].len = 0;
			for (int c = 0; c < M; c++) {
				in >> temp;
				if (((int)'A') <= temp.at(0) && temp.at(0) <= ((int)'Z')) {
					nodes[b].schild[nodes[b].len] = temp;
					nodes[b].len++;
				}
			}
		}
		for (int d = 0; d < N; d++) {
			for (int e = 0; e < nodes[d].len; e++) {
				nodes[d].children[e] = findIndex(nodes[d].schild[e]);
			}
		}
		int ans;

		ans = findAns(0);

		out << "Case #" << a + 1 << ": " << ans << endl;
	}
	
	in.close();
	out.close();
	return 0;
}