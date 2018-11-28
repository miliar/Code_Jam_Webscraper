#include <iostream>
#include <queue>
#include <vector>
#include <fstream>

using namespace std;


struct coaster {
	int size;
	int curr_size;
};

struct problem {
	int R;
	int k;
	int groups[1000];
	int N;
};

vector<problem> prlist;

int solve_case(int R, int k, int groups[], int N) {
	int money = 0, t = 0;
	coaster c;
	c.size = k;
	c.curr_size = 0;
	queue<int> q;
	queue<int> oncoaster;
	int tmp = 0;

	for(int i=0; i<N; i++) {
		q.push(groups[i]);
	}
	while(t < R) {
		if(!q.empty()) {
			tmp = q.front();
			if(c.curr_size + tmp > c.size || q.empty()) {
				money += c.curr_size;
				t++;
				c.curr_size = 0;
				while(!oncoaster.empty()) {
					int g = oncoaster.front();
					q.push(g);
					oncoaster.pop();
				}
			}
			else {
				q.pop();
				oncoaster.push(tmp);
				c.curr_size += tmp;
			}
		}
		else {
			money += c.curr_size;
			t++;
			c.curr_size = 0;
			while(!oncoaster.empty()) {
				int g = oncoaster.front();
				q.push(g);
				oncoaster.pop();
			}
		}
	}
	return money;
}

void read_file() {
	ifstream in;
	in.open("input.txt");
	int T;
	if(in) {
		in >> T;
		for(int i=0; i<T; i++) {
			problem *p = new problem();
			in >> p->R;
			in >> p->k;
			in >> p->N;
			for(int j=0; j<p->N; j++) {
				in >> p->groups[j];
			}
			prlist.push_back(*p);
		}
	}
}

void write_file(vector<problem> &prl) {
	ofstream out;
	out.open("output.txt");
	if(out) {
		for(int i=0; i<prl.size(); i++) {
			out <<"Case #" << i+1 << ": " << solve_case(prl[i].R, prl[i].k, prl[i].groups, prl[i].N) << endl;
		}
	}
}
int main() {
	read_file();
	write_file(prlist);
	return 0;
}