#include <iostream>
#include <fstream>
#include <cstdio>
#include <string>
#include <cstring>

using namespace std;

const int maxn = 1024;

int N;
int total,minn,sum;

ifstream fin("input.txt");

void input() {
	fin >> N;
	minn = -1;
	total = 0;
	sum = 0;
	int x;
	for (int i=0;i<N;i++) {
		fin >> x;
		if (minn == -1) minn = x; else minn = min(x, minn);
		total = total ^ x;
		sum += x;
	}
}

int main() {

	int T;
	fin >> T;
	for (int t=1;t<=T;t++) {	
		input();
		if (total == 0)
			cout << "Case #" << t << ": " << sum - minn << "\n";
		else
			cout << "Case #" << t << ": " << "NO" << "\n";
	}

	return 0;	

}

