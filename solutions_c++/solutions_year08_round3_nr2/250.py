#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include <string>
using namespace std;


inline long long int findSolution(const string& exp, int i,
		int mod2, int mod3, int mod5, int mod7,
		int x2, int x3, int x5, int x7) {
	
	if(i > exp.size()) {
		return (mod2 == 0 || mod3 == 0 || mod5 == 0 || mod7 == 0) ? 1 : 0;
	}
	
	long long int y = exp[i] - '0';
	long long int result = 0;
	
	result += findSolution(exp, i + 1,
			(mod2 + x2) % 2, (mod3 + x3) % 3, (mod5 + x5) % 5, (mod7 + x7) % 7,
			y, y, y, y);
	
	if(i < exp.size()) 
		result += findSolution(exp, i + 1,
				(mod2 - x2) % 2, (mod3 - x3) % 3, (mod5 - x5) % 5, (mod7 - x7) % 7, 
				y, y, y, y);
	
	if(i < exp.size())
		result += findSolution(exp, i + 1,
			mod2, mod3, mod5, mod7,
			(x2 * 10 + y) % 2, (x3 * 10 + y) % 3, (x5 * 10 + y) % 5, (x7 * 10 + y) % 7);
	
	return result;
}

int findSolution(const string& exp) {
	int init = exp[0] - '0';
	return findSolution(exp, 1, 0, 0, 0, 0, init % 2, init % 3, init % 5, init % 7);
}

int main() {
	int N;
	
	ifstream fin("b.in");
	ofstream fout("b.out");
	
	
	fin >> N;
	fin.ignore();
	for(int n = 1; n <= N; n++) {
		string exp;
		
		getline(fin, exp);
		
		fout << "Case #" << n << ": " << findSolution(exp) << endl;
	}
}
