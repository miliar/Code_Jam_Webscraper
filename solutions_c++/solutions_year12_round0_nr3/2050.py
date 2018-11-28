#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <set>
using namespace std;

void num2digits(unsigned long n, vector<int> &digits){
	digits.clear();
	while(n!=0) {
		digits.insert(digits.begin(), n%10);
		n /= 10;
	}
}

unsigned long digits2num(vector<int> &digits){
	unsigned long sum=0;
	unsigned size=digits.size();
	for(unsigned i=0; i<size; i++){
		sum+=digits[i]*pow(10, size-i-1);
		
	}
	return sum;
}

void permut(vector<int> &digits){
	digits.insert(digits.begin(), digits.back());
	digits.pop_back();
}

int main(int argc, char *argv[]) {
	ifstream input("/home/pabratte/Downloads/C-large.in");
	if(!input){
		cerr<<"ERROR"<<endl;
	}
	
	int nTestCases;
	unsigned long a, b;
	input>>nTestCases;
	vector<int> numDigits;
	// los pares que ya contamos
	set< pair<unsigned long, unsigned long> > currentPairs;
	
	for(int i=0; i<nTestCases; i++){
		input>>a>>b;
		currentPairs.clear();
		// recorremos los numeros de a a b
		for(unsigned long j=a; j<b; j++){
			num2digits(j, numDigits);
			//	recorremos las permutaciones del numero
			for(int k=0; k<numDigits.size()-1; k++){
				permut(numDigits);
				unsigned long num;
				num=digits2num(numDigits);
				// j tiene que estar entre a y b (sabemos que es >a)
				// num tiene que estar entre a y b
				// num tiene que ser > j
				// el par no tiene que estar contado ya
				// tienen que tener la misma cantidad de digitos (si tienen un leading 0 el numero va a ser menor que a) 
				if(num<=b && j<num && currentPairs.find(pair<unsigned long, unsigned long>(j,num))==currentPairs.end()){
					currentPairs.insert(pair<unsigned long, unsigned long>(j,num));
				}
			}
			
		}
		cout<<"Case #"<<i+1<<": "<<currentPairs.size()<<endl;
	}
	input.close();
	
	return 0;
}
