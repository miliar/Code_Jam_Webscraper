#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {

	ifstream infile("A-small-attempt0.in");
	ofstream outfile("output.txt");
	int cases;
	infile >> cases;

	for( int i = 0; i != cases; i++) 
	{
		vector<int> vect1;
		vector<int> vect2;

		int length;
		infile >> length;

		for( int j = 0; j != length; j++) 
		{
			int temp;
			infile >> temp;
			vect1.push_back(temp);
		}
		for( int j = 0; j != length; j++) 
		{
			int temp;
			infile >> temp;
			vect2.push_back(temp);
		}
		

		// sort vect1 first
		sort(vect1.begin(), vect1.end());
		// sort vect2 too
		sort(vect2.begin(), vect2.end());
		// and reverse them
		reverse(vect2.begin(), vect2.end());
		
		int sum = 0;
		for( int j = 0; j != length; j++ ) {
			sum += (vect1[j] * vect2[j]);
		}
		outfile << "Case #" << i+1 << ": " << sum << endl;
	}
	

	infile.close();
	system("pause");
	return 0;
}