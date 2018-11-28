#include <vector>
#include <list>
#include <map>
#include <string>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <cstdlib>

using namespace std;

string getline(){
	string tmp;
	getline(cin, tmp);
	return tmp;
}

typedef unsigned long long huge;

void solveCase(){
	long long N;
	int Pd, Pt;
	cin >> N >> Pd >> Pt;
	
	if(Pt == 100 && Pd < 100){
		cout << "Broken" << endl;
		return;
	}
	if(Pt == 0 && Pd > 0){
		cout << "Broken" << endl;
		return;
	}
	if(Pt > 0 && Pd == 0){
		cout << "Possible" << endl;
		return;
	}
	if(Pt == 0 && Pd == 0){
		cout << "Possible" << endl;
		return;
	}
	if(Pd == 100){
		cout << "Possible" << endl;
		return;
	}
	
	
	int M = 100, Wd = Pd;
	
	if(Wd % 5 == 0){
		M /= 5;
		Wd /= 5;
	}
	if(Wd % 5 == 0){
		M /= 5;
		Wd /= 5;
	}
	if(Wd % 2 == 0){
		M /= 2;
		Wd /= 2;
	}
	if(Wd % 2 == 0){
		M /= 2;
		Wd /= 2;
	}
	
	//cout << "[N=" << N << ", M=" << M << ", Pd=" << Pd << ", Pt=" << Pt << "] ";
	
	if(M > N)
		cout << "Broken" << endl;
	else
		cout << "Possible" << endl;
}

int main(int argc, char *argv[]){
	stringstream line(getline());
	unsigned int T;
	
	line >> T;
	
	for(unsigned int t=1; t<=T; t++){
		cout << "Case #" << t << ": ";
		cerr << "Case #" << t << endl;
		solveCase();
	}
	
	return 0;
}

