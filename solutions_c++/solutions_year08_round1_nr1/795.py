#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

//debugging macro
#define trace(expr) cout << #expr << endl;

int main(){

	ifstream inFile;
	ofstream outFile;

	vector <int> a, b;

	inFile.open("1.dat");
	outFile.open("1.out");

	int T, n;

	inFile>>T;

	for (int i = 1; i <= T; i++){
		inFile>>n;

		int temp;

		for (int j = 0; j < n; j++){
			inFile>>temp;
			a.push_back(temp);
		}

		for (int j = 0; j < n; j++){
			inFile>>temp;
			b.push_back(temp);
		}

		//vectors full.
		//you'll always want the smallest numbers multiplying the larger numbers.

		sort(b.begin(),b.end());
		sort(a.begin(),a.end());
		reverse(a.begin(), a.end());

		for (int j = 0; j < n; j++){
			cout<<a[j]<<" "<<endl;
		}
		cout<<endl;
		for (int j = 0; j < n; j++){
			cout<<b[j]<<" "<<endl;
		}
		cout<<endl;

		//calculate scalar product
		int scalar = 0;

		for (int j = 0; j < n; j++){
			scalar += a[j] * b[j];
		}

		cout<<scalar<<endl;
		outFile<<"Case #"<<i<<": "<<scalar<<endl;

		a.clear();
		b.clear();
	}


	inFile.close();
	outFile.close();

}