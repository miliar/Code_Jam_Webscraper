#include <iostream>
#include <fstream>
using namespace std;

unsigned long long int countProm(unsigned long long int l,unsigned long long int p,unsigned long long int c){
	unsigned long long int temp = l * c;
	unsigned long long int count = 0;
	while (temp < p) {
		count++;
		temp *= c;
	}
	return count;
	
}

unsigned long long int countChecks(unsigned long long int count){
	if(count == 1){
		return 1;
	}
	return countChecks(count / 2) + 1;
}

int main (int argc, char * const argv[]) {
	
	int tests,test;
	ifstream in("B.in");
	ofstream out("B-out.txt");
	unsigned long long int l,p,c;
	unsigned long long int count, checks;
	
	in >> tests;
	for (test = 0; test < tests; test++) {
		
		in >> l >> p >> c;
		
		if(test == 846){
			test = 846;
		}
		
		count = countProm(l,p,c);
		if(count > 0){
			checks = countChecks(count);
		}else{
			checks = 0;
		}
		
		
		out << "Case #" << test + 1 << ": " << checks << endl;
		cout << "Case #" << test + 1 << ": " << checks << endl;
	}
	
	cin >> test;
	
	return 0;
}
