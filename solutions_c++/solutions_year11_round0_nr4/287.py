#include <vector>
#include <list>
#include <map>
#include <string>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>

using namespace std;

string getline(){
	string tmp;
	getline(cin, tmp);
	return tmp;
}

void solveCase(){
	int N;
	cin >> N;
	
	int number, moves=N;
	
	for(int n=1; n<=N; n++){
		cin >> number;
		if(number==n) moves--;
	}
	
	cout << moves << ".000000" << endl;
}

int main(int argc, char *argv[]){
	stringstream line(getline());
	unsigned int T;
	
	line >> T;
	
	for(unsigned int t=1; t<=T; t++){
		cout << "Case #" << t << ": ";
		solveCase();
	}
	
	return 0;
}

