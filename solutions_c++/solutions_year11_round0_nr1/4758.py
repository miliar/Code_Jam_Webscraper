#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

vector<int> calculate(vector<int> seq){
	vector<int> res;
	for(int i= 1;i < seq.size();i++){
		int steps = abs(seq[i] - seq[i - 1]);
		res.push_back(steps);
	}
	return res;
}


int solve_prob(vector<char> seq, vector<int> O, vector<int> B){
	vector<int> Osteps, Bsteps;
	Osteps = calculate(O);
	Bsteps = calculate(B);
	int result, op, bp;
	op = bp = result = 0;
	for(int i=0;i<seq.size();i++){
		int steps;
		if( seq[i] == 'O'){
			steps = Osteps[op];
			if(bp < Bsteps.size()){
				Bsteps[bp] = max(Bsteps[bp] - steps - 1, 0);
			}
			result += steps + 1;
			op++;
		}else{
			steps = Bsteps[bp];
			if (op < Osteps.size()){
				Osteps[op] = max(Osteps[op] - steps - 1, 0);
			}
			result += steps + 1;
			bp++;
		}
	}
	return result;
}


int main(){
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("TestOutput.txt");
	int T;
	fin >> T;
	for(int testcase=1;testcase<=T;testcase++){
		int N;
		fin >> N;
		cout << N;
		vector<int> O, B;
		O.push_back(1);
		B.push_back(1);
		vector<char> seq;
		for(int j=0;j<N;j++){
			char c;
			int button;
			fin >> c >> button;
			char buff[100];
			itoa(button, buff, 10);
			string buf(buff);
			seq.push_back(c);
			if (c == 'O'){
				O.push_back(button);
			}
			else{
				B.push_back(button);
			}
		}
		int res = solve_prob(seq, O, B);
		fout << "Case #" << testcase << ": "<< res << endl;
	}
	cout << T;
	return 0;

}