#include <fstream>
#include <cmath>

int main(){

	std::ifstream infile("A-large.in");
	std::ofstream outfile("A-large.out");

	int numCases;
	infile >> numCases;

	for (int i = 1; i <= numCases; i++){
		int n , k;
		infile >> n;
		infile >> k;

		unsigned long int pow2 = 1U;
		pow2 <<= n;
		unsigned long int onNum = pow2 -1;

		while (k > onNum)
			k-= pow2;

		outfile << "Case #"<<i; 

		if (k == onNum)
			outfile<< ": ON"<<std::endl;
		else 
			outfile<<": OFF"<<std::endl;
	}

	infile.close();
	outfile.close();
}
