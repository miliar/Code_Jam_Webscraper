#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>

using namespace std;

struct Move {
	char c;
	int num;
};

int calc(vector<Move> &moves, vector<Move> &mb, vector<Move> &mo) {
	int n = 0;

	int lo = 1;
	int lb = 1;
	unsigned int move = 0; // which move
	unsigned int bmove = 0;
	unsigned int omove = 0;

	//cout << "moves " << moves.size();
	while (move < moves.size()) {
		n++;

		//cout << n << ". ";
		Move &m = moves[move];
		if (m.c == 'O') {
			if (lo == m.num) {
				move++;
				omove++;
				//cout << " O push, ";
			} else {
				lo += m.num > lo ? 1 : -1;
				//cout << "O go " << lo << ", ";
			}
			if (bmove < mb.size()) {
				Move &x = mb[bmove];
				if (x.num == lb) {
					//cout << "B stay, ";
				} else {
					lb += x.num > lb ? 1 : -1;
					//cout << "B go " << lb << ", ";
				}
			}

		} else {
			if (lb == m.num) {
				move++;
				bmove++;
				//cout << " B push, ";
			} else {
				lb += m.num > lb ? 1 : -1;
				//cout << "B go " << lb << ", ";
			}
			if (omove < mo.size()) {
				Move &x = mo[omove];
				if (x.num == lo) {
					//cout << "O stay, ";
				} else {
					lo += x.num > lo ? 1 : -1;
					//cout << "O go " << lo << ", ";
				}
			}
		}
		//cout << endl;
	}

	return n;
}

int main(int argc, char **argv) {
	string ifilename = "A-small.in";
	string ofilename = "A-small.out";
	ifstream ifs(ifilename.c_str());
	ofstream ofs(ofilename.c_str());

	int n, m;
	ifs >> n;


	for (int i = 0; i < n; ++i) {
		ifs >> m;
		vector<Move> moves;
		vector<Move> mb;
		vector<Move> mo;
		for (int j = 0; j < m; ++j) {
			Move m;
			ifs >> m.c >> m.num;
			moves.push_back(m);
			if (m.c == 'O')
				mo.push_back(m);
			else
				mb.push_back(m);
		}
		int res = calc(moves, mb, mo);
		ofs << "Case #" << (i+1) << ": " << res << endl;
	}



	ifs.close();
	ofs.close();
	return 0;
}
