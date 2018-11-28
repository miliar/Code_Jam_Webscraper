#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;


ifstream fin("input");
ofstream out("output");

class Sta{
	public:
		int cur;
		int left;
};
Sta stalist[2];
int cnt;

void init(){
	cnt = 0;
	stalist[0].cur = 1;
	stalist[1].cur = 1;
	stalist[0].left = 0;
	stalist[1].left = 0;
}

int process() {
	int total = 0;
	fin >> total;
	Sta* now = NULL;
	Sta* ano = NULL;
	string peo;
	int button;
	for(int i = 0; i < total; i++) {
		fin >> peo >> button;
		if(peo == "B") {
			now = &(stalist[1]);
			ano = &(stalist[0]);
		} else {
			now = &(stalist[0]);
			ano = &(stalist[1]);
		}
		int move = abs(button - now->cur);
		int add = 0;
		if(now->left >= move) {
			add = 1;
		} else {
			add = move - now->left + 1;
		}
		cnt += add;
		ano->left += add;
		now->left = 0;
		now->cur = button;

	}
	return cnt;
}

int main() {
	int cnum = 0;
	fin >> cnum;
	for(int i = 0; i < cnum; i++) {
		init();
		out << "Case #" << i + 1 << ": " << process() << endl;
	}
	fin.close();
	out.close();
}

