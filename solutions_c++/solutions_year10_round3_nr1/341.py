#include <iostream>
#include <fstream>
using namespace std;

int main (int argc, char * const argv[]) {
	
	int tests,test;
	ifstream in("A.in");
	ofstream out("A-out.txt");
	int count;
	int n, i, j,	x[1000], y[1000];
	
	in >> tests;
	for (test = 0; test < tests; test++) {
		in >> n;
		for (i=0; i<n; i++) {
			in >> x[i] >> y[i];
		}
		count = 0;
		for (i=0; i<n; i++) {
			for (j=i+1; j<n; j++) {
				if((x[i] - x[j])*(y[i]-y[j]) < 0){
					count++;
				}
			}
		}
		
		
		out << "Case #" << test + 1 << ": " << count << endl;
		cout << "Case #" << test + 1 << ": " << count << endl;
	}
	
	cin >> test;
	
	return 0;
}
