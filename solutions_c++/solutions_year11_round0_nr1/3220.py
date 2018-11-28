#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

int main() {
	ifstream fin("A-large.in");
	ofstream fout("output.txt");
	int T, N;
	fin >> T;
	for(int i = 0; i < T; i++) {
		fin >> N;
		bool oPush[101] = {0}, bPush[101] = {0};
		vector<int> oOrder;
		vector<int> bOrder;
		int op = 1, bp = 1;
		int sec = 0;
		for(int j = 0; j < N; j++) {
			string s;
			int n;
			fin >> s >> n;
			if(s == "O") {
				oOrder.push_back(n);
				oPush[j] = true;
			}
			else {
				bOrder.push_back(n);
				bPush[j] = true;
			}
		}
		for(int j = 0; j < N; j++) {
			if(oPush[j]) {
				int oGoal = oOrder[0], bGoal = 0;
				if(bOrder.size() > 0)
					bGoal = bOrder[0];
				int oDist = abs(op - oGoal) + 1, bDist = abs(bp - bGoal);
				if(oDist <= bDist)
					if(bGoal > bp) bp += oDist;
					else bp -= oDist;
				else
					bp = bGoal;
				op = oGoal;
				sec += oDist;
				oOrder.erase(oOrder.begin());
			}
			else {
				int bGoal = bOrder[0], oGoal = 0;
				if(oOrder.size() > 0)
					oGoal = oOrder[0];
				int bDist = abs(bp - bGoal) + 1, oDist = abs(op - oGoal);
				if(bDist <= oDist)
					if(oGoal > op) op += bDist;
					else op -= bDist;
				else
					op = oGoal;
				bp = bGoal;
				sec += bDist;
				bOrder.erase(bOrder.begin());
			}
		}
		fout << "Case #" << i + 1 << ": " << sec << endl;
	}
	fin.close();
	fout.close();
	return 0;
}