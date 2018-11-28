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
	unsigned int N, C, dummy_sum = 0, total_sum = 0, smallest_candy=-1;
	cin >> N;
	
	for(int n=0; n<N; n++){
		cin >> C;
		dummy_sum ^= C;
		total_sum += C;
		if(C < smallest_candy) smallest_candy = C;
	}
	
	if(dummy_sum)
		cout << "NO" << endl;
	else
		cout << ( total_sum - smallest_candy ) << endl;
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

