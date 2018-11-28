#include <fstream>
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

struct mypair {
	int p;
	int v;
	mypair(int p, int v) {
		this->p = p;
		this->v = v;
	}
	mypair() {};
	bool operator < (const mypair& pp) {
		return p < pp.p;
	}
};

bool prov(const vector<mypair> v, int time, int d) {
	int left, right;
	
	
	if (v.size() == 0)
		return true;
	int n = v.size();
	right = -2000000000;

	for (int i = 0; i< v.size(); i++) {
		if (v[i].p - time > right) {
			left = v[i].p - time;
		} else {
			left = right;
		}
		right = left+d*(v[i].v-1);
		if (abs(right - v[i].p) > time)
			return false;
		right += d;
	}
	return true;
}

int main() {
	ifstream infi("input.txt");
	ofstream outf("output.txt");
	int t;
	infi >> t;
	vector<mypair> vv;
	for (int tt = 0; tt < t; tt++) {
		int c, d;
		vv.clear();
		infi >> c >> d;
		d = d*2;
		for (int i = 0; i<c; i++) {
			int p, v;
			infi >> p >> v;
			vv.push_back(mypair(p*2,v));
		}
		sort(vv.begin(), vv.end());
		for (int i = 0; i< vv.size(); i++)
			cout << vv[i].p << " " << vv[i].v << endl;
		
		for (int i = 0; i< 7; i++)
			cout << i<<"\t" << prov(vv, i, d) << endl;
		int time = 0;
		while (!prov(vv, time, d))
			time++;
		outf << "Case #"<<tt+1<<": " << double(time)/2 <<endl;
	}
	outf.close();
	return 0;
}